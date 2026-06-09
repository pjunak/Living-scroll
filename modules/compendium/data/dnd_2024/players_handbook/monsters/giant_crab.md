---name: Giant Crab
size: Huge
type: Huge Beast
alignment: Unaligned
ac: '14'
hp: 85 (9d12 + 27)
speed: 30 ft., Swim 50 ft.
stats:
  str: 21
  dex: 9
  con: 17
  int: 2
  wis: 10
  cha: 7
cr: 5 (XP 1,800; PB +3)
traits:
- name: Hold Breath
  description: The crocodile can hold its breath for 1 hour.
actions:
- name: Multiattack
  description: The crocodile makes one Bite attack and one Tail attack.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 3
      die: 10
      bonus: 5
  type: utility
- name: Tail
  damage:
  - type: bludgeoning
    base:
      dice: 3
      die: 8
      bonus: 5
  type: utility

---
# Giant Crab

*Huge Beast, Unaligned*

### Actions

**Bite.** Melee Attack Roll: +8, reach 5 ft. Hit: 21 (3d10 + 5) Piercing damage. If the target is a Large or smaller creature, it has the Grappled condition (escape DC 15). While Grappled, the target has the Restrained condition and can’t be targeted by the crocodile’s Tail.

**Tail.** Melee Attack Roll: +8, reach 10 ft. Hit: 18 (3d8 + 5) Bludgeoning damage. If the target is a Large or smaller creature, it has the Prone condition.

