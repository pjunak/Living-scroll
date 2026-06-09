---name: Green Hag
size: Medium
type: Medium Aberration
alignment: Unaligned
ac: '14'
hp: 54 (12d8)
speed: 30 ft., Climb 30 ft.
stats:
  str: 14
  dex: 14
  con: 11
  int: 3
  wis: 14
  cha: 5
cr: 2 (XP 450; PB +2)
traits: []
actions:
- name: Multiattack
  description: The grick makes one Beak attack and one Tentacles attack.
- name: Beak
  damage:
  - type: piercing
    base:
      dice: 2
      die: 6
      bonus: 2
  type: utility
- name: Tentacles
  damage:
  - type: slashing
    base:
      dice: 1
      die: 10
      bonus: 2
  type: utility

---
# Green Hag

*Medium Aberration, Unaligned*

### Actions

**Beak.** Melee Attack Roll: +4, reach 5 ft. Hit: 9 (2d6 + 2) Piercing damage.

**Tentacles.** Melee Attack Roll: +4, reach 5 ft. Hit: 7 (1d10 + 2) Slashing damage. If the target is a Medium or smaller creature, it has the Grappled condition (escape DC 12) from all four tentacles.

