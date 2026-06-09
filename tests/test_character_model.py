import pytest
from modules.character_sheet.model.model import (
    AbilityBlock,
    CharacterIdentity,
    ClassProgression,
    SpellcastingData,
    _default_slot_schedule,
    CharacterSheet,
    character_sheet_to_dict,
    character_sheet_from_dict
)

# TestAbilityBlock
def test_effective_modifier_standard():
    # Score 10 -> +0
    ab = AbilityBlock(score=10)
    assert ab.effective_modifier() == 0
    
    # Score 20 -> +5
    ab = AbilityBlock(score=20)
    assert ab.effective_modifier() == 5
    
    # Score 1 -> -5
    ab = AbilityBlock(score=1)
    assert ab.effective_modifier() == -5

def test_effective_modifier_override():
    # Override takes precedence over score
    ab = AbilityBlock(score=10, modifier=5)
    assert ab.effective_modifier() == 5

def test_save_modifier():
    prof_bonus = 3
    # No proficiency: +1 from score 12
    ab = AbilityBlock(score=12, save_proficient=False)
    assert ab.save_modifier(prof_bonus) == 1

    # With proficiency: +1 + 3 = 4
    ab.save_proficient = True
    assert ab.save_modifier(prof_bonus) == 4
    
    # With extra bonus item/feature: +1 + 3 + 2 = 6
    ab.save_bonus = 2
    assert ab.save_modifier(prof_bonus) == 6


# TestCharacterIdentity
def test_level_calculation():
    ident = CharacterIdentity()
    assert ident.level == 0
    
    ident.classes.append(ClassProgression(name="Wizard", level=3))
    assert ident.level == 3
    
    ident.classes.append(ClassProgression(name="Fighter", level=2))
    assert ident.level == 5


# TestSpellcastingData
def test_sync_slot_schedule_initializes_empty():
    sd = SpellcastingData()
    assert sd.spell_slots == {}

def test_sync_slot_schedule_aggregates_slots():
    sd = SpellcastingData()
    # Simulate setup
    sd.slot_schedule = {
        "long_rest": {1: 4, 2: 2},
        "short_rest": {1: 2} # Warlock style
    }
    # Force sync (usually runs in post_init or manual call)
    sd.sync_slot_schedule()
    
    # Should sum long and short rest slots: Lvl 1: 4+2=6, Lvl 2: 2
    assert sd.spell_slots[1] == 6
    assert sd.spell_slots[2] == 2
    
    # State should be initialized to max if empty
    assert sd.slot_state["long_rest"][1] == 4
    assert sd.slot_state["short_rest"][1] == 2

def test_reset_slots_long_rest():
    sd = SpellcastingData()
    sd.slot_schedule = {"long_rest": {1: 4}, "short_rest": {}}
    sd.sync_slot_schedule()
    
    # Spend a slot
    sd.slot_state["long_rest"][1] = 0
    sd.spell_slots = {1: 0}
    
    # Reset Long Rest
    sd.reset_slots("long_rest")
    assert sd.slot_state["long_rest"][1] == 4
    assert sd.spell_slots[1] == 4

def test_reset_slots_short_rest():
    sd = SpellcastingData()
    sd.slot_schedule = {"long_rest": {1: 4}, "short_rest": {2: 2}}
    sd.sync_slot_schedule()
    
    # Spend slots
    sd.slot_state["long_rest"][1] = 0
    sd.slot_state["short_rest"][2] = 0
    
    sd.reset_slots("short_rest")
    assert sd.slot_state["long_rest"].get(1, 0) == 0
    assert sd.slot_state["short_rest"][2] == 2
    # Total slots should reflect this (0 + 2 = 2)
    assert sd.spell_slots.get(1, 0) == 0
    assert sd.spell_slots[2] == 2


# TestSerialization
def test_round_trip():
    sheet = CharacterSheet()
    sheet.identity.name = "Test Hero"
    sheet.abilities["STR"].score = 18
    sheet.identity.classes.append(ClassProgression(name="Rogue", level=5))
    
    data = character_sheet_to_dict(sheet)
    assert data["identity"]["name"] == "Test Hero"
    assert data["abilities"]["STR"]["score"] == 18
    
    loaded = character_sheet_from_dict(data)
    assert loaded.identity.name == "Test Hero"
    assert loaded.abilities["STR"].score == 18
    assert len(loaded.identity.classes) == 1
    assert loaded.identity.classes[0].name == "Rogue"
