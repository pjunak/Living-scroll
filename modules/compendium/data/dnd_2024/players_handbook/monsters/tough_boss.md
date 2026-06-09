---name: Tough Boss
size: Medium
type: Medium or Small Humanoid
alignment: Neutral
ac: '16'
hp: 82 (11d8 + 33)
speed: 30 ft.
stats:
  str: 17
  dex: 14
  con: 16
  int: 11
  wis: 10
  cha: 11
cr: 4 (XP 1,100; PB +2)
traits:
- name: Pack Tactics
  description: "The tough has Advantage on an attack roll against a creature if at\
    \ least one of the tough\u2019s allies is within 5 feet of the creature and the\
    \ ally doesn\u2019t have the Incapacitated condition."
actions:
- name: Multiattack
  description: The tough makes two attacks, using Warhammer or Heavy Crossbow in any
    combination.
- name: Warhammer
  damage:
  - type: bludgeoning
    base:
      dice: 2
      die: 8
      bonus: 3
  type: utility
- name: Heavy Crossbow
  damage:
  - type: piercing
    base:
      dice: 2
      die: 10
      bonus: 2
  type: utility

---
# Tough Boss

*Medium or Small Humanoid, Neutral*

### Actions

**Warhammer.** Melee Attack Roll: +5, reach 5 ft. Hit: 12 (2d8 + 3) Bludgeoning damage. If the target is a Large or smaller creature, the tough pushes the target up to 10 feet straight away from itself.

**Heavy Crossbow.** Ranged Attack Roll: +4, range 100/400 ft. Hit: 13 (2d10 + 2) Piercing damage.

