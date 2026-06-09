---name: Phantasmal Killer
type: spell
level: 4
school: Illusion
ritual: false
casting_time: Action
range: 120 feet
components:
- V
- S
material: ''
duration: Concentration, up to 1 minute
concentration: true
classes:
- Bard
- Wizard
id: spell:phantasmal-killer
material_price: ''
actions:
- type: save
  ability: wis
  on_pass: half
  on_fail: full
  damage:
  - type: psychic
    base:
      dice: 4
      die: 10
      bonus: 0
    scaling:
      dice_per_slot: 1
      die: 10
      mode: spell_level
---
# Phantasmal Killer
*4th-Level Illusion (Bard, Wizard)*
**Casting Time:** Action
**Range:** 120 feet
**Components:** V, S
**Duration:** Concentration, up to 1 minute

You tap into the nightmares of a creature you can see within range and create an illusion of its deepest fears, visible only to that creature. The target makes a Wisdom saving throw. On a failed save, the target takes 4d10 Psychic damage and has Disadvantage on ability checks and attack rolls for the duration. On a successful save, the target takes half as much damage, and the spell ends.

For the duration, the target makes a Wisdom saving throw at the end of each of its turns. On a failed save, it takes the Psychic damage again. On a successful save, the spell ends.

**Using a Higher-Level Spell Slot.** The damage increases by 1d10 for each spell slot level above 4.