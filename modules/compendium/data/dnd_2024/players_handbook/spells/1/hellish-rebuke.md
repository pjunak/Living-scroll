---name: Hellish Rebuke
type: spell
level: 1
school: Evocation
ritual: false
casting_time: Reaction, which you take in response to taking damage from a creature
  that you can see within 60 feet of yourself
range: 60 feet
components:
- V
- S
material: ''
duration: Instantaneous
concentration: false
classes:
- Warlock
id: spell:hellish-rebuke
material_price: ''
actions:
- type: save
  ability: dex
  on_pass: half
  on_fail: full
  damage:
  - type: fire
    base:
      dice: 2
      die: 10
      bonus: 0
    scaling:
      dice_per_slot: 1
      die: 10
      mode: spell_level
---
# Hellish Rebuke
*1st-Level Evocation (Warlock)*
**Casting Time:** Reaction, which you take in response to taking damage from a creature that you can see within 60 feet of yourself
**Range:** 60 feet
**Components:** V, S
**Duration:** Instantaneous

The creature that damaged you is momentarily surrounded by green flames. It makes a Dexterity saving throw, taking 2d10 Fire damage on a failed save or half as much damage on a successful one.

**Using a Higher-Level Spell Slot.** The damage increases by 1d10 for each spell slot level above 1.