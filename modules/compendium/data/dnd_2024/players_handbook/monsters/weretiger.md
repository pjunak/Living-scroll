---name: Weretiger
size: Medium
type: Medium or Small Monstrosity (Lycanthrope)
alignment: Chaotic Evil
ac: '15'
hp: 71 (11d8 + 22)
speed: 30 ft., 40 ft. (wolf form only)
stats:
  str: 16
  dex: 14
  con: 14
  int: 10
  wis: 11
  cha: 10
cr: 3 (XP 700; PB +2)
traits:
- name: Pack Tactics
  description: "The werewolf has Advantage on an attack roll against a creature if\
    \ at least one of the werewolf\u2019s allies is within 5 feet of the creature\
    \ and the ally doesn\u2019t have the Incapacitated condition."
actions:
- name: Multiattack
  description: The werewolf makes two attacks, using Scratch or Longbow in any combination.
    It can replace one attack with a Bite attack.
- name: Bite (Wolf or Hybrid Form Only)
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
- name: Scratch
  damage:
  - type: slashing
    base:
      dice: 2
      die: 6
      bonus: 3
  type: utility
- name: Longbow (Humanoid or Hybrid Form Only)
  damage:
  - type: piercing
    base:
      dice: 2
      die: 8
      bonus: 2
  type: utility
- name: Shape-Shift
  description: "The werewolf shape-shifts into a Large wolf-humanoid hybrid or a Medium\
    \ wolf, or it returns to its true humanoid form. Its game statistics, other than\
    \ its size, are the same in each form. Any equipment it is wearing or carrying\
    \ isn\u2019t transformed."

---
# Weretiger

*Medium or Small Monstrosity (Lycanthrope), Chaotic Evil*

### Actions

**Bite (Wolf or Hybrid Form Only).** Melee Attack Roll: +5, reach 5 ft. Hit: 12 (2d8 + 3) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. Constitution Saving Throw: DC 12. Failure: The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a Werewolf under the DM’s control and has 10 Hit Points. Success: The target is immune to this werewolf’s curse for 24 hours.

**Scratch.** Melee Attack Roll: +5, reach 5 ft. Hit: 10 (2d6 + 3) Slashing damage.

**Longbow (Humanoid or Hybrid Form Only).** Ranged Attack Roll: +4, range 150/600 ft. Hit: 11 (2d8 + 2) Piercing damage.

