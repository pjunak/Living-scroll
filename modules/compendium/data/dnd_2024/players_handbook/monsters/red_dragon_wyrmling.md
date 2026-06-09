---name: Red Dragon Wyrmling
size: Medium
type: Medium Dragon (Chromatic)
alignment: Chaotic Evil
ac: '17'
hp: 75 (10d8 + 30)
speed: 30 ft., Climb 30 ft., Fly 60 ft.
stats:
  str: 19
  dex: 10
  con: 17
  int: 12
  wis: 11
  cha: 15
cr: 4 (XP 1,100; PB +2)
traits:
- name: Immunities
  description: Fire
actions:
- name: Multiattack
  description: The dragon makes two Rend attacks.
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 1
      die: 10
      bonus: 4
  - type: fire
    base:
      dice: 1
      die: 6
      bonus: 0
  type: utility
- name: "Fire Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 13
  on_pass: half
  on_fail: full
  damage:
  - type: fire
    base:
      dice: 7
      die: 6
      bonus: 0

---
# Red Dragon Wyrmling

*Medium Dragon (Chromatic), Chaotic Evil*

### Actions

**Rend.** Melee Attack Roll: +6, reach 5 ft. Hit: 9 (1d10 + 4) Slashing damage plus 3 (1d6) Fire damage.

**Fire Breath (Recharge 5–6).** Dexterity Saving Throw: DC 13, each creature in a 15-foot Cone. Failure: 24 (7d6) Fire damage. Success: Half damage.

