---name: Young Red Dragon
size: Large
type: Large Dragon (Chromatic)
alignment: Chaotic Evil
ac: '18'
hp: 178 (17d10 + 85)
speed: 40 ft., Climb 40 ft., Fly 80 ft.
stats:
  str: 23
  dex: 10
  con: 21
  int: 14
  wis: 11
  cha: 19
cr: 10 (XP 5,900; PB +4)
traits:
- name: Immunities
  description: Fire
actions:
- name: Multiattack
  description: The dragon makes three Rend attacks.
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 2
      die: 6
      bonus: 6
  - type: fire
    base:
      dice: 1
      die: 6
      bonus: 0
  type: utility
- name: "Fire Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 17
  on_pass: half
  on_fail: full
  damage:
  - type: fire
    base:
      dice: 16
      die: 6
      bonus: 0

---
# Young Red Dragon

*Large Dragon (Chromatic), Chaotic Evil*

### Actions

**Rend.** Melee Attack Roll: +10, reach 10 ft. Hit: 13 (2d6 + 6) Slashing damage plus 3 (1d6) Fire damage.

**Fire Breath (Recharge 5–6).** Dexterity Saving Throw: DC 17, each creature in a 30-foot Cone. Failure: 56 (16d6) Fire damage. Success: Half damage.

