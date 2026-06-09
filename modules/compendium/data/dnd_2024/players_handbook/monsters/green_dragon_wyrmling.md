---name: Green Dragon Wyrmling
size: Medium
type: Medium Dragon (Chromatic)
alignment: Lawful Evil
ac: '17'
hp: 38 (7d8 + 7)
speed: 30 ft., Fly 60 ft., Swim 30 ft.
stats:
  str: 15
  dex: 12
  con: 13
  int: 14
  wis: 11
  cha: 13
cr: 2 (XP 450; PB +2)
traits:
- name: Immunities
  description: Poison; Poisoned
- name: Amphibious
  description: The dragon can breathe air and water.
actions:
- name: Multiattack
  description: The dragon makes two Rend attacks.
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 1
      die: 10
      bonus: 2
  - type: poison
    base:
      dice: 1
      die: 6
      bonus: 0
  type: utility
- name: "Poison Breath (Recharge 5\u20136)"
  type: save
  ability: con
  dc: 11
  on_pass: half
  on_fail: full
  damage:
  - type: poison
    base:
      dice: 6
      die: 6
      bonus: 0

---
# Green Dragon Wyrmling

*Medium Dragon (Chromatic), Lawful Evil*

### Actions

**Rend.** Melee Attack Roll: +4, reach 5 ft. Hit: 7 (1d10 + 2) Slashing damage plus 3 (1d6) Poison damage.

**Poison Breath (Recharge 5–6).** Constitution Saving Throw: DC 11, each creature in a 15-foot Cone. Failure: 21 (6d6) Poison damage. Success: Half damage.

