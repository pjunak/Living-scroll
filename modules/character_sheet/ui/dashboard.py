"""Redesigned Character Dashboard."""

from __future__ import annotations

from typing import Dict, List, Optional
from pathlib import Path

from PySide6.QtCore import Qt, QSize, Signal
from PySide6.QtGui import QIcon, QPainter, QColor, QPen, QBrush, QPixmap
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSplitter,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QGridLayout,
    QDialog,
    QToolTip,
    QStackedWidget,
    QMessageBox,
)

from modules.character_sheet.ui.builder.dialog import CharacterBuilderDialog

from modules.character_sheet.model import CharacterSheet, ABILITY_NAMES, EquipmentItem
from modules.character_sheet.services.library import CharacterRecord, DEFAULT_LIBRARY_PATH
from modules.compendium.modifiers.state import ModifierStateSnapshot
from modules.dnd24_mechanics.engine import CharacterEngine
from modules.equipment.ui.window import EquipmentWindow
from modules.core.ui.dialogs.equipment_entry_dialog import EquipmentEntryDialog
from modules.core.application_context import ApplicationContext
from modules.core.ui.resources import get_app_icon
from modules.core.ui.theme import COLORS

# --- Local Styling Constants (aliased from global theme) ---
DASH_COLORS = {
    "bg_base": COLORS["bg_base"],
    "bg_card": COLORS["bg_card"],
    "bg_hero": COLORS["bg_hero"],
    "accent": COLORS["accent_primary"],
    "accent_dim": COLORS["accent_dim"],
    "text_main": COLORS["text_primary"],
    "text_dim": COLORS["text_dim"],
    "border": COLORS["border_dim"],
    "success": COLORS["success"],
    "danger": COLORS["danger"],
}


class _StatHex(QWidget):
    """Custom painted hexagonal stat widget."""
    def __init__(self, label: str, value: int, modifier: int, tooltip_text: str = "", parent=None):
        super().__init__(parent)
        self._label = label
        self._value = value
        self._modifier = modifier
        self.setFixedSize(60, 70)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        if tooltip_text:
            self.setToolTip(tooltip_text)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Draw Hexagon-like shape (or just a nice rounded panel for now)
        # Using rounded rect for simplicity unless hex strictly required
        rect = self.rect().adjusted(2, 2, -2, -2)
        
        # Background
        painter.setBrush(QBrush(QColor(DASH_COLORS["bg_card"])))
        painter.setPen(QPen(QColor(DASH_COLORS["border"]), 1))
        painter.drawRoundedRect(rect, 12, 12)

        # Text
        painter.setPen(QColor(DASH_COLORS["accent"]))
        font = painter.font()
        font.setPixelSize(10)
        font.setBold(True)
        painter.setFont(font)
        painter.drawText(rect.adjusted(0, 5, 0, 0), Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter, self._label)

        # Modifier (Big)
        painter.setPen(QColor(DASH_COLORS["text_main"]))
        font.setPixelSize(22)
        font.setBold(True)
        painter.setFont(font)
        mod_str = f"{self._modifier:+d}"
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, mod_str)

        # Score (Small bubble at bottom)
        score_rect = rect.adjusted(10, rect.height() - 20, -10, -2)
        painter.setBrush(QBrush(QColor(DASH_COLORS["bg_base"])))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(score_rect, 8, 8)
        
        painter.setPen(QColor(DASH_COLORS["text_dim"]))
        font.setPixelSize(10)
        font.setBold(False)
        painter.setFont(font)
        painter.drawText(score_rect, Qt.AlignmentFlag.AlignCenter, str(self._value))


