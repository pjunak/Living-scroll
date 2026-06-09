---name: Cat
size: Large
type: Large Beast
alignment: Unaligned
ac: '13'
hp: 13 (2d10 + 2)
speed: 30 ft., Swim 30 ft.
stats:
  str: 15
  dex: 14
  con: 12
  int: 1
  wis: 10
  cha: 3
cr: 1/4 (XP 50; PB +2)
traits: []
actions:
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 1
      die: 8
      bonus: 2
  type: utility
- name: Constrict
  type: save
  ability: str
  dc: 12
  on_pass: none
  on_fail: full
  damage:
  - type: bludgeoning
    base:
      dice: 3
      die: 4
      bonus: 0

---
# Cat

*Large Beast, Unaligned*

### Actions

**Bite.** Melee Attack Roll: +4, reach 5 ft. Hit: 6 (1d8 + 2) Piercing damage.

**Constrict.** Strength Saving Throw: DC 12, one Medium or smaller creature the snake can see within 5 feet. Failure: 7 (3d4) Bludgeoning damage, and the target has the Grappled condition (escape DC 12).

