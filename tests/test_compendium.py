import unittest
from unittest.mock import MagicMock, patch
from pathlib import Path
from modules.compendium.service import Compendium
from modules.compendium.loader import CompendiumLoader

class TestCompendium(unittest.TestCase):
    def setUp(self):
        self.sample_payload = {
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
        self.compendium = Compendium(self.sample_payload)

    def test_record_by_id(self):
        # Direct hit
        rec = self.compendium.record_by_id("spell:fireball")
        self.assertIsNotNone(rec)
        self.assertEqual(rec["name"], "Fireball")

        # Miss
        rec = self.compendium.record_by_id("spell:nada")
        self.assertIsNone(rec)

    def test_filter_by_type(self):
        # Use public API records()
        spells = self.compendium.records("spells")
        self.assertEqual(len(spells), 1)
        self.assertEqual(spells[0]["name"], "Fireball")

        items = self.compendium.records("equipment")
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["name"], "Sword")

    def test_filter_by_custom_predicate(self):
        # Manual filter on records
        all_spells = self.compendium.records("spells")
        results = [s for s in all_spells if s.get("name", "").startswith("F")]
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Fireball")


class TestCompendiumLoader(unittest.TestCase):
    def setUp(self):
        self.mock_root = MagicMock(spec=Path)
        self.loader = CompendiumLoader(self.mock_root)

    @patch("modules.compendium.loader.CompendiumLoader._load_module")
    def test_load_merges_modules(self, mock_load_module):
        # Setup mocks
        ruleset_path = MagicMock(spec=Path)
        self.mock_root.__truediv__.return_value = ruleset_path
        ruleset_path.exists.return_value = True
        
        # Mock module directories
        mod1 = MagicMock(spec=Path)
        mod1.is_dir.return_value = True
        mod1.name = "core"
        # Fix sorting
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
        result = self.loader.load("dnd_2024")

        # Assert
        self.assertEqual(len(result["spells"]), 2)
        spells = {s["id"] for s in result["spells"]}
        self.assertEqual(spells, {"s1", "s2"})

    @patch("modules.compendium.loader.CompendiumLoader._load_module")
    def test_load_filters_modules(self, mock_load_module):
        # Setup mocks
        ruleset_path = MagicMock(spec=Path)
        self.mock_root.__truediv__.return_value = ruleset_path
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
        result = self.loader.load("dnd_2024", active_modules={"core"})

        # Assert
        # _load_module should be called once (for core)
        self.assertEqual(mock_load_module.call_count, 1)
        self.loader._load_module.assert_called_with(mod1)

if __name__ == "__main__":
    unittest.main()
