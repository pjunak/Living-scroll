---name: Young White Dragon
size: Large
type: Large Dragon (Chromatic)
alignment: Chaotic Evil
ac: '17'
hp: 123 (13d10 + 52)
speed: 40 ft., Burrow 20 ft., Fly 80 ft., Swim 40 ft.
stats:
  str: 18
  dex: 10
  con: 18
  int: 6
  wis: 11
  cha: 12
cr: 6 (2,300 XP; PB +3)
traits:
- name: Immunities
  description: Cold
- name: Ice Walk
  description: "The dragon can move across and climb icy surfaces without needing\
    \ to make an ability check. Additionally, Difficult Terrain composed of ice or\
    \ snow doesn\u2019t cost it extra movement."
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
  - type: cold
    base:
      dice: 1
      die: 4
      bonus: 0
  type: utility
- name: "Cold Breath (Recharge 5\u20136)"
  type: save
  ability: con
  dc: 15
  on_pass: half
  on_fail: full
  damage:
  - type: cold
    base:
      dice: 9
      die: 8
      bonus: 0

---
# Young White Dragon

*Large Dragon (Chromatic), Chaotic Evil*

### Actions

**Rend.** Melee Attack Roll: +7, reach 10 ft. Hit: 9 (2d4 + 4) Slashing damage plus 2 (1d4) Cold damage.

**Cold Breath (Recharge 5–6).** Constitution Saving Throw: DC 15, each creature in a 30-foot Cone. Failure: 40 (9d8) Cold damage. Success: Half damage.

