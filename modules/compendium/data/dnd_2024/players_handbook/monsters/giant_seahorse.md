---name: Giant Seahorse
size: Large
type: Large Beast
alignment: Unaligned
ac: '15'
hp: 52 (7d10 + 14)
speed: 40 ft.
stats:
  str: 16
  dex: 13
  con: 15
  int: 1
  wis: 9
  cha: 3
cr: 3 (XP 700; PB +2)
traits: []
actions:
- name: Multiattack
  description: The scorpion makes two Claw attacks and one Sting attack.
- name: Claw
  damage:
  - type: bludgeoning
    base:
      dice: 1
      die: 6
      bonus: 3
  type: utility
- name: Sting
  damage:
  - type: piercing
    base:
      dice: 1
      die: 8
      bonus: 3
  - type: poison
    base:
      dice: 2
      die: 10
      bonus: 0
  type: utility

---
# Giant Seahorse

*Large Beast, Unaligned*

### Actions

**Claw.** Melee Attack Roll: +5, reach 5 ft. Hit: 6 (1d6 + 3) Bludgeoning damage. If the target is a Large or smaller creature, it has the Grappled condition (escape DC 13) from one of two claws.

**Sting.** Melee Attack Roll: +5, reach 5 ft. Hit: 7 (1d8 + 3) Piercing damage plus 11 (2d10) Poison damage.

