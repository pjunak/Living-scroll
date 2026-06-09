---name: Young Blue Dragon
size: Large
type: Large Dragon (Chromatic)
alignment: Lawful Evil
ac: '18'
hp: 152 (16d10 + 64)
speed: 40 ft., Burrow 20 ft., Fly 80 ft.
stats:
  str: 21
  dex: 10
  con: 19
  int: 14
  wis: 13
  cha: 17
cr: 9 (XP 5,000; PB +4)
traits:
- name: Immunities
  description: Lightning
actions:
- name: Multiattack
  description: The dragon makes three Rend attacks.
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 2
      die: 6
      bonus: 5
  - type: lightning
    base:
      dice: 1
      die: 10
      bonus: 0
  type: utility
- name: "Lightning Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 16
  on_pass: half
  on_fail: full
  damage:
  - type: lightning
    base:
      dice: 10
      die: 10
      bonus: 0

---
# Young Blue Dragon

*Large Dragon (Chromatic), Lawful Evil*

### Actions

**Rend.** Melee Attack Roll: +9, reach 10 ft. Hit: 12 (2d6 + 5) Slashing damage plus 5 (1d10) Lightning damage.

**Lightning Breath (Recharge 5–6).** Dexterity Saving Throw: DC 16, each creature in a 60-foot-long, 5-foot-wide Line. Failure: 55 (10d10) Lightning damage. Success: Half damage.

