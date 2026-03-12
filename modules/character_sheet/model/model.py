"""Structured representation of the D&D 2024 character sheet."""

from __future__ import annotations

from __future__ import annotations
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, root_validator, ConfigDict

from modules.core.enums import Ability

ABILITY_NAMES = tuple(a.value for a in Ability)

class AbilityBlock(BaseModel):
    model_config = ConfigDict(extra="ignore")
    score: int = Field(default=10)
    modifier: Optional[int] = None
    save_proficient: bool = Field(default=False)
    save_bonus: int = Field(default=0)

    def effective_modifier(self) -> int:
        if self.modifier is not None:
            return self.modifier
        return (self.score - 10) // 2

    def save_modifier(self, proficiency_bonus: int) -> int:
        base = self.effective_modifier()
        if self.save_proficient:
            base += proficiency_bonus
        return base + self.save_bonus

class ClassProgression(BaseModel):
    model_config = ConfigDict(extra="ignore")
    name: str = Field(default="")
    level: int = Field(default=0)
    subclass: Optional[str] = None

class BackgroundSelection(BaseModel):
    model_config = ConfigDict(extra="ignore")
    ability_choices: List[str] = Field(default_factory=list)
    skill_choices: List[str] = Field(default_factory=list)
    tool_choices: List[str] = Field(default_factory=list)
    language_choices: List[str] = Field(default_factory=list)
    feat_choice: str = Field(default="")

class CharacterIdentity(BaseModel):
    model_config = ConfigDict(extra="ignore")
    name: str = Field(default="")
    ancestry: str = Field(default="")
    background: str = Field(default="")
    background_choices: BackgroundSelection = Field(default_factory=BackgroundSelection)
    player: str = Field(default="")
    alignment: str = Field(default="")
    experience: int = Field(default=0)
    classes: List[ClassProgression] = Field(default_factory=list)
    level_cap: int = Field(default=0)
    ability_generation: str = Field(default="manual")
    asi_choices: Dict[int, str] = Field(default_factory=dict)
    portrait_path: str = Field(default="")

    @property
    def level(self) -> int:
        return sum(entry.level for entry in self.classes) or 0

    @property
    def effective_level_cap(self) -> int:
        base = self.level_cap or self.level or 1
        return max(1, base)

class CombatStats(BaseModel):
    model_config = ConfigDict(extra="ignore")
    armor_class: int = Field(default=10)
    initiative_bonus: int = Field(default=0)
    speed_ft: int = Field(default=30)
    max_hp: int = Field(default=0)
    current_hp: int = Field(default=0)
    temp_hp: int = Field(default=0)
    hit_dice: str = Field(default="")
    death_save_successes: int = Field(default=0)
    death_save_failures: int = Field(default=0)

class ProficiencySet(BaseModel):
    model_config = ConfigDict(extra="ignore")
    proficiency_bonus: int = Field(default=2)
    armor: List[str] = Field(default_factory=list)
    weapons: List[str] = Field(default_factory=list)
    tools: List[str] = Field(default_factory=list)
    languages: List[str] = Field(default_factory=list)
    skills: Dict[str, int] = Field(default_factory=dict)

class EquipmentItem(BaseModel):
    model_config = ConfigDict(extra="ignore")
    name: str = Field(default="")
    quantity: int = Field(default=1)
    weight_lb: float = Field(default=0.0)
    attuned: bool = Field(default=False)
    equipped: bool = Field(default=False)
    notes: str = Field(default="")
    bonuses: Dict[str, int] = Field(default_factory=dict)
    compendium_id: str = Field(default="")
    cost: str = Field(default="")
    rarity: str = Field(default="")

class FeatureEntry(BaseModel):
    model_config = ConfigDict(extra="ignore")
    title: str = Field(default="")
    source: str = Field(default="")
    description: str = Field(default="")
    compendium_id: str = Field(default="")

class ResourcePool(BaseModel):
    model_config = ConfigDict(extra="ignore")
    name: str = Field(default="")
    max_uses: int = Field(default=0)
    current_uses: int = Field(default=0)
    refreshes_on: str = Field(default="")

class SpellAccessEntry(BaseModel):
    model_config = ConfigDict(extra="ignore")
    spell_name: str = Field(default="")
    source: str = Field(default="")
    prepared: bool = Field(default=False)
    category: str = Field(default="")
    source_type: str = Field(default="")
    source_id: str = Field(default="")
    ability: Optional[str] = None
    granted: bool = Field(default=False)

