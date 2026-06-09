---name: Spirit Naga
size: Tiny
type: Tiny Fey
alignment: Neutral Good
ac: '15'
hp: 10 (4d4)
speed: 10 ft., Fly 40 ft.
stats:
  str: 3
  dex: 18
  con: 10
  int: 14
  wis: 13
  cha: 11
cr: 1/4 (XP 50; PB +2)
traits: []
actions:
- name: Needle Sword
  damage:
  - type: piercing
    base:
      dice: 1
      die: 4
      bonus: 4
  type: utility
- name: Enchanting Bow
  description: "Ranged Attack Roll: +6, range 40/160 ft. Hit: 1 Piercing damage, and\
    \ the target has the Charmed condition until the start of the sprite\u2019s next\
    \ turn."
- name: Heart Sight
  type: save
  ability: cha
  dc: 10
  on_pass: none
  on_fail: full
- name: Invisibility
  description: The sprite casts Invisibility on itself, requiring no spell components
    and using Charisma as the spellcasting ability.

---
# Spirit Naga

*Tiny Fey, Neutral Good*

### Actions

**Needle Sword.** Melee Attack Roll: +6, reach 5 ft. Hit: 6 (1d4 + 4) Piercing damage.

**Heart Sight.** Charisma Saving Throw: DC 10, one creature within 5 feet the sprite can see (Celestials, Fiends, and Undead automatically fail the save). Failure: The sprite knows the target’s emotions and alignment.

