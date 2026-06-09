---name: Inflict Wounds
type: spell
level: 1
school: Necromancy
ritual: false
casting_time: Action
range: Touch
components:
- V
- S
material: ''
duration: Instantaneous
concentration: false
classes:
- Cleric
id: spell:inflict-wounds
material_price: ''
actions:
- type: save
  ability: con
  on_pass: half
  on_fail: full
  damage:
  - type: necrotic
    base:
      dice: 2
      die: 10
      bonus: 0
    scaling:
      dice_per_slot: 1
      die: 10
      mode: spell_level
---
# Inflict Wounds
*1st-Level Necromancy (Cleric)*
**Casting Time:** Action
**Range:** Touch
**Components:** V, S
**Duration:** Instantaneous

A creature you touch makes a Constitution saving throw, taking 2d10 Necrotic damage on a failed save or half as much damage on a successful one.

**Using a Higher-Level Spell Slot.** The damage increases by 1d10 for each spell slot level above 1.