class SpellSourceRecord(BaseModel):
    model_config = ConfigDict(extra="ignore")
    source_type: str = Field(default="")
    source_id: str = Field(default="")
    label: str = Field(default="")
    ability: Optional[str] = None


def _default_slot_schedule() -> Dict[str, Dict[int, int]]:
    return {"long_rest": {}, "short_rest": {}}


def _normalise_slot_dict(entries: Mapping[str, Any] | Dict[int, Any]) -> Dict[int, int]:
    result: Dict[int, int] = {}
    for level, amount in (entries or {}).items():
        try:
            lvl = int(level)
            amt = int(amount)
        except (TypeError, ValueError):
            continue
        if lvl <= 0 or amt <= 0:
            continue
        result[lvl] = amt
    return result


def _aggregate_slot_schedule(schedule: Mapping[str, Dict[int, int]]) -> Dict[int, int]:
    combined: Dict[int, int] = {}
    for pool in (schedule or {}).values():
        for level, amount in (pool or {}).items():
            if amount <= 0:
                continue
            combined[level] = combined.get(level, 0) + amount
    return combined


def _copy_slot_pools(pools: Mapping[int, int]) -> Dict[int, int]:
    return {level: amount for level, amount in pools.items() if amount > 0}


class SpellcastingData(BaseModel):
    model_config = ConfigDict(extra="ignore")
    spellcasting_ability: str = Field(default="INT")
    attack_bonus: Optional[int] = None
    save_dc: Optional[int] = None
    known_spells: List[SpellAccessEntry] = Field(default_factory=list)
    spell_sources: List[SpellSourceRecord] = Field(default_factory=list)
    slot_schedule: Dict[str, Dict[int, int]] = Field(default_factory=_default_slot_schedule)
    slot_state: Dict[str, Dict[int, int]] = Field(default_factory=_default_slot_schedule)
    spell_slots: Dict[int, int] = Field(default_factory=dict)
    prepared_spells: List[str] = Field(default_factory=list)

    def model_post_init(self, __context: Any) -> None:
        self.sync_slot_schedule()

    def sync_slot_schedule(self) -> None:
        """Keep aggregated spell slots and rest-based pools aligned."""

        raw_schedule = self.slot_schedule or {}
        schedule = {
            "long_rest": _normalise_slot_dict(raw_schedule.get("long_rest", {})),
            "short_rest": _normalise_slot_dict(raw_schedule.get("short_rest", {})),
        }
        if not any(schedule.values()):
            if self.spell_slots:
                schedule["long_rest"] = _normalise_slot_dict(self.spell_slots)
            else:
                schedule = _default_slot_schedule()

        raw_state = self.slot_state or {}
        state: Dict[str, Dict[int, int]] = {}
        for rest_key, pool in schedule.items():
            state_pool = _normalise_slot_dict(raw_state.get(rest_key, pool))
            clamped: Dict[int, int] = {}
            for level, maximum in pool.items():
                value = state_pool.get(level, maximum)
                clamped[level] = max(0, min(value, maximum))
            state[rest_key] = clamped

        self.slot_schedule = schedule
        self.slot_state = state
        self.spell_slots = _aggregate_slot_schedule(self.slot_state)

    def reset_slots(self, rest_type: str) -> None:
        """Restore slot state according to the requested rest type."""

        rest_key = str(rest_type or "").lower()
        if rest_key not in {"short", "short_rest", "long", "long_rest"}:
            rest_key = "long_rest"
        if rest_key.startswith("short"):
            current_long = _copy_slot_pools(self.slot_state.get("long_rest", self.slot_schedule.get("long_rest", {})))
            self.slot_state["short_rest"] = _copy_slot_pools(self.slot_schedule.get("short_rest", {}))
            self.slot_state["long_rest"] = current_long
        else:
            self.slot_state = {
                "long_rest": _copy_slot_pools(self.slot_schedule.get("long_rest", {})),
                "short_rest": _copy_slot_pools(self.slot_schedule.get("short_rest", {})),
            }
        self.spell_slots = _aggregate_slot_schedule(self.slot_state)

