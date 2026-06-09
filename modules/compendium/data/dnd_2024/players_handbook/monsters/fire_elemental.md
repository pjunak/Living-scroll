---name: Fire Elemental
size: Huge
type: Huge Giant
alignment: Lawful Evil
ac: '18'
hp: 162 (13d12 + 78)
speed: 30 ft.
stats:
  str: 25
  dex: 9
  con: 23
  int: 10
  wis: 14
  cha: 13
cr: 9 (XP 5,000; PB +4)
traits:
- name: Immunities
  description: Fire
actions:
- name: Multiattack
  description: The giant makes two attacks, using Flame Sword or Hammer Throw in any
    combination.
- name: Flame Sword
  damage:
  - type: slashing
    base:
      dice: 4
      die: 6
      bonus: 7
  - type: fire
    base:
      dice: 3
      die: 6
      bonus: 0
  type: utility
- name: Hammer Throw
  damage:
  - type: bludgeoning
    base:
      dice: 3
      die: 10
      bonus: 7
  - type: fire
    base:
      dice: 1
      die: 8
      bonus: 0
  type: utility

---
# Fire Elemental

*Huge Giant, Lawful Evil*

### Actions

**Flame Sword.** Melee Attack Roll: +11, reach 10 ft. Hit: 21 (4d6 + 7) Slashing damage plus 10 (3d6) Fire damage.

**Hammer Throw.** Ranged Attack Roll: +11, range 60/240 ft. Hit: 23 (3d10 + 7) Bludgeoning damage plus 4 (1d8) Fire damage, and the target is pushed up to 15 feet straight away from the giant and has Disadvantage on the next attack roll it makes before the end of its next turn.

