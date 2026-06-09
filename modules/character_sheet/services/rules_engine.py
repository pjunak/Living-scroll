"""
Rules Engine for 5th Edition (2024).
Responsible for rehydrating a full CharacterSheet from CharacterData (decisions).

Refactored to a Pipeline architecture: each aspect of character sheet generation
is handled by an isolated HydrationStep processor.
"""

from __future__ import annotations

import logging
from typing import List

from modules.character_sheet.model.model import CharacterSheet, ProficiencySet
from modules.character_sheet.model.schema import CharacterData
from modules.compendium.service import Compendium

from modules.character_sheet.services.hydration_steps import HydrationStep
from modules.character_sheet.services.hydration_steps.identity_step import IdentityStep
from modules.character_sheet.services.hydration_steps.stats_step import BaseStatsStep
from modules.character_sheet.services.hydration_steps.species_step import SpeciesStep
from modules.character_sheet.services.hydration_steps.background_step import BackgroundStep
from modules.character_sheet.services.hydration_steps.class_step import ClassStep
from modules.character_sheet.services.hydration_steps.derived_step import DerivedStatsStep
from modules.character_sheet.services.hydration_steps.validation_step import ValidationStep

log = logging.getLogger(__name__)


class RulesEngine:
    """
    Pipeline executor for character sheet rehydration.
    
    Each step in the pipeline mutates the CharacterSheet in-place,
    in dependency order:
    
    1. Identity   — name, alignment, portrait
    2. Base Stats  — raw ability scores
    3. Species    — species traits, resistances, senses
    4. Background — +2/+1 bonuses, proficiencies, Origin Feat
    5. Class      — level-by-level features, subclass merging
    6. Derived    — proficiency bonus, HP, spell slots, save DCs
    7. Validation — dev-mode warnings (never blocks sheet generation)
    """

    def __init__(self, compendium: Compendium) -> None:
        self.compendium = compendium
        self._validation_step = ValidationStep()

        self.pipeline: List[HydrationStep] = [
            IdentityStep(),
            BaseStatsStep(),
            SpeciesStep(),
            BackgroundStep(),
            ClassStep(),
            DerivedStatsStep(),
            self._validation_step,
        ]

    def hydrate(self, data: CharacterData) -> CharacterSheet:
        """
        Reconstruct a CharacterSheet from raw decisions (CharacterData).
        """
        sheet = CharacterSheet()
        sheet.proficiencies = ProficiencySet()

        for step in self.pipeline:
            try:
                step.apply(sheet, data, self.compendium)
            except Exception as exc:
                step_name = type(step).__name__
                log.error("Hydration step %s failed: %s", step_name, exc, exc_info=True)

        return sheet

    @property
    def validation_warnings(self):
        """Access dev-mode warnings from the most recent hydration."""
        return self._validation_step.warnings
