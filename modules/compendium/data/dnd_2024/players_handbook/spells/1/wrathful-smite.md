---name: Wrathful Smite
type: spell
level: 1
school: Necromancy
ritual: false
casting_time: Bonus Action, which you take immediately after hitting a creature with
  a Melee weapon or an Unarmed Strike
range: Self
components:
- V
material: ''
duration: 1 minute
concentration: false
classes:
- Paladin
id: spell:wrathful-smite
material_price: ''
actions:
- type: save
  ability: wis
  on_pass: none
  on_fail: full
  damage:
  - type: necrotic
    base:
      dice: 1
      die: 6
      bonus: 0
    scaling:
      dice_per_slot: 1
      die: 6
      mode: spell_level
---
# Wrathful Smite
*1st-Level Necromancy (Paladin)*
**Casting Time:** Bonus Action, which you take immediately after hitting a creature with a Melee weapon or an Unarmed Strike
**Range:** Self
**Components:** V
**Duration:** 1 minute

The target takes an extra 1d6 Necrotic damage from the attack, and it must succeed on a Wisdom saving throw or have the Frightened condition until the spell ends. At the end of each of its turns, the Frightened target repeats the save, ending the spell on itself on a success.

**Using a Higher-Level Spell Slot.** The damage increases by 1d6 for each spell slot level above 1.