---name: Giant Centipede
size: Huge
type: Huge Beast
alignment: Unaligned
ac: '12'
hp: 60 (8d12 + 8)
speed: 30 ft., Swim 30 ft.
stats:
  str: 19
  dex: 14
  con: 12
  int: 1
  wis: 10
  cha: 3
cr: 2 (XP 450; PB +2)
traits: []
actions:
- name: Multiattack
  description: The snake makes one Bite attack and uses Constrict.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 2
      die: 6
      bonus: 4
  type: utility
- name: Constrict
  type: save
  ability: str
  dc: 14
  on_pass: none
  on_fail: full
  damage:
  - type: bludgeoning
    base:
      dice: 2
      die: 8
      bonus: 4

---
# Giant Centipede

*Huge Beast, Unaligned*

### Actions

**Bite.** Melee Attack Roll: +6, reach 10 ft. Hit: 11 (2d6 + 4) Piercing damage.

**Constrict.** Strength Saving Throw: DC 14, one Large or smaller creature the snake can see within 10 feet. Failure: 13 (2d8 + 4) Bludgeoning damage, and the target has the Grappled condition (escape DC 14).

