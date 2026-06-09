---name: Giant Spider
size: Large
type: Large Beast
alignment: Unaligned
ac: '11'
hp: 39 (6d10 + 6)
speed: 30 ft., Swim 30 ft.
stats:
  str: 15
  dex: 13
  con: 13
  int: 2
  wis: 10
  cha: 3
cr: 1 (XP 200; PB +2)
traits:
- name: Amphibious
  description: The toad can breathe air and water.
- name: Standing Leap
  description: "The toad\u2019s Long Jump is up to 20 feet and its High Jump is up\
    \ to 10 feet with or without a running start."
actions:
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 1
      die: 6
      bonus: 2
  - type: poison
    base:
      dice: 2
      die: 4
      bonus: 0
  type: utility
- name: Swallow
  damage:
  - type: acid
    base:
      dice: 3
      die: 6
      bonus: 0
  type: utility

---
# Giant Spider

*Large Beast, Unaligned*

### Actions

**Bite.** Melee Attack Roll: +4, reach 5 ft. Hit: 5 (1d6 + 2) Piercing damage plus 5 (2d4) Poison damage. If the target is a Medium or smaller creature, it has the Grappled condition (escape DC 12).

**Swallow.** The toad swallows a Medium or smaller target it is grappling. While swallowed, the target isn’t Grappled but has the Blinded and Restrained conditions, and it has Total Cover against attacks and other effects outside the toad. In addition, the target takes 10 (3d6) Acid damage at the end of each of the toad’s turns. The toad can have only one target swallowed at a time, and it can’t use Bite while it has a swallowed target. If the toad dies, a swallowed creature is no longer Restrained and can escape from the corpse using 5 feet of movement, exiting with the Prone condition.

