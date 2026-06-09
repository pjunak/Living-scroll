---name: Marilith
size: Medium
type: Medium Monstrosity
alignment: Lawful Evil
ac: '15'
hp: 127 (17d8 + 51)
speed: 30 ft.
stats:
  str: 10
  dex: 17
  con: 16
  int: 12
  wis: 13
  cha: 15
cr: 6 (XP 2,300; PB +3)
traits: []
actions:
- name: Multiattack
  description: The medusa makes two Claw attacks and one Snake Hair attack, or it
    makes three Poison Ray attacks.
- name: Claw
  damage:
  - type: slashing
    base:
      dice: 2
      die: 6
      bonus: 3
  type: utility
- name: Snake Hair
  damage:
  - type: piercing
    base:
      dice: 1
      die: 4
      bonus: 3
  - type: poison
    base:
      dice: 4
      die: 6
      bonus: 0
  type: utility
- name: Poison Ray
  damage:
  - type: poison
    base:
      dice: 2
      die: 8
      bonus: 2
  type: utility
- name: Petrifying Gaze (Recharge
  type: save
  ability: con
  dc: 13
  on_pass: none
  on_fail: full

---
# Marilith

*Medium Monstrosity, Lawful Evil*

### Actions

**Claw.** Melee Attack Roll: +6, reach 5 ft. Hit: 10 (2d6 + 3) Slashing damage.

**Snake Hair.** Melee Attack Roll: +6, reach 5 ft. Hit: 5 (1d4 + 3) Piercing damage plus 14 (4d6) Poison damage.

**Poison Ray.** Ranged Attack Roll: +5, range 150 ft. Hit: 11 (2d8 + 2) Poison damage.

**Petrifying Gaze (Recharge.** 5–6). Constitution Saving Throw: DC 13, each creature in a 30-foot Cone. If the medusa sees its reflection in the Cone, the medusa must make this save. First Failure: The target has the Restrained condition and repeats the save at the end of its next turn if it is still Restrained, ending the effect on itself on a success. Second Failure: The target has the Petrified condition instead of the Restrained condition.

