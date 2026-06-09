"""Service for parsing compendium spell records into graphing-ready formats."""

from typing import Dict, List, Any
import re

def parse_spell_record_from_compendium(payload: dict) -> dict:
    """Convert a filesystem compendium spell record into the runtime shape used by the UI."""
    record = dict(payload or {})
    effects: List[dict] = []
    
    # Process actions block based on the bold new YAML schema
    actions = record.get("actions", [])
    if isinstance(actions, list):
        for action in actions:
            if not isinstance(action, dict): continue

            # Extract Damage
            damage_list = action.get("damage", [])
            if isinstance(damage_list, list) and damage_list:
                first_dmg = damage_list[0]
                base = first_dmg.get("base", {})
                scaling = first_dmg.get("scaling", {})
                
                if isinstance(base, dict) and base.get("dice"):
                    effects.append({
                        "effect_type": "primary",
                        "effect_data": {
                            "damage": {
                                "type": first_dmg.get("type", "damage"),
                                "base": {"dice": base.get("dice", 0), "die": base.get("die", 0)},
                                "scaling": {"dice_per_slot": scaling.get("dice_per_slot", 0), "die": scaling.get("die", 0)}
                            }
                        }
                    })
                    continue # Try not to stack multiple primary effects for now

            # Extract Healing
            healing = action.get("healing", {})
            if isinstance(healing, dict):
                base = healing.get("base", {})
                if isinstance(base, dict) and base.get("dice"):
                    effects.append({
                        "effect_type": "primary",
                        "effect_data": {
                            "damage": {  # UI currently expects 'damage' shape for graphing
                                "type": "healing",
                                "base": {"dice": base.get("dice", 0), "die": base.get("die", 0)},
                                "scaling": {"dice_per_slot": base.get("dice", 0), "die": base.get("die", 0)} # Healing scaling often mirrors base
                            }
                        }
                    })
                    continue

    runtime: dict = {
        "id": record.get("id"),
        "name": record.get("name"),
        "level": record.get("level", 0),
        "school": record.get("school"),
        "casting_time": record.get("casting_time"),
        "range": record.get("range"),
        "duration": record.get("duration"),
        "components": record.get("components", []),
        "effects": effects,
        "modifiers": [],
    }

    scaling_levels = record.get("scaling_levels")
    if isinstance(scaling_levels, list):
        runtime["scaling_levels"] = list(scaling_levels)

    return runtime
