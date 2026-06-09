import pytest
from unittest.mock import MagicMock, patch
from pathlib import Path
from modules.compendium.service import Compendium
from modules.compendium.loader import CompendiumLoader

@pytest.fixture
def compendium():
    sample_payload = {
        "spells": [{
            "id": "spell:fireball",
            "name": "Fireball",
            "type": "spell",
            "level": 3,
            "school": "Evocation"
        }],
        "classes": [{
            "id": "class:wizard",
            "name": "Wizard",
            "type": "class",
            "hit_die": "d6"
        }],
        "equipment": [{
            "id": "item:sword",
            "name": "Sword",
            "type": "item",
            "cost": "10gp"
        }]
    }
    return Compendium(sample_payload)

# TestCompendium
def test_record_by_id(compendium):
    # Direct hit
    rec = compendium.record_by_id("spell:fireball")
    assert rec is not None
    assert rec["name"] == "Fireball"

    # Miss
    rec = compendium.record_by_id("spell:nada")
    assert rec is None

def test_filter_by_type(compendium):
    # Use public API records()
    spells = compendium.records("spells")
    assert len(spells) == 1
    assert spells[0]["name"] == "Fireball"

    items = compendium.records("equipment")
    assert len(items) == 1
    assert items[0]["name"] == "Sword"

def test_filter_by_custom_predicate(compendium):
    # Manual filter on records
    all_spells = compendium.records("spells")
    results = [s for s in all_spells if s.get("name", "").startswith("F")]
    assert len(results) == 1
    assert results[0]["name"] == "Fireball"


# TestCompendiumLoader
@pytest.fixture
def compendium_loader():
    mock_root = MagicMock(spec=Path)
    loader = CompendiumLoader(mock_root)
    return loader, mock_root

@patch("modules.compendium.loader.CompendiumLoader._load_module")
def test_load_merges_modules(mock_load_module, compendium_loader):
    loader, mock_root = compendium_loader
    # Setup mocks
    ruleset_path = MagicMock(spec=Path)
    mock_root.__truediv__.return_value = ruleset_path
    ruleset_path.exists.return_value = True
    
    # Mock module directories
    mod1 = MagicMock(spec=Path)
    mod1.is_dir.return_value = True
    mod1.name = "core"
    mod1.__lt__ = lambda s, o: s.name < o.name
    
    mod2 = MagicMock(spec=Path)
    mod2.is_dir.return_value = True
    mod2.name = "expansion"
    mod2.__lt__ = lambda s, o: s.name < o.name

    ruleset_path.iterdir.return_value = [mod1, mod2]
    
    # Mock module payloads
    mock_load_module.side_effect = [
        {"spells": [{"id": "s1", "name": "Spell 1"}]},
        {"spells": [{"id": "s2", "name": "Spell 2"}]}
    ]

    # Action
    result = loader.load("dnd_2024")

    # Assert
    assert len(result["spells"]) == 2
    spells = {s["id"] for s in result["spells"]}
    assert spells == {"s1", "s2"}

@patch("modules.compendium.loader.CompendiumLoader._load_module")
def test_load_filters_modules(mock_load_module, compendium_loader):
    loader, mock_root = compendium_loader
    # Setup mocks
    ruleset_path = MagicMock(spec=Path)
    mock_root.__truediv__.return_value = ruleset_path
    ruleset_path.exists.return_value = True
    
    mod1 = MagicMock(spec=Path)
    mod1.is_dir.return_value = True
    mod1.name = "core"
    mod1.__lt__ = lambda s, o: s.name < o.name
    
    mod2 = MagicMock(spec=Path)
    mod2.is_dir.return_value = True
    mod2.name = "expansion"
    mod2.__lt__ = lambda s, o: s.name < o.name

    ruleset_path.iterdir.return_value = [mod1, mod2]
    
    # Mock payload
    mock_load_module.return_value = {"spells": [{"id": "s1"}]}

    # Action: Only load 'core'
    result = loader.load("dnd_2024", active_modules={"core"})

    # Assert
    # _load_module should be called once (for core)
    assert mock_load_module.call_count == 1
    loader._load_module.assert_called_with(mod1)
