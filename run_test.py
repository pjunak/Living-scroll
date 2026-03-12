from modules.character_sheet.model.model import (
    AbilityBlock,
    CharacterIdentity,
    ClassProgression,
    SpellcastingData,
    CharacterSheet,
    character_sheet_to_dict,
    character_sheet_from_dict
)
import sys

def main():
    print("Testing Pydantic instantiation...")
    sheet = CharacterSheet()
    sheet.identity.name = "Test Hero"
    sheet.abilities["STR"].score = 18
    sheet.identity.classes.append(ClassProgression(name="Rogue", level=5))
    
    print("Testing serialization...")
    data = character_sheet_to_dict(sheet)
    print(f"Serialized name: {data['identity']['name']}")
    print(f"Serialized STR: {data['abilities']['STR']['score']}")
    
    print("Testing deserialization...")
    loaded = character_sheet_from_dict(data)
    print(f"Loaded name: {loaded.identity.name}")
    print(f"Loaded STR: {loaded.abilities['STR'].score}")
    print(f"Loaded class: {loaded.identity.classes[0].name}")
    print("Success!")
    sys.exit(0)

if __name__ == "__main__":
    main()
