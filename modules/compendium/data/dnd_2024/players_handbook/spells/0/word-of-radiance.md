---name: Word of Radiance
type: spell
level: 0
school: Evocation
ritual: false
casting_time: Action
range: Self
components:
- V
- M
material: a sunburst token
duration: Instantaneous
concentration: false
classes:
- Cleric
id: spell:word-of-radiance
material_price: ''
actions:
- type: save
  ability: con
  on_pass: none
  on_fail: full
  damage:
  - type: radiant
    base:
      dice: 1
      die: 6
      bonus: 0
    scaling:
      dice_per_slot: 1
      die: 6
      mode: character_level
---
# Word of Radiance
*Evocation Cantrip (Cleric)*
**Casting Time:** Action
**Range:** Self
**Components:** V, M (a sunburst token)
**Duration:** Instantaneous

Burning radiance erupts from you in a 5-foot Emanation. Each creature of your choice that you can see in it must succeed on a Constitution saving throw or take 1d6 Radiant damage.

**Cantrip Upgrade.** The damage increases by 1d6 when you reach levels 5 (2d6), 11 (3d6), and 17 (4d6).