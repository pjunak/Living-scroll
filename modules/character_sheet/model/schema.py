""" 
Persistence Schema for Character Data.
This module defines the "Source of Truth" data structures that represent
user decisions, independent of the calculated Character Sheet results.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Any

@dataclass
class IdentityData:
    """Core identity decisions."""
    name: str = ""
    ancestry: str = ""         # Species Key (e.g., "elf")
    ancestry_subtype: str = "" # Sub-species Key (e.g., "high_elf")
    background: str = ""       # Background Key (e.g., "criminal")
    alignment: str = ""
    player_name: str = ""
    portrait_path: str = ""
    xp: int = 0
    level_cap: int = 20

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> IdentityData:
        return cls(**{k: v for k, v in data.items() if k in cls.__annotations__})

@dataclass
class ClassLevelData:
    """A single class entry in the progression."""
    class_name: str            # Class Key (e.g., "rogue")
    level: int = 1
    subclass: Optional[str] = None
    
    # Feature Choices: Map of feature_key -> selection_value
    # e.g., {"rogue_skill_1": "stealth", "rogue_expertise_1": "stealth"}
    feature_choices: Dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> ClassLevelData:
        return cls(
            class_name=data.get("class_name", ""),
            level=data.get("level", 1),
            subclass=data.get("subclass"),
            feature_choices=data.get("feature_choices", {})
        )

@dataclass
class CharacterData:
    """
    The root Save File object.
    Contains ONLY decisions, no computed results.
    """
    version: str = "1.0"
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    
    # Core Decisions
    identity: IdentityData = field(default_factory=IdentityData)
    
    # Base Stats (Before racial/feat bonuses)
    # e.g. {"STR": 15, "DEX": 14, ...} or Point Buy config
    base_stats: Dict[str, int] = field(default_factory=lambda: {
        "STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10
    })
    
    # Class Progression
    classes: List[ClassLevelData] = field(default_factory=list)
    
    # Background selections/customization
    # e.g. {"background_skill_1": "athletics"}
    background_choices: Dict[str, str] = field(default_factory=dict)
    
    # Inventory (Stateful, not fully re-computable)
    equipment: List[Dict[str, Any]] = field(default_factory=list)
    
    # Roleplay / Notes
    notes: Dict[str, str] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> CharacterData:
        identity = IdentityData.from_dict(data.get("identity", {}))
        
        classes = [
            ClassLevelData.from_dict(c) 
            for c in data.get("classes", [])
        ]
        
        return cls(
            version=data.get("version", "1.0"),
            id=data.get("id", str(uuid.uuid4())),
            identity=identity,
            base_stats=data.get("base_stats", {
                "STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10
            }),
            classes=classes,
            background_choices=data.get("background_choices", {}),
            equipment=data.get("equipment", []),
            notes=data.get("notes", {})
        )

