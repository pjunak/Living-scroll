---name: Shatter
type: spell
level: 2
school: Evocation
ritual: false
casting_time: Action
range: 60 feet
components:
- V
- S
- M
material: a chip of mica
duration: Instantaneous
concentration: false
classes:
- Bard
- Sorcerer
- Wizard
id: spell:shatter
material_price: ''
actions:
- type: save
  ability: con
  on_pass: half
  on_fail: full
  damage:
  - type: thunder
    base:
      dice: 3
      die: 8
      bonus: 0
    scaling:
      dice_per_slot: 1
      die: 8
      mode: spell_level
---
# Shatter
*2nd-Level Evocation (Bard, Sorcerer, Wizard)*
**Casting Time:** Action
**Range:** 60 feet
**Components:** V, S, M (a chip of mica)
**Duration:** Instantaneous

A loud noise erupts from a point of your choice within range. Each creature in a 10-foot-radius Sphere centered there makes a Constitution saving throw, taking 3d8 Thunder damage on a failed save or half as much damage on a successful one. A Construct has Disadvantage on the save.

A nonmagical object that isn’t being worn or carried also takes the damage if it’s in the spell’s area.

**Using a Higher-Level Spell Slot.** The damage increases by 1d8 for each spell slot level above 2.