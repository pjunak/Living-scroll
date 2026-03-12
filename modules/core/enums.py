"""Centralized Enums for Core Game Concepts.

This module replaces stringly-typed identifiers across the project to improve
type safety and reduce typos.
"""

from enum import Enum

class Ability(str, Enum):
    STR = "STR"
    DEX = "DEX"
    CON = "CON"
    INT = "INT"
    WIS = "WIS"
    CHA = "CHA"

class Skill(str, Enum):
    ACROBATICS = "Acrobatics"
    ANIMAL_HANDLING = "Animal Handling"
    ARCANA = "Arcana"
    ATHLETICS = "Athletics"
    DECEPTION = "Deception"
    HISTORY = "History"
    INSIGHT = "Insight"
    INTIMIDATION = "Intimidation"
    INVESTIGATION = "Investigation"
    MEDICINE = "Medicine"
    NATURE = "Nature"
    PERCEPTION = "Perception"
    PERFORMANCE = "Performance"
    PERSUASION = "Persuasion"
    RELIGION = "Religion"
    SLEIGHT_OF_HAND = "Sleight of Hand"
    STEALTH = "Stealth"
    SURVIVAL = "Survival"

class ArmorType(str, Enum):
    LIGHT = "light"
    MEDIUM = "medium"
    HEAVY = "heavy"
    SHIELD = "shield"

class WeaponProperty(str, Enum):
    AMMUNITION = "ammunition"
    FINESSE = "finesse"
    HEAVY = "heavy"
    LIGHT = "light"
    LOADING = "loading"
    REACH = "reach"
    THROWN = "thrown"
    TWO_HANDED = "two-handed"
    VERSATILE = "versatile"
