---name: Wereboar
size: Medium
type: Medium or Small Monstrosity (Lycanthrope)
alignment: Lawful Evil
ac: '13'
hp: 60 (11d8 + 11)
speed: 30 ft., Climb 30 ft.
stats:
  str: 10
  dex: 16
  con: 12
  int: 11
  wis: 10
  cha: 8
cr: 2 (XP 450; PB +2)
traits: []
actions:
- name: Multiattack
  description: The wererat makes two attacks, using Scratch or Hand Crossbow in any
    combination. It can replace one attack with a Bite attack.
- name: Bite (Rat or Hybrid Form Only)
  type: save
  ability: con
  dc: 11
  on_pass: none
  on_fail: full
  damage:
  - type: piercing
    base:
      dice: 2
      die: 4
      bonus: 3
- name: Scratch
  damage:
  - type: slashing
    base:
      dice: 1
      die: 6
      bonus: 3
  type: utility
- name: Hand Crossbow (Humanoid or Hybrid Form Only)
  damage:
  - type: piercing
    base:
      dice: 1
      die: 6
      bonus: 3
  type: utility
- name: Shape-Shift
  description: "The wererat shape-shifts into a Medium rat-humanoid hybrid or a Small\
    \ rat, or it returns to its true humanoid form. Its game statistics, other than\
    \ its size, are the same in each form. Any equipment it is wearing or carrying\
    \ isn\u2019t transformed."

---
# Wereboar

*Medium or Small Monstrosity (Lycanthrope), Lawful Evil*

### Actions

**Bite (Rat or Hybrid Form Only).** Melee Attack Roll: +5, reach 5 ft. Hit: 8 (2d4 + 3) Piercing damage. If the target is a Humanoid, it is subjected to the following effect. Constitution Saving Throw: DC 11. Failure: The target is cursed. If the cursed target drops to 0 Hit Points, it instead becomes a Wererat under the DM’s control and has 10 Hit Points. Success: The target is immune to this wererat’s curse for 24 hours.

**Scratch.** Melee Attack Roll: +5, reach 5 ft. Hit: 6 (1d6 + 3) Slashing damage.

**Hand Crossbow (Humanoid or Hybrid Form Only).** Ranged Attack Roll: +5, range 30/120 ft. Hit: 6 (1d6 + 3) Piercing damage.

