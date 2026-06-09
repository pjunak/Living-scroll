---name: Wererat
size: Medium
type: Medium or Small Monstrosity (Lycanthrope)
alignment: Neutral
ac: '12'
hp: 120 (16d8 + 48)
speed: 30 ft., 40 ft. (tiger form only)
stats:
  str: 17
  dex: 15
  con: 16
  int: 10
  wis: 13
  cha: 11
cr: 4 (XP 1,100; PB +2)
traits: []
actions:
- name: Multiattack
  description: The weretiger makes two attacks, using Scratch or Longbow in any combination.
    It can replace one attack with a Bite attack.
- name: Bite (Tiger or Hybrid Form Only)
  type: save
  ability: con
  dc: 13
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
- name: Prowl (Tiger or Hybrid Form Only)
  description: The weretiger moves up to its Speed without provoking Opportunity Attacks.
    At the end of this movement, the weretiger can take the Hide action.
- name: Shape-Shift
  description: "The weretiger shape-shifts into a Large tiger-humanoid hybrid or a\
    \ Large tiger, or it returns to its true humanoid form. Its game statistics, other\
    \ than its size, are the same in each form. Any equipment it is wearing or carrying\
    \ isn\u2019t transformed."

---
# Wererat

*Medium or Small Monstrosity (Lycanthrope), Neutral*

### Actions

**Bite (Tiger or Hybrid Form Only).** Melee Attack Roll: +5, reach 5 ft. Hit: 12 (2d8 + 3) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. Constitution Saving Throw: DC 13. Failure: The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a Weretiger under the DM’s control and has 10 Hit Points. Success: The target is immune to this weretiger’s curse for 24 hours.

**Scratch.** Melee Attack Roll: +5, reach 5 ft. Hit: 10 (2d6 + 3) Slashing damage.

**Longbow (Humanoid or Hybrid Form Only).** Ranged Attack Roll: +4, range 150/600 ft. Hit: 11 (2d8 + 2) Piercing damage.

