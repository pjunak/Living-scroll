---name: Adult White Dragon
size: Huge
type: Huge Dragon (Chromatic)
alignment: Chaotic Evil
ac: '18'
hp: 200 (16d12 + 96)
speed: 40 ft., Burrow 30 ft., Fly 80 ft., Swim 40 ft.
stats:
  str: 22
  dex: 10
  con: 22
  int: 8
  wis: 12
  cha: 12
cr: 13 (XP 10,000, or 11,500 in lair; PB +5)
traits:
- name: Immunities
  description: Cold
- name: Ice Walk
  description: "The dragon can move across and climb icy surfaces without needing\
    \ to make an ability check. Additionally, Difficult Terrain composed of ice or\
    \ snow doesn\u2019t cost it extra movement."
- name: Legendary Resistance (3/Day, or 4/Day in Lair)
  description: If the dragon fails a saving throw, it can choose to succeed instead.
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
  - type: cold
    base:
      dice: 1
      die: 8
      bonus: 0
  type: utility
- name: "Cold Breath (Recharge 5\u20136)"
  type: save
  ability: con
  dc: 19
  on_pass: half
  on_fail: full
  damage:
  - type: cold
    base:
      dice: 12
      die: 8
      bonus: 0
- name: Freezing Burst
  type: save
  ability: con
  dc: 14
  on_pass: none
  on_fail: full
  damage:
  - type: cold
    base:
      dice: 2
      die: 6
      bonus: 0
- name: Frightful Presence
  description: "The dragon casts Fear, requiring no Material components and using\
    \ Charisma as the spellcasting ability (spell save DC 14). The dragon can\u2019\
    t take this action again until the start of its next turn."
- name: Pounce
  description: The dragon moves up to half its Speed, and it makes one Rend attack.

---
# Adult White Dragon

*Huge Dragon (Chromatic), Chaotic Evil*

### Actions

**Rend.** Melee Attack Roll: +11, reach 10 ft. Hit: 13 (2d6 + 6) Slashing damage plus 4 (1d8) Cold damage.

**Cold Breath (Recharge 5–6).** Constitution Saving Throw: DC 19, each creature in a 60-foot Cone. Failure: 54 (12d8) Cold damage. Success: Half damage.

**Freezing Burst.** Constitution Saving Throw: DC 14, each creature in a 30-foot-radius Sphere centered on a point the dragon can see within 120 feet. Failure: 7 (2d6) Cold damage, and the target’s Speed is 0 until the end of the target’s next turn. Failure or Success: The dragon can’t take this action again until the start of its next turn.

