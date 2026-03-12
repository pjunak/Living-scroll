import sys
from PySide6.QtWidgets import QApplication
from modules.character_sheet.model.model import CharacterSheet
from modules.character_sheet.ui.builder.tabs.creation import CreationTab
from modules.character_sheet.ui.builder.tabs.leveling import LevelingTab
from modules.compendium.modifiers.state import ModifierStateSnapshot
from typing import Mapping

def main():
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    
    sheet = CharacterSheet()
    modifier_snapshot = ModifierStateSnapshot()
    
    # Needs to be tested with leveling tab
    creation = CreationTab(sheet, modifier_snapshot)
    leveling = LevelingTab(sheet, modifier_snapshot)

    # Let's mock the main window signal
    def on_data_changed():
        leveling.refresh_from_sheet()
        
    creation.dataChanged.connect(on_data_changed)

    # Trigger species change to Elf
    idx = creation._species_combo.findText("Elf")
    if idx >= 0:
        print(f"Selecting Elf at index {idx}")
        creation._species_combo.setCurrentIndex(idx)
        print("Done setting species.")
    else:
        print("Elf not found.")
        
    # Check if lineage dropdown exists
    has_dropdown = any(isinstance(k, str) and 'lineage' in getattr(leveling, "_dynamic_widgets", {}).keys() for k in getattr(leveling, "_dynamic_widgets", {}))
    print(getattr(leveling, "_dynamic_widgets", {}))
    print(f"Has Dropdown: {has_dropdown}")

if __name__ == "__main__":
    main()
