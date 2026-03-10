from __future__ import annotations

from typing import Mapping
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel,
    QGroupBox, QScrollArea, QFrame
)

from modules.character_sheet.model import CharacterSheet
from modules.compendium.service import Compendium
from modules.compendium.modifiers.state import ModifierStateSnapshot
from modules.character_sheet.ui.builder.widgets.level_entry import LevelEntry

class OriginTab(QWidget):
    """
    Handles Background (Origin) Selection and Origin-specific dynamic traits
    like Origin Feats, Tools, and Languages.
    """
    dataChanged = Signal()

    def __init__(
        self,
        sheet: CharacterSheet,
        modifier_snapshot: ModifierStateSnapshot,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self._sheet = sheet
        self._modifier_snapshot = modifier_snapshot
        self._selections = dict(sheet.feature_options)
        self._compendium = Compendium.load()
        
        self._bg_combo: QComboBox | None = None
        self._bg_entry: LevelEntry | None = None
        
        self._layout_ui()
        self._load_data()

    def _layout_ui(self):
        layout = QVBoxLayout(self)
        
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        content = QWidget()
        self.form_layout = QVBoxLayout(content)
        self.form_layout.setSpacing(20)
        
        # 1. Background Selection Group
        self.form_layout.addWidget(self._build_background_section())
        
        # 2. Origin Features Container
        self._features_container = QVBoxLayout()
        self.form_layout.addLayout(self._features_container)
        
        self.form_layout.addStretch()
        scroll.setWidget(content)
        layout.addWidget(scroll)

    def _build_background_section(self) -> QWidget:
        group = QGroupBox("Origin Background")
        layout = QHBoxLayout(group)
        
        layout.addWidget(QLabel("Background:"))
        
        self._bg_combo = QComboBox()
        self._bg_combo.setMinimumWidth(200)
        self._bg_combo.addItem("(Select Background)", "")
        self._bg_combo.currentIndexChanged.connect(self._on_background_changed)
        layout.addWidget(self._bg_combo)
        layout.addStretch()
        
        return group

    def _load_data(self):
        bg_records = [r for r in self._compendium.records("backgrounds") if isinstance(r, Mapping)]
        sorted_bg = sorted(bg_records, key=lambda x: str(x.get("name", "")))
        for r in sorted_bg:
            self._bg_combo.addItem(str(r.get("name")), r)
            
        current_bg = self._sheet.identity.background
        if current_bg:
            idx = self._bg_combo.findText(current_bg)
            if idx >= 0:
                self._bg_combo.setCurrentIndex(idx)
        
        self._refresh_features()

    def _on_background_changed(self):
        txt = self._bg_combo.currentText()
        if txt == "(Select Background)":
            self._sheet.identity.background = ""
        else:
            self._sheet.identity.background = txt
            
        self._refresh_features()
        self.dataChanged.emit()

    def _refresh_features(self):
        if self._bg_entry:
            self._bg_entry.setParent(None)
            self._bg_entry.deleteLater()
            self._bg_entry = None
            
        bg_name = self._sheet.identity.background
        if not bg_name:
            return
            
        bg_record = next((b for b in self._compendium.records("backgrounds") if isinstance(b, dict) and str(b.get("name", "")).lower() == str(bg_name).lower()), None)
        if not bg_record:
            return
            
        bg_features = []
        feat_name = bg_record.get("starting_feat")
        if feat_name:
            bg_features.append({"name": f"Origin Feat ({feat_name})", "source": "Background"})
            
        def process_ability_bonus(record, source_name, entry_widget):
            abo = record.get("ability_bonus_options")
            if abo and isinstance(abo, dict):
                choose = abo.get("choose", 0)
                amount = abo.get("amount", 1)
                allowed = abo.get("abilities", [])
                if choose > 0 and allowed:
                    from modules.character_sheet.ui.builder.utils.selection_helpers import get_available_attributes, SKILL_DROPDOWN_WIDTH
                    for i in range(choose):
                        opt_key = f"{source_name.lower().replace(' ', '_')}_ability_{i}"
                        current_attr = self._selections.get(opt_key, "")
                        options = get_available_attributes(
                            self._sheet, 
                            max_score=20, 
                            pending_selections=self._selections,
                            compendium=self._compendium
                        )
                        if "any" not in [a.lower() for a in allowed]:
                            options = [o for o in options if o.upper() in allowed]
                            
                        entry_widget.add_dynamic_option(
                            label=f"Ability Increase (+{amount})",
                            options=options,
                            current=current_attr,
                            key=opt_key,
                            width=SKILL_DROPDOWN_WIDTH,
                            group_id=source_name.lower().replace(' ', '_')
                        )
            
        self._bg_entry = LevelEntry(
            level=0,
            class_name="Origin (Background)",
            features=bg_features,
            parent=self
        )
        self._bg_entry._header.setText(f"Origin Background: {bg_name}")
        self._bg_entry._remove_btn.hide()
        
        # Populate dynamic options (Origin Feats)
        self._populate_feat_options(feat_name, self._bg_entry, "background_feat")
        
        # Populate Attributes
        process_ability_bonus(bg_record, "background", self._bg_entry)
        
        self._bg_entry.choiceChanged.connect(self._on_choice_changed)
        self._features_container.addWidget(self._bg_entry)

    def _populate_feat_options(self, feat_name: str | None, entry_widget: LevelEntry, feat_key: str):
        if not feat_name:
            return
            
        resolved_feat = next((f for f in self._compendium.records("feats") if isinstance(f, dict) and str(f.get("name", "")).lower() == feat_name.lower()), None)
        if not resolved_feat:
            # Fallback for magic initiate
            options = []
            if feat_name.lower() == "magic initiate":
                options = ["Magic Initiate (Cleric)", "Magic Initiate (Druid)", "Magic Initiate (Wizard)"]
                
                class OptionWrapper:
                    def __init__(self, l, v):
                        self.label = l
                        self.value = v
                        
                wrapped_options = [OptionWrapper(o, o) for o in options]
                current_val = self._selections.get(feat_key, "")
                entry_widget.add_dynamic_option(
                    label=f"Choose {feat_name} Variant",
                    options=wrapped_options,
                    current=current_val,
                    key=feat_key,
                    group_id="background_origin_feat"
                )
            return
            
        from modules.character_sheet.ui.builder.utils.selection_helpers import (
            get_available_skill_proficiencies,
            get_available_skill_expertises,
            get_available_attributes,
            get_available_tool_proficiencies,
            SKILL_DROPDOWN_WIDTH
        )
        
        feat_key_base = f"{feat_name.lower().replace(' ', '_')}"
        
        # Attribute increase options
        attr_increase = resolved_feat.get("attribute_increase")
        if attr_increase and isinstance(attr_increase, list):
            attr_key = f"{feat_key_base}_attribute"
            available_attrs = get_available_attributes(
                self._sheet, 
                max_score=20, 
                pending_selections=self._selections,
                compendium=self._compendium
            )
            
            if "any" in [a.lower() for a in attr_increase]:
                options = available_attrs
            else:
                options = [a for a in attr_increase if a.upper() in available_attrs]
            
            increase_amount = 1 
            for i in range(increase_amount):
                opt_key = f"{attr_key}_{i}"
                current_selection = self._selections.get(opt_key, "")
                
                entry_widget.add_dynamic_option(
                    label=f"Choose Attribute (+1)",
                    options=options,
                    current=current_selection,
                    key=opt_key,
                    width=SKILL_DROPDOWN_WIDTH,
                    group_id=feat_key
                )
        
        proficiency = resolved_feat.get("proficiency")
        if proficiency and isinstance(proficiency, dict):
            skills = proficiency.get("skills", [])
            if skills:
                skill_key = f"{feat_key_base}_skill_proficiency"
                current_skill = self._selections.get(skill_key, "")
                available_skills = get_available_skill_proficiencies(self._sheet, self._selections)
                
                if skills == ["any"] or "any" in skills:
                    options = available_skills
                else:
                    options = [opt for opt in available_skills if opt.value in skills]
                
                if options:
                    entry_widget.add_dynamic_option(
                        label="Choose Skill Proficiency",
                        options=options,
                        current=current_skill,
                        key=skill_key,
                        width=SKILL_DROPDOWN_WIDTH,
                        group_id=feat_key
                    )
                    
            tools = proficiency.get("tools", [])
            if tools:
                tool_key = f"{feat_key_base}_tool_proficiency"
                current_tool = self._selections.get(tool_key, "")
                available_tools = get_available_tool_proficiencies(self._sheet, self._selections)
                
                if tools == ["any"] or "any" in tools:
                    options = available_tools
                else:
                    options = [t for t in tools if t in available_tools]
                
                if options:
                    entry_widget.add_dynamic_option(
                        label="Choose Tool Proficiency",
                        options=options,
                        current=current_tool,
                        key=tool_key,
                        width=SKILL_DROPDOWN_WIDTH,
                        group_id=feat_key
                    )
                    
        options = resolved_feat.get("options", [])
        if options:
            opt_key = f"{feat_key_base}_choice"
            current_val = self._selections.get(opt_key, "")
            
            class OptionWrapper:
                def __init__(self, l, v):
                    self.label = l
                    self.value = v
                    
            wrapped_options = []
            for o in options:
                if isinstance(o, dict):
                    wrapped_options.append(OptionWrapper(o.get("name", ""), o.get("name", "")))
                else:
                    wrapped_options.append(OptionWrapper(str(o), str(o)))
                    
            if wrapped_options:
                entry_widget.add_dynamic_option(
                    label=f"Choose {feat_name} Option",
                    options=wrapped_options,
                    current=current_val,
                    key=opt_key,
                    width=200,
                    group_id=feat_key
                )

    def _on_choice_changed(self, key: str, value: str):
        if value:
            self._selections[key] = value
            self._sheet.feature_options[key] = value
        else:
            self._selections.pop(key, None)
            self._sheet.feature_options.pop(key, None)
        self.dataChanged.emit()
