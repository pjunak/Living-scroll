---name: Water Elemental
size: Medium
type: Medium or Small Monstrosity (Lycanthrope)
alignment: Neutral Good
ac: '15'
hp: 135 (18d8 + 54)
speed: 30 ft., 40 ft. (bear form only), Climb 30 ft. (bear form only)
stats:
  str: 19
  dex: 10
  con: 17
  int: 11
  wis: 12
  cha: 12
cr: 5 (XP 1,800; PB +3)
traits: []
actions:
- name: Multiattack
  description: The werebear makes two attacks, using Handaxe or Rend in any combination.
    It can replace one attack with a Bite attack.
- name: Bite (Bear or Hybrid Form Only)
  type: save
  ability: con
  dc: 14
  on_pass: none
  on_fail: full
  damage:
  - type: piercing
    base:
      dice: 2
      die: 12
      bonus: 4
- name: Handaxe (Humanoid or Hybrid Form Only)
  damage:
  - type: slashing
    base:
      dice: 3
      die: 6
      bonus: 4
  type: utility
- name: Rend (Bear or Hybrid Form Only)
  damage:
  - type: slashing
    base:
      dice: 2
      die: 8
      bonus: 4
  type: utility
- name: Shape-Shift
  description: "The werebear shape-shifts into a Large bear-humanoid hybrid form or\
    \ a Large bear, or it returns to its true humanoid form. Its game statistics,\
    \ other than its size, are the same in each form. Any equipment it is wearing\
    \ or carrying isn\u2019t transformed."

---
# Water Elemental

*Medium or Small Monstrosity (Lycanthrope), Neutral Good*

### Actions

**Bite (Bear or Hybrid Form Only).** Melee Attack Roll: +7, reach 5 ft. Hit: 17 (2d12 + 4) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. Constitution Saving Throw: DC 14. Failure: The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a Werebear under the DM’s control and has 10 Hit Points. Success: The target is immune to this werebear’s curse for 24 hours.

**Handaxe (Humanoid or Hybrid Form Only).** Melee or Ranged Attack Roll: +7, reach 5 ft or range 20/60 ft. Hit: 14 (3d6 + 4) Slashing damage.

**Rend (Bear or Hybrid Form Only).** Melee Attack Roll: +7, reach 5 ft. Hit: 13 (2d8 + 4) Slashing damage.

