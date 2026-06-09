---name: Harpy
size: Medium
type: Medium Fiend
alignment: Lawful Evil
ac: '15'
hp: 58 (9d8 + 18)
speed: 50 ft.
stats:
  str: 17
  dex: 12
  con: 14
  int: 6
  wis: 13
  cha: 6
cr: 3 (XP 700; PB +2)
traits:
- name: Immunities
  description: Fire
- name: Pack Tactics
  description: "The hound has Advantage on an attack roll against a creature if at\
    \ least one of the hound\u2019s allies is within 5 feet of the creature and the\
    \ ally doesn\u2019t have the Incapacitated condition."
actions:
- name: Multiattack
  description: The hound makes two Bite attacks.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 1
      die: 8
      bonus: 3
  - type: fire
    base:
      dice: 1
      die: 6
      bonus: 0
  type: utility
- name: "Fire Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 12
  on_pass: half
  on_fail: full
  damage:
  - type: fire
    base:
      dice: 5
      die: 6
      bonus: 0

---
# Harpy

*Medium Fiend, Lawful Evil*

### Actions

**Bite.** Melee Attack Roll: +5, reach 5 ft. Hit: 7 (1d8 + 3) Piercing damage plus 3 (1d6) Fire damage.

**Fire Breath (Recharge 5–6).** Dexterity Saving Throw: DC 12, each creature in a 15-foot Cone. Failure: 17 (5d6) Fire damage. Success: Half damage.

