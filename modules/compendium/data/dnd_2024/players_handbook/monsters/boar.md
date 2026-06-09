---name: Boar
size: Large
type: Large Beast
alignment: Unaligned
ac: '11'
hp: 22 (3d10 + 6)
speed: 40 ft., Climb 30 ft.
stats:
  str: 17
  dex: 12
  con: 15
  int: 2
  wis: 13
  cha: 7
cr: 1 (XP 200; PB +2)
traits: []
actions:
- name: Multiattack
  description: The bear makes one Bite attack and one Claw attack.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 1
      die: 8
      bonus: 3
  type: utility
- name: Claw
  damage:
  - type: slashing
    base:
      dice: 1
      die: 4
      bonus: 3
  type: utility

---
# Boar

*Large Beast, Unaligned*

### Actions

**Bite.** Melee Attack Roll: +5, reach 5 ft. Hit: 7 (1d8 + 3) Piercing damage.

**Claw.** Melee Attack Roll: +5, reach 5 ft. Hit: 5 (1d4 + 3) Slashing damage. If the target is a Large or smaller creature, it has the Prone condition.

