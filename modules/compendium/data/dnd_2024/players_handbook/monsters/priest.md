---name: Priest
size: Tiny
type: Tiny Dragon
alignment: Neutral Good
ac: '14'
hp: 10 (3d4 + 3)
speed: 15 ft., Fly 60 ft.
stats:
  str: 6
  dex: 15
  con: 13
  int: 10
  wis: 12
  cha: 10
cr: 1/4 (XP 50; PB +2)
traits:
- name: Magic Resistance
  description: The pseudodragon has Advantage on saving throws against spells and
    other magical effects.
actions:
- name: Multiattack
  description: The pseudodragon makes two Bite attacks.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 1
      die: 4
      bonus: 2
  type: utility
- name: Sting
  type: save
  ability: con
  dc: 12
  on_pass: none
  on_fail: full
  damage:
  - type: poison
    base:
      dice: 2
      die: 4
      bonus: 0

---
# Priest

*Tiny Dragon, Neutral Good*

### Actions

**Bite.** Melee Attack Roll: +4, reach 5 ft. Hit: 4 (1d4 + 2) Piercing damage.

**Sting.** Constitution Saving Throw: DC 12, one creature the pseudodragon can see within 5 feet. Failure: 5 (2d4) Poison damage, and the target has the Poisoned condition for 1 hour. While Poisoned, the target also has the Unconscious condition, which ends early if the target takes damage or a creature within 5 feet of it takes an action to wake it.

