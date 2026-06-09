---name: Ankylosaurus
size: Medium
type: Medium Beast
alignment: Unaligned
ac: '12'
hp: 19 (3d8 + 6)
speed: 30 ft., Climb 30 ft.
stats:
  str: 16
  dex: 14
  con: 14
  int: 6
  wis: 12
  cha: 7
cr: 1/2 (XP 100; PB +2)
traits: []
actions:
- name: Multiattack
  description: The ape makes two Fist attacks.
- name: Fist
  damage:
  - type: bludgeoning
    base:
      dice: 1
      die: 4
      bonus: 3
  type: utility
- name: Rock (Recharge 6)
  damage:
  - type: bludgeoning
    base:
      dice: 2
      die: 6
      bonus: 3
  type: utility

---
# Ankylosaurus

*Medium Beast, Unaligned*

### Actions

**Fist.** Melee Attack Roll: +5, reach 5 ft. Hit: 5 (1d4 + 3) Bludgeoning damage.

**Rock (Recharge 6).** Ranged Attack Roll: +5, range 25/50 ft. Hit: 10 (2d6 + 3) Bludgeoning damage.

