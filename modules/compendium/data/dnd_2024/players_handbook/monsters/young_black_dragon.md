---name: Young Black Dragon
size: Large
type: Large Dragon (Chromatic)
alignment: Chaotic Evil
ac: '18'
hp: 127 (15d10 + 45)
speed: 40 ft., Fly 80 ft., Swim 40 ft.
stats:
  str: 19
  dex: 14
  con: 17
  int: 12
  wis: 11
  cha: 15
cr: 7 (XP 2,900; PB +3)
traits:
- name: Immunities
  description: Acid
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
      die: 4
      bonus: 4
  - type: acid
    base:
      dice: 1
      die: 6
      bonus: 0
  type: utility
- name: "Acid Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 14
  on_pass: half
  on_fail: full
  damage:
  - type: acid
    base:
      dice: 14
      die: 6
      bonus: 0

---
# Young Black Dragon

*Large Dragon (Chromatic), Chaotic Evil*

### Actions

**Rend.** Melee Attack Roll: +7, reach 10 ft. Hit: 9 (2d4 + 4) Slashing damage plus 3 (1d6) Acid damage.

**Acid Breath (Recharge 5–6).** Dexterity Saving Throw: DC 14, each creature in a 30-foot-long, 5-foot-wide Line. Failure: 49 (14d6) Acid damage. Success: Half damage.