class CharacterDashboard(QWidget):
    """
    The new 'Golden Standard' Character Sheet.
    Features: Dashboard layout, 'Equipped' toggle, collapsible drawers.
    """

    def __init__(self, record: CharacterRecord, app_context: ApplicationContext, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._app_context = app_context
        # Initialize the Unidirectional State Store
        from modules.character_sheet.store import CharacterStore
        self._store = CharacterStore(record, self._app_context.ensure_library(), self._app_context.ensure_compendium(), self)
        self._store.character_updated.connect(self._on_character_updated)

        self._record = self._store.record
        self._sheet = self._store.sheet
        self._engine = self._store.engine
        
        # Placeholder for modifier snapshot
        self._modifier_snapshot = ModifierStateSnapshot([], self._record.modifiers)
        
        # Helper map for spellcasting
        self._class_casting_map = {
            "Wizard": "INT", "Artificer": "INT",
            "Cleric": "WIS", "Druid": "WIS", "Ranger": "WIS", "Monk": "WIS",
            "Bard": "CHA", "Paladin": "CHA", "Sorcerer": "CHA", "Warlock": "CHA"
        }

        self._init_ui()

    def _init_ui(self, is_rebuild=False):
        # Main Layout
        if not is_rebuild:
            self.setLayout(QVBoxLayout())
            self.layout().setContentsMargins(0, 0, 0, 0)
            self.layout().setSpacing(0)
            self.setStyleSheet(f"background-color: {DASH_COLORS['bg_base']}; color: {DASH_COLORS['text_main']}; font-family: 'Segoe UI';")
            
        main_layout = self.layout()

        # 1. Header (Identity + Vitals)
        self._header = self._build_header_section()
        main_layout.addWidget(self._header)

        # 2. Main Split Area
        main_split = QSplitter(Qt.Orientation.Horizontal)
        main_split.setHandleWidth(1)
        main_split.setStyleSheet(f"QSplitter::handle {{ background: {DASH_COLORS['border']}; }}")
        
        # 1. Column 1: Attributes, Saves, Skills
        left_panel = self._build_left_panel()
        main_split.addWidget(left_panel)

        # 2. Column 2: Main Workspace (Tabs)
        center_panel = QWidget()
        center_panel_layout = QVBoxLayout(center_panel)
        center_panel_layout.setContentsMargins(0, 0, 0, 0)
        center_panel_layout.setSpacing(0)
        
        # Navigation Bar
        self._nav_bar = self._build_nav_bar()
        center_panel_layout.addWidget(self._nav_bar)
        
         # Stacked Content
        self._stack = QStackedWidget()
        
        # Page 0: Overview
        self._overview_page = self._build_overview_page()
        self._stack.addWidget(self._overview_page)
        
        # Page 1: Backpack
        self._inventory_page = InventoryPage(self._record, self._app_context, self)
        self._stack.addWidget(self._inventory_page)
        
        # Page 2+: Placeholders
        self._grimoire_page = QLabel("Grimoire (Coming Soon)")
        self._grimoire_page.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._stack.addWidget(self._grimoire_page)
        
        # Page 3: Features
        self._features_page = FeaturesPage(self._record, self._app_context, self)
        self._stack.addWidget(self._features_page)
        
        # Page 4: Notes (Placeholder)
        self._notes_page = QLabel("Notes (Coming Soon)")
        self._notes_page.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._stack.addWidget(self._notes_page)
        
        center_panel_layout.addWidget(self._stack)
        main_split.addWidget(center_panel)

        # 3. Column 3: The Inspector
        self._inspector_panel = self._build_inspector_panel()
        main_split.addWidget(self._inspector_panel)
        
        # Set Split Ratios (25%, 50%, 25%)
        main_split.setStretchFactor(0, 1)
        main_split.setStretchFactor(1, 2)
        main_split.setStretchFactor(2, 1)

        main_layout.addWidget(main_split, 1)
        
        # Refresh on tab change
        self._stack.currentChanged.connect(self._on_tab_changed)

    def _build_overview_page(self) -> QWidget:
        page = QWidget()
        layout = QVBoxLayout(page)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # Header is now global, no need to include locally
        
        # Action Area
        self._action_area = self._build_action_area()
        layout.addWidget(self._action_area, 1)
        
        return page

    def _rebuild_ui(self):
        # Legacy hook, might not need full rebuild anymore with tabs.
        # Just refresh current view.
        self._refresh_ui()

    def _on_tab_changed(self, index):
        # Refresh the page we just switched to
        if index == 0:
             self._refresh_overview()
        elif index == 1:
             self._inventory_page.refresh()
        elif index == 3:
             self._features_page.refresh()
            
    def _refresh_overview(self):
        # We need to refresh the Equipped items list
        # Check if the layout exists to update it
        if hasattr(self, '_action_content_layout'):
             # Clear layout
             layout = self._action_content_layout
             while layout.count():
                 child = layout.takeAt(0)
                 if child.widget(): child.widget().deleteLater()
                 
             # Rebuild
             equipped_items = [i for i in self._sheet.equipment if i.equipped]
             
             if not equipped_items:
                  empty = QLabel("No items equipped. Open Backpack to equip weapons or armor.")
                  empty.setStyleSheet(f"color: {DASH_COLORS['text_dim']}; font-style: italic; padding: 20px;")
                  empty.setAlignment(Qt.AlignmentFlag.AlignCenter)
                  layout.addWidget(empty)
             else:
                  for item in equipped_items:
                      card = self._create_item_card(item)
                      layout.addWidget(card)
                      
             layout.addStretch()

    def _refresh_ui(self):
        # Store current tab if it exists
        current_idx = 0
        if hasattr(self, '_stack') and self._stack:
            current_idx = self._stack.currentIndex()
            
        # Clear main layout and rebuild
        layout = self.layout()
        if layout:
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()
                    
        self._init_ui(is_rebuild=True)
        
        # Restore tab
        if hasattr(self, '_stack') and self._stack:
            self._stack.setCurrentIndex(current_idx)

    def _drawer_closed(self):
        self._refresh_ui()

    def _on_character_updated(self, record, engine):
        """Called automatically by the CharacterStore when the character is modified."""
        self._record = record
        self._sheet = record.sheet
        self._engine = engine
        self._refresh_ui()

    def _increase_hp(self):
        hp_breakdown = self._engine.get_hp_breakdown()
        max_hp = hp_breakdown['total']
        self._sheet.combat.current_hp = min(max_hp, self._sheet.combat.current_hp + 1)
        self._store.dispatch_update(self._sheet, self._record.modifiers)

    def _decrease_hp(self):
        self._sheet.combat.current_hp = max(0, self._sheet.combat.current_hp - 1)
        self._store.dispatch_update(self._sheet, self._record.modifiers)


        # (Sidebar removed to merge into left_panel)


    def _build_header_section(self) -> QWidget:
        container = QFrame()
        container.setObjectName("HeaderContainer")
        container.setStyleSheet(f"QFrame#HeaderContainer {{ background: {DASH_COLORS['bg_hero']}; border-bottom: 1px solid {DASH_COLORS['border']}; }}")
        container.setFixedHeight(140)
        
        layout = QHBoxLayout(container)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        # Left: Portrait + Name
        # Check portrait
        portrait_widget = QLabel()
        portrait_widget.setFixedSize(100, 100)
        portrait_widget.setObjectName("PortraitWidget")
        portrait_widget.setStyleSheet(f"QLabel#PortraitWidget {{ background-color: {DASH_COLORS['bg_base']}; border-radius: 8px; border: 1px solid {DASH_COLORS['accent']}; }}")
        portrait_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        p_path = self._record.sheet.identity.portrait_path
        if p_path:
             if not Path(p_path).is_absolute():
                  full_p = DEFAULT_LIBRARY_PATH / "portraits" / p_path
             else:
                  full_p = Path(p_path)
             
             if full_p.exists():
                 pix = QPixmap(str(full_p))
                 portrait_widget.setPixmap(pix.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation))
        
        layout.addWidget(portrait_widget)

        # Identity
        id_layout = QVBoxLayout()
        id_layout.setSpacing(4)
        name_lbl = QLabel(self._record.display_name)
        name_lbl.setStyleSheet("font-size: 24px; font-weight: 800; color: white;")
        
        sub_lbl = QLabel(f"Level {self._record.level} {self._record.sheet.identity.ancestry} {self._record.class_summary}")
        sub_lbl.setStyleSheet(f"color: {DASH_COLORS['text_dim']}; font-size: 14px;")
        
        id_layout.addWidget(name_lbl)
        id_layout.addWidget(sub_lbl)
        id_layout.addStretch()
        layout.addLayout(id_layout)

        layout.addStretch()

        layout.addStretch()

        # Edit button
        edit_btn = QPushButton("✎ Edit Character")
        edit_btn.setToolTip("Edit Character")
        edit_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        edit_btn.setStyleSheet(f"""
            QPushButton {{
                background-color: transparent;
                color: {DASH_COLORS['text_dim']};
                border: 1px solid {DASH_COLORS['border']};
                border-radius: 4px;
                padding: 8px 12px;
                font-weight: 700;
                font-size: 12px;
            }}
            QPushButton:hover {{
                color: {DASH_COLORS['accent']};
                border-color: {DASH_COLORS['accent']};
                background-color: rgba(155, 89, 182, 0.1);
            }}
        """)
        edit_btn.clicked.connect(self._open_editor)
        
        vitals_layout = QVBoxLayout()
        top_row = QHBoxLayout()
        top_row.addStretch()
        
        # HP Adjustment (Moved to top row for prominence)
        hp_breakdown = self._engine.get_hp_breakdown()
        hp_str = f"{self._sheet.combat.current_hp} / {hp_breakdown['total']}"
        hp_val = QLabel(hp_str)
        hp_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hp_val.setMinimumWidth(80) # Prevent shifting when numbers cross 10 or 100
        hp_val.setProperty("class", "AdjustValue")
        hp_val.setToolTip(hp_breakdown['tooltip'])
        
        hp_layout = QHBoxLayout()
        hp_layout.setContentsMargins(0, 0, 0, 0)
        hp_layout.setSpacing(8)
        
        btn_minus = QPushButton("–")
        btn_minus.setFixedSize(26, 26)
        btn_minus.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_minus.setProperty("class", "AdjustMinus")
        btn_minus.clicked.connect(self._decrease_hp)
        
        btn_plus = QPushButton("+")
        btn_plus.setFixedSize(26, 26)
        btn_plus.setCursor(Qt.CursorShape.PointingHandCursor)
        btn_plus.setProperty("class", "AdjustPlus")
        btn_plus.clicked.connect(self._increase_hp)

        hp_lbl = QLabel("HP")
        hp_lbl.setProperty("class", "StatBoxLabel")
        
        hp_layout.addWidget(hp_lbl)
        hp_layout.addSpacing(4)
        hp_layout.addWidget(btn_minus)
        hp_layout.addWidget(hp_val)
        hp_layout.addWidget(btn_plus)
        
        hp_widget = QWidget()
        hp_widget.setLayout(hp_layout)

        top_row.addWidget(hp_widget)
        top_row.addSpacing(20)
        top_row.addWidget(edit_btn)
        
        vitals_layout.addLayout(top_row)

        # Vitals (AC, Init, Prof, Speed)
        # Using a grid for tight packing
        vitals_grid = QGridLayout()
        vitals_grid.setHorizontalSpacing(30)
        vitals_grid.setVerticalSpacing(5)

        # AC
        ac_breakdown = self._engine.get_ac_breakdown()
        ac_val = QLabel(str(ac_breakdown['total']))
        ac_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ac_val.setProperty("class", "StatBoxValue")
        ac_val.setToolTip(ac_breakdown['tooltip'])
        ac_lbl = QLabel("AC")
        ac_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ac_lbl.setProperty("class", "StatBoxLabel")
        
        vitals_grid.addWidget(ac_val, 0, 0)
        vitals_grid.addWidget(ac_lbl, 1, 0)

        # Initiative
        init_breakdown = self._engine.get_initiative_breakdown()
        init_val = QLabel(f"{init_breakdown['total']:+d}")
        init_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        init_val.setProperty("class", "StatBoxValue")
        init_val.setToolTip(init_breakdown['tooltip'])
        init_lbl = QLabel("INITIATIVE")
        init_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        init_lbl.setProperty("class", "StatBoxLabel")
        
        vitals_grid.addWidget(init_val, 0, 1)
        vitals_grid.addWidget(init_lbl, 1, 1)

        # Proficiency
        prof_breakdown = self._engine.get_proficiency_breakdown()
        prof_val = QLabel(f"{prof_breakdown['total']:+d}")
        prof_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        prof_val.setProperty("class", "StatBoxValue")
        prof_val.setToolTip(prof_breakdown['tooltip'])
        prof_lbl = QLabel("PROF.")
        prof_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        prof_lbl.setProperty("class", "StatBoxLabel")
        
        vitals_grid.addWidget(prof_val, 0, 2)
        vitals_grid.addWidget(prof_lbl, 1, 2)

        # Speed
        speed_breakdown = self._engine.get_speed_breakdown()
        speed_val = QLabel(str(speed_breakdown['total']))
        speed_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
        speed_val.setProperty("class", "StatBoxValue")
        speed_val.setToolTip(speed_breakdown['tooltip'])
        speed_lbl = QLabel("SPEED")
        speed_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        speed_lbl.setProperty("class", "StatBoxLabel")
        
        vitals_grid.addWidget(speed_val, 0, 3)
        vitals_grid.addWidget(speed_lbl, 1, 3)

        # Spell Stats (Conditional)
        cast_ability = self._get_primary_spellcasting_ability()
        
        if cast_ability:
            try:
                ability_obj = self._sheet.get_ability(cast_ability)
                # Ensure we use engine logic for the cast ability
                mod = (self._engine.get_ability_breakdown(cast_ability)["total"] - 10) // 2
                prof = self._engine.calculated_proficiency_bonus()
                
                dc = 8 + prof + mod
                atk = prof + mod
                
                # DC
                dc_val = QLabel(str(dc))
                dc_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
                dc_val.setProperty("class", "StatBoxValue")
                dc_val.setStyleSheet(f"color: {DASH_COLORS['accent']};")
                dc_lbl = QLabel(f"SAVE DC ({cast_ability})")
                dc_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                dc_lbl.setProperty("class", "StatBoxLabel")
                
                vitals_grid.addWidget(dc_val, 0, 4)
                vitals_grid.addWidget(dc_lbl, 1, 4)

                # Attack
                atk_val = QLabel(f"{atk:+d}")
                atk_val.setAlignment(Qt.AlignmentFlag.AlignCenter)
                atk_val.setProperty("class", "StatBoxValue")
                atk_lbl = QLabel("SPELL ATK")
                atk_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
                atk_lbl.setProperty("class", "StatBoxLabel")
                
                vitals_grid.addWidget(atk_val, 0, 5)
                vitals_grid.addWidget(atk_lbl, 1, 5)
                
            except KeyError:
                pass # Should not happen with valid map

        vitals_layout.addLayout(vitals_grid)
        layout.addLayout(vitals_layout)

        return container
        
    def _get_primary_spellcasting_ability(self) -> str | None:
        """Determines primary spellcasting ability based on classes."""
        # TODO: Handle multi-classing more robustly (currently takes highest level caster)
        best_ability = None
        highest_level = -1
        
        for cls_entry in self._sheet.identity.classes:
            name = cls_entry.name
            level = cls_entry.level
            
            # Simple substring match for "Eldritch Knight" or "Arcane Trickster" could follow later
            # For now direct map
            ability = self._class_casting_map.get(name)
            if ability:
                if level > highest_level:
                     highest_level = level
                     best_ability = ability
        
        return best_ability

    def _build_action_area(self) -> QWidget:
        area = QWidget()
        layout = QVBoxLayout(area)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Section Title
        title_row = QHBoxLayout()
        lbl = QLabel("Equipped & Ready")
        lbl.setStyleSheet(f"font-size: 16px; font-weight: 700; color: {DASH_COLORS['accent']}; text-transform: uppercase; letter-spacing: 1px;")
        title_row.addWidget(lbl)
        title_row.addStretch()
        layout.addLayout(title_row)

        # Scroll for items
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setStyleSheet("background: transparent;")
        
        content = QWidget()
        self._action_content_layout = QVBoxLayout(content)
        self._action_content_layout.setContentsMargins(0, 10, 0, 10)
        self._action_content_layout.setSpacing(10)

        # Initial Population
        self._refresh_overview()

        scroll.setWidget(content)
        layout.addWidget(scroll)
        
        return area
        
    def _build_left_panel(self) -> QWidget:
        """Attributes, Saves, and Skills List"""
        panel = QFrame()
        panel.setObjectName("LeftPanel")
        panel.setStyleSheet(f"QFrame#LeftPanel {{ background-color: {DASH_COLORS['bg_card']}; border-right: 1px solid {DASH_COLORS['border']}; }}")
        panel.setFixedWidth(340)  # Wider to fit Hex + Saves + Skills horizontally
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(10, 10, 10, 10)
        
        lbl = QLabel("ATTRIBUTES & SKILLS")
        lbl.setStyleSheet(f"font-weight: bold; color: {DASH_COLORS['text_dim']}; font-size: 12px; letter-spacing: 1px;")
        layout.addWidget(lbl)
        
        # Scroll for list
        scroll = QScrollArea()
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        scroll.setWidgetResizable(True)
        content = QWidget()
        c_layout = QVBoxLayout(content)
        c_layout.setSpacing(8)  # Space between attribute groups
        
        # Group skills by attribute
        from modules.character_sheet.ui.builder.utils.selection_helpers import SKILL_ABILITY_MAP, ALL_SKILLS
        
        grouped_skills = {}
        for skill in ALL_SKILLS:
            attr = SKILL_ABILITY_MAP.get(skill, "OTHER")
            if attr not in grouped_skills:
                grouped_skills[attr] = []
            grouped_skills[attr].append(skill)
            
        attr_order = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
        
        # Helper to calculate bonus
        def calc_skill_bonus(skill_name, attr_name):
            breakdown = self._engine.get_ability_breakdown(attr_name)
            total = breakdown['total']
            mod = (total - 10) // 2
            
            prof_level = self._sheet.proficiencies.skills.get(skill_name, 0)
            pb = self._engine.calculated_proficiency_bonus()
            
            bonus = mod
            if prof_level >= 1:
                bonus += pb
            if prof_level >= 2: # Expertise
                bonus += pb
                
            return bonus, prof_level
            
        for attr in attr_order:
            skills = grouped_skills.get(attr, [])
            attr_block = QFrame()
            attr_block.setObjectName("AttrBlock")
            attr_block.setStyleSheet(f"QFrame#AttrBlock {{ background-color: {DASH_COLORS['bg_base']}; border-radius: 6px; }}")
            attr_layout = QHBoxLayout(attr_block)
            attr_layout.setContentsMargins(6, 6, 6, 6)
            attr_layout.setSpacing(10)
            
            # Left side: Hex ONLY
            hex_col = QVBoxLayout()
            hex_col.setAlignment(Qt.AlignmentFlag.AlignTop)
            
            # 1. Hex
            breakdown = self._engine.get_ability_breakdown(attr)
            total = breakdown['total']
            mod = (total - 10) // 2
            hex_widget = _StatHex(attr, total, mod, tooltip_text=breakdown['tooltip'])
            hex_col.addWidget(hex_widget, 0, Qt.AlignmentFlag.AlignHCenter)
            
            attr_layout.addLayout(hex_col)
            
            # Right side: Save and Skills
            right_col = QVBoxLayout()
            right_col.setAlignment(Qt.AlignmentFlag.AlignTop)
            right_col.setSpacing(2)
            right_col.setContentsMargins(10, 0, 0, 0)
            
            # 2. Saving Throw Row
            save_row = QWidget()
            sr_layout = QHBoxLayout(save_row)
            sr_layout.setContentsMargins(0, 0, 0, 0)
            sr_layout.setSpacing(4)
            
            # Proficiencies are stored as a list in 'saves', so we check membership
            is_proficient = attr in getattr(self._sheet.proficiencies, "saves", [])
            save_prof = 1 if is_proficient else 0
            
            save_bonus = mod
            if save_prof >= 1:
                save_bonus += self._engine.calculated_proficiency_bonus()
                
            sign = "+" if save_bonus >= 0 else ""
            
            save_prof_indicator = QLabel("●" if save_prof >= 1 else "○")
            save_prof_indicator.setFixedWidth(15)
            save_prof_indicator.setStyleSheet(f"color: {DASH_COLORS['accent'] if save_prof >= 1 else DASH_COLORS['text_dim']}; font-size: 12px;")
            
            save_lbl_val = QLabel(f"{sign}{save_bonus}")
            save_lbl_val.setFixedWidth(25)
            save_lbl_val.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
            save_lbl_val.setStyleSheet(f"color: {DASH_COLORS['accent']}; font-weight: bold;")
            
            save_lbl_name = QLabel("Saving Throw")
            save_lbl_name.setStyleSheet(f"color: {DASH_COLORS['text_dim']}; font-size: 10px; font-weight: bold; text-transform: uppercase; letter-spacing: 1px;")
            
            sr_layout.addWidget(save_prof_indicator)
            sr_layout.addWidget(save_lbl_val)
            sr_layout.addWidget(save_lbl_name)
            sr_layout.addStretch()
            
            right_col.addWidget(save_row)
            
            # Skills
            if skills:
                # Add a subtle separator
                sep = QFrame()
                sep.setFrameShape(QFrame.Shape.HLine)
                sep.setStyleSheet(f"background-color: {DASH_COLORS['border']};")
                sep.setFixedHeight(1)
                right_col.addWidget(sep)
                
                for skill in skills:
                    bonus, prof_level = calc_skill_bonus(skill, attr)
                    sign = "+" if bonus >= 0 else ""
                    
                    style = f"color: {DASH_COLORS['text_dim']};"
                    font_weight = "normal"
                    text_decoration = "none"
                    indicator = "○"
                    indicator_color = DASH_COLORS['text_dim']
                    
                    if prof_level >= 1:
                        style = f"color: {DASH_COLORS['text_main']};"
                        font_weight = "bold"
                        indicator = "●"
                        indicator_color = DASH_COLORS['accent']
                        
                    if prof_level >= 2:
                        text_decoration = "underline"
                        indicator = "★"
                    
                    row = QWidget()
                    r_layout = QHBoxLayout(row)
                    r_layout.setContentsMargins(0, 0, 0, 0)
                    r_layout.setSpacing(4)
                    
                    # Indicator
                    ind_lbl = QLabel(indicator)
                    ind_lbl.setFixedWidth(15)
                    ind_lbl.setStyleSheet(f"color: {indicator_color}; font-size: 12px;")
                    
                    # Bonus
                    bonus_lbl = QLabel(f"{sign}{bonus}")
                    bonus_lbl.setFixedWidth(25)
                    bonus_lbl.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)
                    bonus_lbl.setStyleSheet(f"color: {DASH_COLORS['accent']}; font-weight: bold;")
                    
                    # Name
                    name_lbl = QLabel(skill)
                    name_lbl.setStyleSheet(f"{style} font-weight: {font_weight}; text-decoration: {text_decoration};")
                    
                    r_layout.addWidget(ind_lbl)
                    r_layout.addWidget(bonus_lbl)
                    r_layout.addWidget(name_lbl)
                    r_layout.addStretch()
                    
                    right_col.addWidget(row)
                    
            attr_layout.addLayout(right_col)
                
            c_layout.addWidget(attr_block)

        c_layout.addStretch()
        scroll.setWidget(content)
        layout.addWidget(scroll)
        
        return panel

    def _build_inspector_panel(self) -> QWidget:
        """Right-most panel for contextual details."""
        panel = QFrame()
        panel.setStyleSheet(f"background-color: {DASH_COLORS['bg_base']}; border-left: 1px solid {DASH_COLORS['border']};")
        layout = QVBoxLayout(panel)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Header for Inspector
        self._inspector_title = QLabel("NOTES")
        self._inspector_title.setStyleSheet(f"font-size: 18px; font-weight: 800; color: {DASH_COLORS['accent']};")
        layout.addWidget(self._inspector_title)
        
        # Content
        self._inspector_content = QLabel("Select an item, spell, or feature to view details.")
        self._inspector_content.setWordWrap(True)
        self._inspector_content.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self._inspector_content, 1) # Expand
        
        return panel

    def _create_item_card(self, item) -> QWidget:
        card = QFrame()
        # card.setFixedHeight(60) # Taller for details
        card.setStyleSheet(f"""
            QFrame {{
                background-color: {DASH_COLORS['bg_card']};
                border-radius: 4px;
                border: 1px solid {DASH_COLORS['border']};
            }}
            QFrame:hover {{
                border-color: {DASH_COLORS['accent']};
            }}
        """)
        
        layout = QVBoxLayout(card)
        layout.setContentsMargins(10, 8, 10, 8)
        layout.setSpacing(2)

        # Row 1: Name + Bonus
        row1 = QHBoxLayout()
        name_txt = item.name
        if item.bonuses:
             # simplistic display of magic bonus
             magic = sum(item.bonuses.values())
             if magic: name_txt += f" +{magic}"
             
        name = QLabel(name_txt)
        name.setStyleSheet("font-weight: bold; font-size: 14px; border: none; background: transparent; color: #e0e0e0;")
        row1.addWidget(name)
        row1.addStretch()
        
        # Tag (Attuned)
        if item.attuned:
             tag = QLabel("A")
             tag.setToolTip("Attuned")
             tag.setStyleSheet(f"background: {DASH_COLORS['accent']}; color: black; border-radius: 8px; padding: 2px 6px; font-weight: bold; font-size: 10px;")
             row1.addWidget(tag)

        layout.addLayout(row1)
        
        # Row 2: Notes / Damage (if any)
        if item.notes:
            notes = QLabel(item.notes)
            notes.setWordWrap(True)
            notes.setStyleSheet(f"font-size: 12px; color: {DASH_COLORS['text_dim']}; border: none; background: transparent;")
            layout.addWidget(notes)

        return card

    def _save_changes(self):
        self._store.dispatch_update(self._sheet, self._record.modifiers)

    def _on_character_updated(self, updated_record, updated_engine):
        """Unified callback whenever character state changes in the Store."""
        self._record = updated_record
        self._sheet = updated_record.sheet
        self._engine = updated_engine
        
        # In a generic single-page app, we could trigger granular UI target updates here.
        # For our MVP dashboard, we rebuild the dynamic view.
        self._refresh_ui()

        # Delete the duplicate MessageBox refresh logic. The master _refresh_ui handles this transparently now.

    def _open_editor(self):
        # Open Character Builder
        snapshot = self._modifier_snapshot
        if not snapshot:
             snapshot = ModifierStateSnapshot([], self._record.modifiers)

        dialog = CharacterBuilderDialog(self._record, snapshot, self)
        if dialog.exec() != QDialog.DialogCode.Accepted:
            return
            
        # Save changes via Store
        new_sheet, new_modifiers, new_data = dialog.get_result()
        self._modifier_snapshot = ModifierStateSnapshot(snapshot.definitions, new_modifiers)
        
        self._store.dispatch_update(new_sheet, new_modifiers, data=new_data)

    def _build_nav_bar(self) -> QWidget:
        # Replaces _build_dock
        nav = QFrame()
        nav.setFixedHeight(40)
        nav.setStyleSheet(f"background-color: {DASH_COLORS['bg_card']}; border-bottom: 1px solid {DASH_COLORS['border']};")
        
        layout = QHBoxLayout(nav)
        layout.setContentsMargins(10, 0, 10, 0)
        layout.setSpacing(10)
        
        def add_tab_btn(label, index):
            btn = QPushButton(label)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setFlat(True)
            # Add basic checkable style logic if time permits, for now simple buttons
            btn.setStyleSheet(f"""
                QPushButton {{
                    font-size: 13px; 
                    font-weight: 700; 
                    color: {DASH_COLORS['text_dim']}; 
                    border: none;
                    padding: 5px 10px;
                }}
                QPushButton:hover {{
                    color: {DASH_COLORS['accent']};
                    background-color: rgba(255, 255, 255, 0.05);
                    border-radius: 4px;
                }}
            """)
            btn.clicked.connect(lambda: self._stack.setCurrentIndex(index))
            layout.addWidget(btn)
            
        add_tab_btn("OVERVIEW", 0)
        add_tab_btn("BACKPACK", 1) # Renamed
        add_tab_btn("GRIMOIRE", 2)
        add_tab_btn("FEATURES", 3)
        add_tab_btn("NOTES", 4)
        
        layout.addStretch()
        return nav

