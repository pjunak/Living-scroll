"""Pydantic models for Compendium data structures."""

from __future__ import annotations

from typing import Dict, List, Optional, Union, Any, Literal
from pydantic import BaseModel, Field, AliasChoices

class BonusBundle(BaseModel):
    """Represents flat bonuses and spell slots."""
    bonuses: Dict[str, int] = Field(default_factory=dict)
    spell_slots: Dict[str, int] = Field(default_factory=dict)

class TraitGrants(BaseModel):
    """Represents grants of senses, resistances, and immunities."""
    senses: Dict[str, int] = Field(default_factory=dict)
    resistances: List[str] = Field(default_factory=list)
    condition_immunities: List[str] = Field(default_factory=list)

class SkillGrants(BaseModel):
    """Represents skill proficiency grants."""
    skills: Union[Dict[str, int], List[str]] = Field(default_factory=dict)

class Grants(BaseModel):
    """Container for all mechanical effects granted by a record."""
    bonuses: Dict[str, int] = Field(default_factory=dict)
    spell_slots: Dict[str, int] = Field(default_factory=dict)
    senses: Dict[str, int] = Field(default_factory=dict)
    resistances: List[str] = Field(default_factory=list)
    condition_immunities: List[str] = Field(default_factory=list)
    skills: Union[Dict[str, int], List[str]] = Field(default_factory=dict)
    hp_per_level: int = 0
    
    # Flexible parsing for unquantifiable modifiers
    unquantifiable_modifiers: List[str] = Field(
        default_factory=list,
        validation_alias=AliasChoices("unquantifiable_modifiers", "unquantifiable_modifier", "unqualifiable_modifier")
    )
    
    armor_class_formulas: List[Dict[str, Any]] = Field(default_factory=list)
    armor_class_formula: Optional[Dict[str, Any]] = None

class CompendiumRecord(BaseModel):
    """Base model for all compendium records."""
    id: str
    name: str
    description: Optional[str] = None
    source: str = "PHB24" # Default source
    grants: Optional[Grants] = None
    
    # Internal metadata
    meta_source_path: Optional[str] = Field(default=None, alias="_meta_source_path")

class Spell(CompendiumRecord):
    level: int
    school: str
    casting_time: str = Field(default="1 action")
    range: str = Field(default="Touch")
    components: List[str] = Field(default_factory=list)
    duration: str = Field(default="Instantaneous")
    ritual: bool = False
    concentration: bool = False
    text: Dict[str, str] = Field(default_factory=dict)

class FeatureOption(BaseModel):
    """An option available within a feature, potentially with its own grants."""
    label: str
    value: str
    grants: Optional[Grants] = None

class Feature(CompendiumRecord):
    """A feature granted by a class, race, or feat."""
    level: int = 1
    prerequisites: List[Dict[str, Any]] = Field(default_factory=list)
    options: List[FeatureOption] = Field(default_factory=list)

class Subclass(CompendiumRecord):
    class_name: str = Field(default="") # Usually inferred or linked
    features: List[Feature] = Field(default_factory=list)
    spellcasting: Optional[Dict[str, Any]] = None

class Class(CompendiumRecord):
    hit_die: str
    primary_ability: Union[str, List[str]]
    saves: List[str]
    subclasses: List[Subclass] = Field(default_factory=list)
    features: List[Feature] = Field(default_factory=list)
    spellcasting: Optional[Dict[str, Any]] = None
    multiclass_requirements: Optional[Dict[str, int]] = None
    armor_class_formula: Optional[str] = None

class Feat(CompendiumRecord):
    prerequisite: Optional[str] = None
    repeatable: bool = False

class Background(CompendiumRecord):
    pass

class Species(CompendiumRecord):
    subtypes: List[Species] = Field(default_factory=list)

