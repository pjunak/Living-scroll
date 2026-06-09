---name: Blue Dragon Wyrmling
size: Medium
type: Medium Dragon (Chromatic)
alignment: Lawful Evil
ac: '17'
hp: 65 (10d8 + 20)
speed: 30 ft., Burrow 15 ft., Fly 60 ft.
stats:
  str: 17
  dex: 10
  con: 15
  int: 12
  wis: 11
  cha: 15
cr: 3 (XP 700; PB +2)
traits:
- name: Immunities
  description: Lightning
actions:
- name: Multiattack
  description: The dragon makes two Rend attacks.
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 1
      die: 10
      bonus: 3
  - type: lightning
    base:
      dice: 1
      die: 6
      bonus: 0
  type: utility
- name: "Lightning Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 12
  on_pass: half
  on_fail: full
  damage:
  - type: lightning
    base:
      dice: 6
      die: 6
      bonus: 0

---
# Blue Dragon Wyrmling

*Medium Dragon (Chromatic), Lawful Evil*

### Actions

**Rend.** Melee Attack Roll: +5, reach 5 ft. Hit: 8 (1d10 + 3) Slashing damage plus 3 (1d6) Lightning damage.

**Lightning Breath (Recharge 5–6).** Dexterity Saving Throw: DC 12, each creature in a 30-foot-long, 5-foot-wide Line. Failure: 21 (6d6) Lightning damage. Success: Half damage.