class InventoryPage(QWidget):
    """
    Full page inventory view.
    """
    def __init__(self, record: CharacterRecord, app_context: ApplicationContext, dashboard: CharacterDashboard):
        super().__init__()
        self._record = record
        self._sheet = record.sheet
        self._app_context = app_context
        self._dashboard = dashboard # Back reference for saving
        
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # Controls
        controls = QHBoxLayout()
        
        title = QLabel("Backpack")
        title.setStyleSheet(f"font-size: 24px; font-weight: bold; color: {DASH_COLORS['text_main']};")
        controls.addWidget(title)
        
        controls.addStretch()
        
        browse_btn = QPushButton("+ Add from Ruleset")
        browse_btn.setProperty("class", "PrimaryButton")
        browse_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        browse_btn.clicked.connect(self._open_ruleset_browser)
        
        custom_btn = QPushButton("+ Create Custom")
        custom_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        custom_btn.clicked.connect(self._open_custom_dialog)
        
        controls.addWidget(browse_btn)
        controls.addWidget(custom_btn)
        
        layout.addLayout(controls)
        
        # Item List
        # Using a QScrollArea with a VBoxLayout for now to match style
        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)
        self._scroll.setFrameShape(QFrame.Shape.NoFrame)
        self._scroll.setStyleSheet("background: transparent;")
        
        self._content = QWidget()
        self._content_layout = QVBoxLayout(self._content)
        self._content_layout.setContentsMargins(0, 0, 0, 0)
        self._content_layout.setSpacing(8)
        
        self._scroll.setWidget(self._content)
        layout.addWidget(self._scroll)
        
        self.refresh()

    def refresh(self):
        # Rebuild list
        # Clear
        while self._content_layout.count():
             child = self._content_layout.takeAt(0)
             if child.widget(): child.widget().deleteLater()
             
        for item in self._sheet.equipment:
            card = self._create_item_row(item)
            self._content_layout.addWidget(card)
            
        self._content_layout.addStretch()

    def _create_item_row(self, item: EquipmentItem) -> QWidget:
        row = QFrame()
        row.setStyleSheet(f"""
            QFrame {{
                background-color: {DASH_COLORS['bg_card']};
                border-radius: 6px;
                border: 1px solid {DASH_COLORS['border']};
            }}
            QFrame:hover {{
                border-color: {DASH_COLORS['accent']};
            }}
        """)
        row.setFixedHeight(40)
        l = QHBoxLayout(row)
        l.setContentsMargins(10, 2, 10, 2)
        
        # Icon/Type indicator?
        
        name_txt = item.name
        if item.attuned: name_txt += " [A]"
        name = QLabel(name_txt)
        name.setStyleSheet("font-weight: bold; font-size: 13px; border: none; background: transparent;")
        l.addWidget(name)
        
        l.addStretch()
        
        qty = QLabel(f"x{item.quantity}")
        qty.setStyleSheet(f"color: {DASH_COLORS['text_dim']}; border: none; background: transparent;")
        l.addWidget(qty)
        
        l.addSpacing(20)
        
        equip_btn = QPushButton("Unequip" if item.equipped else "Equip")
        equip_style = f"""
            QPushButton {{
                background-color: {DASH_COLORS['accent'] if item.equipped else 'transparent'};
                border: 1px solid {DASH_COLORS['accent']};
                color: {'white' if item.equipped else DASH_COLORS['accent']};
                border-radius: 4px;
                padding: 2px 8px;
                font-weight: 600;
            }}
            QPushButton:hover {{
                background-color: {DASH_COLORS['accent']};
                color: white;
            }}
        """
        equip_btn.setStyleSheet(equip_style)
        equip_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        equip_btn.clicked.connect(lambda _, i=item: self._toggle_equip(i))
        l.addWidget(equip_btn)
        
        # Remove/Delete?
        
        return row

    def _toggle_equip(self, item):
        item.equipped = not item.equipped
        self._dashboard._save_changes()
        self.refresh()
        self._dashboard._refresh_overview()

    def _open_ruleset_browser(self):
        # Open EquipmentWindow
        self._eq_window = EquipmentWindow(parent=self.window(), selection_mode=True)
        self._eq_window.setWindowFlags(Qt.WindowType.Window)
        self._eq_window.setWindowModality(Qt.WindowModality.ApplicationModal)
        self._eq_window.items_selected.connect(self._on_items_added)
        self._eq_window.show()

    def _open_custom_dialog(self):
        dialog = EquipmentEntryDialog(parent=self.window())
        if dialog.exec() == QDialog.DialogCode.Accepted:
             item = dialog.get_item()
             if item.name:
                 self._on_items_added([(dict(name=item.name, weight=item.weight_lb, cost=item.cost, rarity=item.rarity), item.quantity)]) 
                 # Wait, logic mismatch. _on_items_added expects list of tuples. 
                 # Should adapt. 
                 self._add_to_sheet([item])

    def _on_items_added(self, items_data):
        new_items = []
        for data, qty in items_data:
             entry = EquipmentItem(
                name=str(data.get("name", "New Item")),
                quantity=max(1, qty),
                weight_lb=float(data.get("weight", 0.0) or 0.0),
                attuned=bool(data.get("attunement", False)),
                equipped=False,
                compendium_id=str(data.get("id", "")),
                rarity=str(data.get("rarity", "")),
            )
             new_items.append(entry)
        self._add_to_sheet(new_items)

    def _add_to_sheet(self, items):
        self._sheet.equipment.extend(items)
        self._dashboard._save_changes()
        self.refresh()

