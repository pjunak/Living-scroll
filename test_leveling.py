import sys
from PySide6.QtWidgets import QApplication
from modules.character_sheet.model.model import CharacterSheet
from modules.character_sheet.ui.builder.tabs.creation import CreationTab
from modules.character_sheet.ui.builder.tabs.leveling import LevelingTab
from modules.compendium.modifiers.state import ModifierStateSnapshot

def main():
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)
    
    sheet = CharacterSheet()
    modifier_snapshot = ModifierStateSnapshot()
    
    creation = CreationTab(sheet, modifier_snapshot)
    leveling = LevelingTab(sheet, modifier_snapshot)

    def on_data_changed():
        print("Data changed, refreshing leveling tab...")
        try:
            leveling.refresh_from_sheet()
            print("Refresh successful.")
        except Exception as e:
            import traceback
            traceback.print_exc()

    creation.dataChanged.connect(on_data_changed)

    idx = creation._species_combo.findText("Elf")
    if idx >= 0:
        print(f"Selecting Elf at index {idx}")
        creation._species_combo.setCurrentIndex(idx)
        print("Done setting species.")
    else:
        print("Elf not found.")
        
    print(getattr(leveling, "_dynamic_widgets", {}))

if __name__ == "__main__":
    main()
