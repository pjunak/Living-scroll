---name: Pseudodragon
size: Gargantuan
type: Gargantuan Monstrosity
alignment: Unaligned
ac: '18'
hp: 247 (15d20 + 90)
speed: 50 ft., Burrow 50 ft.
stats:
  str: 28
  dex: 7
  con: 22
  int: 1
  wis: 8
  cha: 4
cr: 15 (XP 13,000; PB +5)
traits:
- name: Tunneler
  description: The worm can burrow through solid rock at half its Burrow Speed and
    leaves a 10-foot-diameter tunnel in its wake.
actions:
- name: Multiattack
  description: The worm makes one Bite attack and one Tail Stinger attack.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 3
      die: 8
      bonus: 9
  type: utility
- name: Tail Stinger
  damage:
  - type: piercing
    base:
      dice: 2
      die: 6
      bonus: 9
  - type: poison
    base:
      dice: 10
      die: 6
      bonus: 0
  type: utility
- name: Swallow
  type: save
  ability: str
  dc: 19
  on_pass: none
  on_fail: full
  damage:
  - type: acid
    base:
      dice: 5
      die: 6
      bonus: 0

---
# Pseudodragon

*Gargantuan Monstrosity, Unaligned*

### Actions

**Bite.** Melee Attack Roll: +14, reach 10 ft. Hit: 22 (3d8 + 9) Piercing damage. If the target is a Large or smaller creature, it has the Grappled condition (escape DC 19), and it has the Restrained condition until the grapple ends.

**Tail Stinger.** Melee Attack Roll: +14, reach 10 ft. Hit: 16 (2d6 + 9) Piercing damage plus 35 (10d6) Poison damage.

**Swallow.** Strength Saving Throw: DC 19, one Large or smaller creature Grappled by the worm (it can have up to three creatures swallowed at a time). Failure: The target is swallowed by the worm, and the Grappled condition ends. A swallowed creature has the Blinded and Restrained conditions, has Total Cover against attacks and other effects outside the worm, and takes 17 (5d6) Acid damage at the start of each of the worm’s turns.

