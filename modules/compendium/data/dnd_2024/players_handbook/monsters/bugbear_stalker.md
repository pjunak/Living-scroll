---name: Bugbear Stalker
size: Medium
type: Medium Fey (Goblinoid)
alignment: Chaotic Evil
ac: '15'
hp: 65 (10d8 + 20)
speed: 30 ft.
stats:
  str: 17
  dex: 14
  con: 14
  int: 11
  wis: 12
  cha: 11
cr: 3 (XP 700; PB +2)
traits:
- name: Abduct
  description: "The bugbear needn\u2019t spend extra movement to move a creature it\
    \ is grappling."
actions:
- name: Multiattack
  description: The bugbear makes two Javelin or Morningstar attacks.
- name: Javelin
  damage:
  - type: piercing
    base:
      dice: 3
      die: 6
      bonus: 3
  type: utility
- name: Morningstar
  damage:
  - type: piercing
    base:
      dice: 2
      die: 8
      bonus: 3
  type: utility
- name: Quick Grapple
  type: save
  ability: dex
  dc: 13
  on_pass: none
  on_fail: full

---
# Bugbear Stalker

*Medium Fey (Goblinoid), Chaotic Evil*

### Actions

**Javelin.** Melee or Ranged Attack Roll: +5, reach 10 ft. or range 30/120 ft. Hit: 13 (3d6 + 3) Piercing damage.

**Morningstar.** Melee Attack Roll: +5 (with Advantage if the target is Grappled by the bugbear), reach 10 ft. Hit: 12 (2d8 + 3) Piercing damage.

**Quick Grapple.** Dexterity Saving Throw: DC 13, one Medium or smaller creature the bugbear can see within 10 feet. Failure: The target has the Grappled condition (escape DC 13).

