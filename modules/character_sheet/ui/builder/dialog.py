"""
Main container for the redesign Character Builder experience.
Migrating from SpellcastingSettingsDialog to a split Creation/Leveling tab approach.
"""

from __future__ import annotations

import copy
from typing import Optional, Tuple, List

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QTabWidget,
    QWidget,
)

from modules.character_sheet.model import CharacterSheet
from modules.compendium.service import Compendium
from modules.compendium.modifiers.state import ModifierStateSnapshot
from modules.character_sheet.ui.builder.tabs.creation import CreationTab
from modules.character_sheet.ui.builder.tabs.leveling import LevelingTab
from modules.character_sheet.ui.builder.tabs.species import SpeciesTab
from modules.character_sheet.ui.builder.tabs.origin import OriginTab
from modules.character_sheet.ui.builder.tabs.management import (
    collect_management_entries,
    ManagementEntryTab,
)


class CharacterBuilderDialog(QDialog):
    """
    The new Character Builder.
    Tabs:
      1. Identity          – Base identity & stats
      2. Species           – Species traits
      3. Origin            – Background selection
      4. Class             – Level-by-level progression
      5+. <dynamic>        – One tab per management entry (Spellbook, Prepared, …)
    """

    # Number of fixed (non-management) tabs
    _FIXED_TAB_COUNT = 4

    def __init__(
        self,
        record, # Expecting CharacterRecord
        modifier_snapshot: ModifierStateSnapshot | None,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.setWindowTitle("Character Builder")
        self.resize(1024, 768)

        # Working copies
        self._sheet = copy.deepcopy(record.sheet)
        self._modifier_snapshot = modifier_snapshot or ModifierStateSnapshot([], {})
        
        # Original Data structure (Decisions)
        from modules.character_sheet.model.schema import CharacterData
        self._record_data = copy.deepcopy(record.data) if getattr(record, 'data', None) else CharacterData()

        self._compendium = Compendium.load()
        
        # Layout
        layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # 1. Identity & Stats
        self.creation_tab = CreationTab(self._sheet, self._modifier_snapshot, parent=self)
        self.tabs.addTab(self.creation_tab, "Identity")

        # 2. Species Tab
        self.species_tab = SpeciesTab(self._sheet, self._modifier_snapshot, parent=self)
        self.tabs.addTab(self.species_tab, "Species")

        # 3. Origin Tab
        self.origin_tab = OriginTab(self._sheet, self._modifier_snapshot, parent=self)
        self.tabs.addTab(self.origin_tab, "Origin")

        # 4. Class Tab
        self.leveling_tab = LevelingTab(self._sheet, self._modifier_snapshot, parent=self)
        self.tabs.addTab(self.leveling_tab, "Class")

        # 5+. Dynamic management tabs (one per entry)
        self._management_tabs: List[ManagementEntryTab] = []
        self._refresh_management_tabs()

        # Connect signals for cross-tab updates
        self.creation_tab.dataChanged.connect(self._on_creation_data_changed)

        # Dialog Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    # ── Dynamic management tabs ───────────────────────────────────

    def _refresh_management_tabs(self) -> None:
        """Remove old management tabs and create new ones from class data."""
        # Remove existing management tabs (everything after the fixed tabs)
        for tab in self._management_tabs:
            idx = self.tabs.indexOf(tab)
            if idx >= 0:
                self.tabs.removeTab(idx)
            tab.deleteLater()
        self._management_tabs.clear()

        # Collect entries from all classes
        entries = collect_management_entries(self._sheet, self._compendium)
        for entry in entries:
            tab = ManagementEntryTab(
                entry=entry,
                sheet=self._sheet,
                data=self._record_data,
                compendium=self._compendium,
                parent=self,
            )
            tab.dataChanged.connect(self._on_management_data_changed)
            self._management_tabs.append(tab)
            self.tabs.addTab(tab, entry["_tab_label"])

    def _on_management_data_changed(self) -> None:
        """Called when any management tab changes its state."""
        pass  # Data is already persisted in CharacterData by the tab

    def _on_creation_data_changed(self):
        """Called when base creation data (Identity, Class Lvl 1) changes."""
        self.leveling_tab.refresh_from_sheet()
        self._refresh_management_tabs()

    def get_result(self) -> Tuple[CharacterSheet, dict, 'CharacterData']:
        """Return the modified sheet, modifier states, and the authoritative decisions (data)."""
        from modules.character_sheet.model.schema import ClassLevelData
        from modules.character_sheet.model import ABILITY_NAMES
        
        # Reconstruct CharacterData from the mutated CharacterSheet.
        self._record_data.identity.name = self._sheet.identity.name
        self._record_data.identity.ancestry = self._sheet.identity.ancestry
        self._record_data.identity.ancestry_subtype = getattr(self._sheet.identity, 'ancestry_subtype', "")
        self._record_data.identity.background = self._sheet.identity.background
        self._record_data.identity.alignment = self._sheet.identity.alignment
        self._record_data.identity.player_name = getattr(self._sheet.identity, 'player', "")
        self._record_data.identity.portrait_path = self._sheet.identity.portrait_path
        
        # Base stats (from pure scores)
        self._record_data.base_stats = {abil: self._sheet.get_ability(abil).score for abil in ABILITY_NAMES}
        
        # Classes
        self._record_data.classes = []
        for c in self._sheet.identity.classes:
            self._record_data.classes.append(ClassLevelData(class_name=c.name, level=c.level, subclass=c.subclass))
        
        return self._sheet, self._modifier_snapshot.states, self._record_data

