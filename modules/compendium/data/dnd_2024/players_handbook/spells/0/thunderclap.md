---name: Thunderclap
type: spell
level: 0
school: Evocation
ritual: false
casting_time: Action
range: Self
components:
- S
material: ''
duration: Instantaneous
concentration: false
classes:
- Artificer
- Bard
- Druid
- Sorcerer
- Warlock
- Wizard
id: spell:thunderclap
material_price: ''
actions:
- type: save
  ability: con
  on_pass: none
  on_fail: full
  damage:
  - type: thunder
    base:
      dice: 1
      die: 6
      bonus: 0
    scaling:
      dice_per_slot: 1
      die: 6
      mode: character_level
---
# Thunderclap
*Evocation Cantrip (Artificer, Bard, Druid, Sorcerer, Warlock, Wizard)*
**Casting Time:** Action
**Range:** Self
**Components:** S
**Duration:** Instantaneous

Each creature in a 5-foot Emanation originating from you must succeed on a Constitution saving throw or take 1d6 Thunder damage. The spell’s thunderous sound can be heard up to 100 feet away.

**Cantrip Upgrade.** The damage increases by 1d6 when you reach levels 5 (2d6), 11 (3d6), and 17 (4d6).