class FeaturesPage(QWidget):
    """
    Displays ASI choices, Feats, and active Traits from Origin/Classes.
    """
    def __init__(self, record: CharacterRecord, app_context: ApplicationContext, dashboard: CharacterDashboard):
        super().__init__()
        self._record = record
        self._sheet = record.sheet
        self._app_context = app_context
        self._dashboard = dashboard
        
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # Controls / Title
        title = QLabel("Features & Traits")
        title.setStyleSheet(f"font-size: 24px; font-weight: bold; color: {DASH_COLORS['text_main']};")
        layout.addWidget(title)
        
        # Scroll Area for Features
        self._scroll = QScrollArea()
        self._scroll.setWidgetResizable(True)
        self._scroll.setFrameShape(QFrame.Shape.NoFrame)
        self._scroll.setStyleSheet("background: transparent;")
        
        self._content = QWidget()
        self._content_layout = QVBoxLayout(self._content)
        self._content_layout.setContentsMargins(0, 0, 0, 0)
        self._content_layout.setSpacing(8)
        
        self._scroll.setWidget(self._content)
        layout.addWidget(self._scroll)
        
        self.refresh()

    def refresh(self):
        # Clear existing
        while self._content_layout.count():
             child = self._content_layout.takeAt(0)
             if child.widget(): child.widget().deleteLater()
             
        # Add sections: Active Feats, ASI Choices, Racial Traits, Class Features
        features: list[dict] = []
        
        # Gather ASI selections
        import re
        for key, val in self._sheet.feature_options.items():
            if not val:
                continue
            if "_asi_" in key and val.startswith("ASI:"):
                level_match = re.search(r'_asi_(\d+)$', key)
                lvl = level_match.group(1) if level_match else "?"
                features.append({
                    "name": f"Ability Score Improvement (Level {lvl})",
                    "source": "ASI",
                    "description": val
                })
            elif ("_feat" in key or "_asi" in key) and not val.startswith("ASI:"):
                # Exclude if the key is an origin feat (handled below) or an attribute sub-choice
                if key.startswith("origin_feat_") or val in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
                    continue
                    
                features.append({
                    "name": val,
                    "source": "Feat",
                    "description": "Selected Feat"
                })
        
        # Origin features (Background / Species)
        origin_feats = []
        compendium = self._app_context.ensure_compendium()
        
        def build_feature_dict(tf: dict, source: str) -> dict:
            name = tf.get("name", "Unknown")
            desc = tf.get("description", "")
            
            # Check if this feature has any saved options in the sheet
            feat_name_lower = name.lower().replace(' ', '_')
            base_key = f"origin_feat_{feat_name_lower}"
            
            # Collect any choices made for this trait
            choices_made = []
            for k, v in self._sheet.feature_options.items():
                if k.startswith(base_key) and v:
                    if k == base_key:
                        # Root choice for this feature
                        choices_made.append(f"Choice: {v}")
                    else:
                        # Sub-choice (e.g. skills, attributes)
                        opt_name = k.replace(f"{base_key}_", "").replace("_", " ").title()
                        choices_made.append(f"{opt_name}: {v}")
                    
            if choices_made:
                desc = desc + "\n\n**Selected:**\n" + "\n".join(f"- {c}" for c in choices_made)
                
            return {
                "name": name,
                "source": source,
                "description": desc
            }
        
        if compendium:
            sp_name = self._sheet.identity.ancestry
            sp_record = next((s for s in compendium.records("species") if isinstance(s, dict) and str(s.get("name", "")).lower() == str(sp_name).lower()), None)
            if sp_record:
                # Species Ability Score Increase Choices
                sp_key = sp_name.lower().replace(' ', '_')
                ability_choices = []
                for k, v in self._sheet.feature_options.items():
                    if k.startswith(f"{sp_key}_ability_") and v:
                        ability_choices.append(v)
                if ability_choices:
                    features.append({
                        "name": "Ability Score Increase",
                        "source": f"Species ({sp_name})",
                        "description": "Selected Attributes: " + ", ".join(ability_choices)
                    })
                    
                for tf in sp_record.get("features", []):
                    features.append(build_feature_dict(tf, f"Species ({sp_name})"))
                            
            bg_name = self._sheet.identity.background
            bg_record = next((b for b in compendium.records("backgrounds") if isinstance(b, dict) and str(b.get("name", "")).lower() == str(bg_name).lower()), None)
            if bg_record:
                 bg_ability_choices = []
                 for k, v in self._sheet.feature_options.items():
                     if k.startswith("background_ability_") and v:
                         bg_ability_choices.append(v)
                 if bg_ability_choices:
                     features.append({
                         "name": "Ability Score Increase",
                         "source": f"Background ({bg_name})",
                         "description": "Selected Attributes: " + ", ".join(bg_ability_choices)
                     })
                     
                 bg_feat = bg_record.get("starting_feat")
                 if bg_feat:
                     feat_key_base = bg_feat.lower().replace(' ', '_')
                     choices_made = []
                     for k, v in self._sheet.feature_options.items():
                         if k.startswith(feat_key_base) and v:
                             opt_name = k.replace(f"{feat_key_base}_", "").replace("_", " ").title()
                             choices_made.append(f"{opt_name}: {v}")
                     
                     desc = "Starting Feat"
                     if choices_made:
                         desc += "\n\n**Selected:**\n" + "\n".join(f"- {c}" for c in choices_made)
                         
                     features.append({
                         "name": bg_feat,
                         "source": f"Background ({bg_name})",
                         "description": desc
                     })
                     
        # Class features are harder without pulling full compendium class data for the current level.
        # Could add class traits here if we loop over them.
        
        # Populate
        for f in features:
            card = self._create_feature_card(f)
            self._content_layout.addWidget(card)
            
        self._content_layout.addStretch()

    def _create_feature_card(self, f: dict) -> QWidget:
        card = QFrame()
        card.setStyleSheet(f"""
            QFrame {{
                background-color: {DASH_COLORS['bg_card']};
                border-radius: 6px;
                border: 1px solid {DASH_COLORS['border']};
            }}
        """)
        l = QVBoxLayout(card)
        l.setContentsMargins(12, 12, 12, 12)
        
        row1 = QHBoxLayout()
        name = QLabel(f["name"])
        name.setStyleSheet(f"font-weight: bold; font-size: 15px; color: {DASH_COLORS['text_main']};")
        row1.addWidget(name)
        
        row1.addStretch()
        
        source = QLabel(f["source"])
        source.setStyleSheet(f"font-size: 11px; font-weight: bold; color: {DASH_COLORS['accent']}; text-transform: uppercase;")
        row1.addWidget(source)
        
        l.addLayout(row1)
        
        if f.get("description"):
            desc = QLabel(f["description"])
            desc.setWordWrap(True)
            desc.setStyleSheet(f"font-size: 13px; color: {DASH_COLORS['text_dim']}; margin-top: 4px;")
            l.addWidget(desc)
            
        return card