class CharacterSheet(BaseModel):
    model_config = ConfigDict(extra="ignore")
    identity: CharacterIdentity = Field(default_factory=CharacterIdentity)
    abilities: Dict[str, AbilityBlock] = Field(
        default_factory=lambda: {name: AbilityBlock() for name in ABILITY_NAMES}
    )
    combat: CombatStats = Field(default_factory=CombatStats)
    proficiencies: ProficiencySet = Field(default_factory=ProficiencySet)
    equipment: List[EquipmentItem] = Field(default_factory=list)
    features: List[FeatureEntry] = Field(default_factory=list)
    resources: List[ResourcePool] = Field(default_factory=list)
    spellcasting: SpellcastingData = Field(default_factory=SpellcastingData)
    feature_options: Dict[str, str] = Field(default_factory=dict)
    class_options: Dict[str, List[str]] = Field(default_factory=dict)
    notes: Dict[str, str] = Field(default_factory=dict)

    def get_ability(self, name: str) -> AbilityBlock:
        key = name.upper()
        if key not in self.abilities:
            raise KeyError(f"Unknown ability: {name}")
        return self.abilities[key]


def character_sheet_to_dict(sheet: CharacterSheet, compendium: Any = None) -> Dict[str, Any]:
    # With Pydantic, we can just use model_dump()
    data = sheet.model_dump(exclude_none=True)
    
    # Keeping the custom equipment dehydration for now since it touches Compendium
    if compendium and "equipment" in data:
        minified_equipment = []
        for item in sheet.equipment:
            entry = {
                "name": item.name,
                "quantity": item.quantity,
                "attuned": item.attuned,
                "equipped": item.equipped,
            }
            if item.compendium_id:
                entry["compendium_id"] = item.compendium_id
            
            if not item.compendium_id:
                entry["weight_lb"] = item.weight_lb
                entry["notes"] = item.notes
                entry["bonuses"] = item.bonuses
                entry["cost"] = item.cost
                entry["rarity"] = item.rarity
            else:
                if item.notes:
                    entry["notes"] = item.notes
            
            minified_equipment.append(entry)
        data["equipment"] = minified_equipment

    return data

# Note: The custom hydration logic for equipment/features will need to be refactored into the Engine
# For now, we wrap Pydantic's validation to match the old signature but allow it to parse the nested dict directly.
def character_sheet_from_dict(data: Any, compendium: Any = None) -> CharacterSheet:
    # This completely replaces the 150-line custom parse
    # For robust backwards compatibility in case `data` has strange None values
    sheet = CharacterSheet.model_validate(data)
    
    # We still need to do the custom hydration pass for equipment and features because
    # they currently depend on the Compendium for stats. We will extract this to engine later.
    if compendium:
        _hydrate_equipment(sheet, compendium)
        _hydrate_features(sheet, compendium)
        
    return sheet

def _hydrate_equipment(sheet: CharacterSheet, compendium: Any) -> None:
    for item in sheet.equipment:
        if not item.compendium_id and not item.name:
            continue
            
        record = None
        if item.compendium_id:
             record = compendium.record_by_id(item.compendium_id)
        if not record and item.name:
             # simple name fallback
             try:
                 for eq in compendium.records("equipment"):
                     if isinstance(eq, dict) and "items" in eq:
                         for r in eq["items"]:
                             if str(r.get("name", "")).lower() == item.name.lower():
                                 record = r
                                 break
                     if record: break
             except Exception:
                 pass
                 
        if record:
             item.compendium_id = record.get("id", item.compendium_id)
             if not item.name: item.name = record.get("name", item.name)
             if item.weight_lb == 0.0:
                 w_str = str(record.get("weight", "")).lower().replace("lb.", "").strip()
                 try:
                     item.weight_lb = float(w_str)
                 except ValueError:
                     pass
             if not item.cost: item.cost = str(record.get("cost", ""))
             if not item.rarity: item.rarity = str(record.get("rarity", ""))

def _hydrate_features(sheet: CharacterSheet, compendium: Any) -> None:
    for feature in sheet.features:
        if not feature.compendium_id: continue
        record = compendium.record_by_id(feature.compendium_id)
        if record and not feature.description:
            text_val = record.get("text")
            if isinstance(text_val, dict):
                feature.description = text_val.get("full", "")
            elif isinstance(text_val, str):
                feature.description = text_val


__all__ = [
    "ABILITY_NAMES",
    "AbilityBlock",
    "CharacterIdentity",
    "ClassProgression",
    "BackgroundSelection",
    "CombatStats",
    "ProficiencySet",
    "EquipmentItem",
    "FeatureEntry",
    "ResourcePool",
    "SpellAccessEntry",
    "SpellSourceRecord",
    "SpellcastingData",
    "CharacterSheet",
    "character_sheet_to_dict",
    "character_sheet_from_dict",
]