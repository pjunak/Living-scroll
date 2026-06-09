"""
Hydration Pipeline for Character Sheet generation.

Each step implements the HydrationStep protocol and is responsible
for one isolated aspect of character sheet rehydration.
"""

from __future__ import annotations

from typing import Protocol, List, TYPE_CHECKING

if TYPE_CHECKING:
    from modules.character_sheet.model.model import CharacterSheet
    from modules.character_sheet.model.schema import CharacterData
    from modules.compendium.service import Compendium


class HydrationStep(Protocol):
    """Interface that every pipeline processor must satisfy."""

    def apply(
        self,
        sheet: "CharacterSheet",
        data: "CharacterData",
        compendium: "Compendium",
    ) -> None:
        """Mutate *sheet* in-place based on *data* and *compendium*."""
        ...
