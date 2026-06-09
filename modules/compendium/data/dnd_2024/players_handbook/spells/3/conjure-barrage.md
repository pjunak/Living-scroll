---name: Conjure Barrage
type: spell
level: 3
school: Conjuration
ritual: false
casting_time: Action
range: Self
components:
- V
- S
- M
material: a Melee or Ranged weapon worth at least 1 CP
duration: Instantaneous
concentration: false
classes:
- Ranger
id: spell:conjure-barrage
material_price: ''
actions:
- type: save
  ability: dex
  on_pass: half
  on_fail: full
  damage:
  - type: force
    base:
      dice: 5
      die: 8
      bonus: 0
    scaling:
      dice_per_slot: 1
      die: 8
      mode: spell_level
---
# Conjure Barrage
*3rd-Level Conjuration (Ranger)*
**Casting Time:** Action
**Range:** Self
**Components:** V, S, M (a Melee or Ranged weapon worth at least 1 CP)
**Duration:** Instantaneous

You brandish the weapon used to cast the spell and conjure similar spectral weapons (or ammunition appropriate to the weapon) that launch forward and then disappear. Each creature of your choice that you can see in a 60-foot Cone makes a Dexterity saving throw, taking 5d8 Force damage on a failed save or half as much damage on a successful one.

**Using a Higher-Level Spell Slot.** The damage increases by 1d8 for each spell slot level above 3.