import pytest
from PySide6.QtWidgets import QApplication
import sys

# Ensure we have a QApplication instance for UI tests
@pytest.fixture(scope="session")
def qapp():
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    return app

def test_spell_grapher_load(qapp):
    """Test that the Spell Grapher window can be instantiated without crashing."""
    from modules.spell_grapher.ui.window import MainWindow
    try:
        window = MainWindow()
        assert window is not None
    except Exception as e:
        pytest.fail(f"Spell Grapher failed to load: {e}")

def test_rules_explorer_load(qapp):
    """Test that the Rules Explorer window can be instantiated without crashing."""
    from modules.rules_explorer.ui.window import CompendiumWindow
    try:
        window = CompendiumWindow()
        assert window is not None
    except Exception as e:
        pytest.fail(f"Rules Explorer failed to load: {e}")

def test_bestiary_load(qapp):
    """Test that the Bestiary window can be instantiated without crashing."""
    from modules.bestiary.ui.window import MonsterWindow
    try:
        window = MonsterWindow()
        assert window is not None
    except Exception as e:
        pytest.fail(f"Bestiary failed to load: {e}")

def test_equipment_manager_load(qapp):
    """Test that the Equipment Manager window can be instantiated without crashing."""
    from modules.equipment.ui.window import EquipmentWindow
    try:
        window = EquipmentWindow()
        assert window is not None
    except Exception as e:
        pytest.fail(f"Equipment Manager failed to load: {e}")

def test_grimoire_load(qapp):
    """Test that the Grimoire Spell Browser window can be instantiated without crashing."""
    from modules.grimoire.ui.window import SpellWindow
    try:
        window = SpellWindow()
        assert window is not None
    except Exception as e:
        pytest.fail(f"Grimoire failed to load: {e}")

def test_character_hub_load(qapp):
    """Test that the Character Hub window can be instantiated without crashing."""
    from modules.character_sheet.ui.hub import CharacterSheetHubWindow
    try:
        window = CharacterSheetHubWindow(app_context=None)
        assert window is not None
    except Exception as e:
        pytest.fail(f"Character Hub failed to load: {e}")
