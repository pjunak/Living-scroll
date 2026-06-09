import pytest
from unittest.mock import patch
from modules.core.services.settings import Settings

@pytest.fixture
def mock_qsettings():
    with patch("modules.core.services.settings.QSettings") as mock_q:
        mock_instance = mock_q.return_value
        # Default mock behavior: return default value if provided, else None
        def get_value(key, default=None, type=None):
            return default
        mock_instance.value.side_effect = get_value
        yield mock_instance

def list_clean_env(monkeypatch):
    monkeypatch.delenv("LIVING_SCROLL_RULESET", raising=False)
    monkeypatch.delenv("LIVING_SCROLL_MODULES", raising=False)

def test_defaults(mock_qsettings, monkeypatch):
    list_clean_env(monkeypatch)
    s = Settings()
    # Mock returns None -> default handling in property
    assert s.ruleset == "dnd_2024"
    assert s.dev_mode is False

def test_env_var_override(mock_qsettings, monkeypatch):
    list_clean_env(monkeypatch)
    monkeypatch.setenv("LIVING_SCROLL_RULESET", "custom_rules")
    s = Settings()
    assert s.ruleset == "custom_rules"

def test_active_modules_parsing(mock_qsettings, monkeypatch):
    list_clean_env(monkeypatch)
    monkeypatch.setenv("LIVING_SCROLL_MODULES", "mod_a,mod_b")
    s = Settings()
    # Required 'players_handbook' is always added
    assert "mod_a" in s.active_modules
    assert "mod_b" in s.active_modules
    assert "players_handbook" in s.active_modules
