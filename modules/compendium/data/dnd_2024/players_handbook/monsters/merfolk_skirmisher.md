---name: Merfolk Skirmisher
size: Large
type: Large Monstrosity
alignment: Chaotic Evil
ac: '13'
hp: 45 (6d10 + 12)
speed: 10 ft., Swim 40 ft.
stats:
  str: 18
  dex: 15
  con: 15
  int: 8
  wis: 10
  cha: 9
cr: 2 (XP 450; PB +2)
traits:
- name: Amphibious
  description: The merrow can breathe air and water.
actions:
- name: Multiattack
  description: The merrow makes two attacks, using Bite, Claw, or Harpoon in any combination.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 1
      die: 4
      bonus: 4
  type: utility
- name: Claw
  damage:
  - type: slashing
    base:
      dice: 2
      die: 4
      bonus: 4
  type: utility
- name: Harpoon
  damage:
  - type: piercing
    base:
      dice: 2
      die: 6
      bonus: 4
  type: utility

---
# Merfolk Skirmisher

*Large Monstrosity, Chaotic Evil*

### Actions

**Bite.** Melee Attack Roll: +6, reach 5 ft. Hit: 6 (1d4 + 4) Piercing damage, and the target has the Poisoned condition until the end of the merrow’s next turn.

**Claw.** Melee Attack Roll: +6, reach 5 ft. Hit: 9 (2d4 + 4) Slashing damage.

**Harpoon.** Melee or Ranged Attack Roll: +6, reach 5 ft. or range 20/60 ft. Hit: 11 (2d6 + 4) Piercing damage. If the target is a Large or smaller creature, the merrow pulls the target up to 15 feet straight toward itself.

