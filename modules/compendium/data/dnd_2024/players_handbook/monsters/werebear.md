---name: Werebear
size: Medium
type: Medium or Small Monstrosity (Lycanthrope)
alignment: Neutral Evil
ac: '15'
hp: 97 (15d8 + 30)
speed: 30 ft., 40 ft. (boar form only)
stats:
  str: 17
  dex: 10
  con: 15
  int: 10
  wis: 11
  cha: 8
cr: 4 (XP 1,100; PB +2)
traits: []
actions:
- name: Multiattack
  description: The wereboar makes two attacks, using Javelin or Tusk in any combination.
    It can replace one attack with a Gore attack.
- name: Gore (Boar or Hybrid Form Only)
  type: save
  ability: con
  dc: 12
  on_pass: none
  on_fail: full
  damage:
  - type: piercing
    base:
      dice: 2
      die: 8
      bonus: 3
- name: Javelin (Humanoid or Hybrid Form Only)
  damage:
  - type: piercing
    base:
      dice: 3
      die: 6
      bonus: 3
  type: utility
- name: Tusk (Boar or Hybrid Form Only)
  damage:
  - type: piercing
    base:
      dice: 2
      die: 6
      bonus: 3
  - type: piercing
    base:
      dice: 2
      die: 6
      bonus: 0
  type: utility
- name: Shape-Shift
  description: "The wereboar shape-shifts into a Medium boar-humanoid hybrid or a\
    \ Small boar, or it returns to its true humanoid form. Its game statistics, other\
    \ than its size, are the same in each form. Any equipment it is wearing or carrying\
    \ isn\u2019t transformed."

---
# Werebear

*Medium or Small Monstrosity (Lycanthrope), Neutral Evil*

### Actions

**Gore (Boar or Hybrid Form Only).** Melee Attack Roll: +5, reach 5 ft. Hit: 12 (2d8 + 3) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. Constitution Saving Throw: DC 12. Failure: The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a Wereboar under the DM’s control and has 10 Hit Points. Success: The target is immune to this wereboar’s curse for 24 hours.

**Javelin (Humanoid or Hybrid Form Only).** Melee or Ranged Attack Roll: +5, reach 5 ft. or range 30/120 ft. Hit: 13 (3d6 + 3) Piercing damage.

**Tusk (Boar or Hybrid Form Only).** Melee Attack Roll: +5, reach 5 ft. Hit: 10 (2d6 + 3) Piercing damage. If the target is a Medium or smaller creature and the wereboar moved 20+ feet straight toward it immediately before the hit, the target takes an extra 7 (2d6) Piercing damage and has the Prone condition.

