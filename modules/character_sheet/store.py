"""State Management for the Character Sheet.

This module implements a unidirectional Store pattern.
UI components dispatch updates to the store, which persists changes
and emits a centralized `character_updated` signal.
"""

from typing import Dict, Any

from PySide6.QtCore import QObject, Signal

from modules.character_sheet.model import CharacterSheet
from modules.character_sheet.services.library import CharacterLibrary, CharacterRecord
from modules.compendium.service import Compendium
from modules.dnd24_mechanics.engine import CharacterEngine


class CharacterStore(QObject):
    """Centralized state manager for a single character."""
    
    # Emitted whenever the character sheet or modifiers change successfully.
    # Payload: (updated_record, updated_engine)
    character_updated = Signal(object, object) 
    
    # Emitted if an update fails (e.g., IO error saving to disk).
    error_occurred = Signal(str)

    def __init__(self, record: CharacterRecord, library: CharacterLibrary, compendium: Compendium, parent: QObject | None = None):
        super().__init__(parent)
        self._record = record
        self._library = library
        self._compendium = compendium
        self._engine = CharacterEngine(self._record.sheet, self._compendium)

    @property
    def record(self) -> CharacterRecord:
        """Get the current read-only record."""
        return self._record

    @property
    def sheet(self) -> CharacterSheet:
        """Get the current character sheet."""
        return self._record.sheet

    @property
    def engine(self) -> CharacterEngine:
        """Get the current calculation engine."""
        return self._engine

    def dispatch_update(self, new_sheet: CharacterSheet, new_modifiers: Dict[str, bool], data: Any = None) -> None:
        """
        Request a state change. 
        Replaces direct calls to `library.update_record`.
        """
        payload_data = data if data is not None else self._record.data
        try:
            self._library.update_record(self._record.identifier, new_sheet, new_modifiers, data=payload_data)
            
            # Reload fresh state
            self._record = self._library.get(self._record.identifier)
            self._engine = CharacterEngine(self._record.sheet, self._compendium)
            
            # Broadcast the update to all listening UI components
            self.character_updated.emit(self._record, self._engine)
        except Exception as e:
            self.error_occurred.emit(str(e))
