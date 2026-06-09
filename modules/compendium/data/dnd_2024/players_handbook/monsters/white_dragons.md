---name: White Dragons
size: Medium
type: Medium Undead
alignment: Neutral Evil
ac: '14'
hp: 82 (11d8 + 33)
speed: 30 ft.
stats:
  str: 15
  dex: 14
  con: 16
  int: 10
  wis: 13
  cha: 15
cr: 3 (XP 700; PB +2)
traits:
- name: Resistances
  description: Necrotic
- name: Immunities
  description: Poison; Exhaustion, Poisoned
- name: Sunlight Sensitivity
  description: While in sunlight, the wight has Disadvantage on ability checks and
    attack rolls.
actions:
- name: Multiattack
  description: The wight makes two attacks, using Necrotic Sword or Necrotic Bow in
    any combination. It can replace one attack with a use of Life Drain.
- name: Necrotic Sword
  damage:
  - type: slashing
    base:
      dice: 1
      die: 8
      bonus: 2
  - type: necrotic
    base:
      dice: 1
      die: 8
      bonus: 0
  type: utility
- name: Necrotic Bow
  damage:
  - type: piercing
    base:
      dice: 1
      die: 8
      bonus: 2
  - type: necrotic
    base:
      dice: 1
      die: 8
      bonus: 0
  type: utility
- name: Life Drain
  type: save
  ability: con
  dc: 13
  on_pass: none
  on_fail: full
  damage:
  - type: necrotic
    base:
      dice: 1
      die: 8
      bonus: 2

---
# White Dragons

*Medium Undead, Neutral Evil*

### Actions

**Necrotic Sword.** Melee Attack Roll: +4, reach 5 ft. Hit: 6 (1d8 + 2) Slashing damage plus 4 (1d8) Necrotic damage.

**Necrotic Bow.** Ranged Attack Roll: +4, range 150/600 ft. Hit: 6 (1d8 + 2) Piercing damage plus 4 (1d8) Necrotic damage.

**Life Drain.** Constitution Saving Throw: DC 13, one creature within 5 feet. Failure: 6 (1d8 + 2) Necrotic damage, and the target’s Hit Point maximum decreases by an amount equal to the damage taken.

