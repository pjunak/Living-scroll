"""
Main container for the redesign Character Builder experience.
Migrating from SpellcastingSettingsDialog to a split Creation/Leveling tab approach.
"""

from __future__ import annotations

import copy
from typing import Optional, Tuple

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QTabWidget,
    QWidget,
)

from modules.character_sheet.model import CharacterSheet
from modules.character_sheet.model.schema import CharacterData
from modules.character_sheet.services.library import CharacterRecord
from modules.character_sheet.services.rules_engine import RulesEngine
from modules.compendium.service import Compendium
from modules.compendium.modifiers.state import ModifierStateSnapshot
from modules.character_sheet.ui.builder.tabs.creation import CreationTab
from modules.character_sheet.ui.builder.tabs.leveling import LevelingTab


class CharacterBuilderDialog(QDialog):
    """
    The new Character Builder.
    Tabs:
      1. Creation: Base identity, species, class (level 1), background, initial stats.
      2. Leveling: Post-creation progression management (1-20).
    """

    def __init__(
        self,
        record: CharacterRecord,
        modifier_snapshot: ModifierStateSnapshot | None,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.setWindowTitle("Character Builder")
        self.resize(1024, 768)

        self._record = record
        
        # Initialize Compendium & Engine
        self._compendium = Compendium.load()
        self._engine = RulesEngine(self._compendium)
        
        # Resolve 'Source of Truth'
        if record.data:
            self._data = copy.deepcopy(record.data)
            # Hydrate to get working sheet
            self._sheet = self._engine.hydrate(self._data)
        else:
            # New Character (or strictly fresh start)
            self._data = CharacterData()
            self._sheet = self._engine.hydrate(self._data)
            
        self._modifier_snapshot = modifier_snapshot or ModifierStateSnapshot([], {})
        
        # Layout
        layout = QVBoxLayout(self)
        self.tabs = QTabWidget()
        layout.addWidget(self.tabs)

        # 1. Creation Tab
        self.creation_tab = CreationTab(self._sheet, self._modifier_snapshot, self._data, parent=self)
        self.tabs.addTab(self.creation_tab, "Creation")

        # 2. Leveling Tab
        self.leveling_tab = LevelingTab(
            self._sheet, 
            self._modifier_snapshot, 
            data=self._data,
            engine=self._engine,
            parent=self
        )
        self.tabs.addTab(self.leveling_tab, "Leveling")

        # Connect signals for cross-tab updates?
        # e.g., if Name changes in Creation, title might change.
        # e.g., if Class changes in Creation, Leveling tab needs rebuild.
        self.creation_tab.dataChanged.connect(self._on_creation_data_changed)

        # Dialog Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Cancel | QDialogButtonBox.StandardButton.Ok)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    def _on_creation_data_changed(self):
        """Called when base creation data (Identity, Class Lvl 1) changes."""
        # Signal Leveling tab to refresh its base assumptions
        self.leveling_tab.refresh_from_sheet()

    def get_result(self) -> Tuple[CharacterSheet, dict, CharacterData]:
        """Return the modified sheet, modifier states, and Source Data."""
        # Finalize data from tabs if needed
        # We should ensure self._data is updated from UI state if UI acts on Sheet
        
        # TEMP: Since we haven't fully refactored tabs to write to _data yet,
        # we might have a drift. But we are refactoring LevelingTab next.
        return self._sheet, self._modifier_snapshot.states, self._data
