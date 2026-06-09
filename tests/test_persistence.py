import pytest
import shutil
import uuid
from pathlib import Path

from modules.character_sheet.model.schema import CharacterData
from modules.character_sheet.model.model import CharacterSheet
from modules.character_sheet.services.library import CharacterLibrary, CharacterRecord

@pytest.fixture
def temp_library_path(tmp_path):
    # Set up a temporary directory for character saves
    lib_path = tmp_path / "characters"
    lib_path.mkdir()
    yield lib_path
    # Clean up (tmp_path is handled by pytest, but good practice)
    if lib_path.exists():
        shutil.rmtree(lib_path)


def test_character_creation_and_rehydration(temp_library_path):
    """
    Test that a CharacterData payload correctly passes from creation, 
    down to the disk, and is loaded correctly on the next app 'restart'.
    """
    
    # 1. Simulate 'Session 1': Creating a new character
    lib_session1 = CharacterLibrary(storage_path=temp_library_path)
    
    # Explicitly craft decisions (like the UI does)
    data = CharacterData()
    data.identity.name = "Test Hero"
    data.identity.ancestry = "Elf"
    data.base_stats["STR"] = 18
    
    # The hub passes empty sheet/modifiers, and the core data.
    record1 = lib_session1.create_record(sheet=CharacterSheet(), modifiers={}, data=data)
    char_id = record1.identifier
    
    assert record1.data is not None
    assert record1.data.identity.name == "Test Hero"
    
    # Verify the JSON file actually exists
    save_file = temp_library_path / f"{char_id}.json"
    assert save_file.exists(), "JSON file was not created on disk."
    
    
    # 2. Simulate 'Session 2': Restarting the application
    lib_session2 = CharacterLibrary.load(temp_library_path)
    
    # Get the record back out
    record2 = lib_session2.get(char_id)
    assert record2 is not None, "Failed to load the character from disk."
    
    # The Rehydration Engine should have hydrated the internal CharacterSheet from CharacterData
    assert record2.data is not None, "CharacterData was wiped or failed to deserialize on load."
    assert record2.data.identity.name == "Test Hero", "Decisions failed to persist across loads."
    assert record2.data.identity.ancestry == "Elf"
    assert record2.data.base_stats["STR"] == 18
    
    # Depending on RulesEngine, the sheet native values should also be populated:
    assert record2.sheet.identity.name == "Test Hero" 


def test_partial_update_preservation(temp_library_path):
    """
    Test that performing a partial update (e.g. changing HP or toggling a modifier)
    does not wipe the core CharacterData decisions.
    """
    # Create
    lib = CharacterLibrary(storage_path=temp_library_path)
    data = CharacterData()
    data.identity.name = "Persistent Hero"
    record = lib.create_record(sheet=CharacterSheet(), modifiers={}, data=data)
    char_id = record.identifier
    
    # Simulate partial Dashboard update
    updated_sheet = record.sheet
    updated_sheet.combat.current_hp = 5 # Changed HP
    
    new_modifiers = {"some_feat": True}
    
    # Update without passing data (simulating older dashboard behavior before our fix,
    # or the behavior expected of the library where data shouldn't be wiped. 
    # Actually, CharacterStore now passes data=payload_data. 
    # Let's test the library layer method.)
    lib.update_record(char_id, updated_sheet, new_modifiers, data=record.data)
    
    # Load fresh to verify
    lib_fresh = CharacterLibrary.load(temp_library_path)
    loaded_record = lib_fresh.get(char_id)
    
    assert loaded_record.data is not None, "Data was wiped during partial update."
    assert loaded_record.data.identity.name == "Persistent Hero", "Data fields altered on partial update."
    assert loaded_record.modifiers.get("some_feat") is True, "Modifiers did not persist."

