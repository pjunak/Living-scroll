---name: Young Green Dragon
size: Large
type: Large Dragon (Chromatic)
alignment: Lawful Evil
ac: '18'
hp: 136 (16d10 + 48)
speed: 40 ft., Fly 80 ft., Swim 40 ft.
stats:
  str: 19
  dex: 12
  con: 17
  int: 16
  wis: 13
  cha: 15
cr: 8 (XP 3,900; PB +3)
traits:
- name: Immunities
  description: Poison; Poisoned
- name: Amphibious
  description: The dragon can breathe air and water.
actions:
- name: Multiattack
  description: The dragon makes three Rend attacks.
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 2
      die: 6
      bonus: 4
  - type: poison
    base:
      dice: 2
      die: 6
      bonus: 0
  type: utility
- name: "Poison Breath (Recharge 5\u20136)"
  type: save
  ability: con
  dc: 14
  on_pass: half
  on_fail: full
  damage:
  - type: poison
    base:
      dice: 12
      die: 6
      bonus: 0

---
# Young Green Dragon

*Large Dragon (Chromatic), Lawful Evil*

### Actions

**Rend.** Melee Attack Roll: +7, reach 10 ft. Hit: 11 (2d6 + 4) Slashing damage plus 7 (2d6) Poison damage.

**Poison Breath (Recharge 5–6).** Constitution Saving Throw: DC 14, each creature in a 30-foot Cone. Failure: 42 (12d6) Poison damage. Success: Half damage.

