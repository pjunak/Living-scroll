---name: Ancient White Dragon
size: Gargantuan
type: Gargantuan Dragon (Chromatic)
alignment: Chaotic Evil
ac: '20'
hp: 333 (18d20 + 144)
speed: 40 ft., Burrow 40 ft., Fly 80 ft., Swim 40 ft.
stats:
  str: 26
  dex: 10
  con: 26
  int: 10
  wis: 13
  cha: 18
cr: 20 (XP 25,000, or 33,000 in lair; PB +6)
traits:
- name: Immunities
  description: Cold
- name: Ice Walk
  description: "The dragon can move across and climb icy surfaces without needing\
    \ to make an ability check. Additionally, Difficult Terrain composed of ice or\
    \ snow doesn\u2019t cost it extra movement."
- name: Legendary Resistance (4/Day, or 5/Day in Lair)
  description: If the dragon fails a saving throw, it can choose to succeed instead.
actions:
- name: Multiattack
  description: The dragon makes three Rend attacks.
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 2
      die: 8
      bonus: 8
  - type: cold
    base:
      dice: 2
      die: 6
      bonus: 0
  type: utility
- name: "Cold Breath (Recharge 5\u20136)"
  type: save
  ability: con
  dc: 22
  on_pass: half
  on_fail: full
  damage:
  - type: cold
    base:
      dice: 14
      die: 8
      bonus: 0
- name: Freezing Burst
  type: save
  ability: con
  dc: 20
  on_pass: none
  on_fail: full
  damage:
  - type: cold
    base:
      dice: 4
      die: 6
      bonus: 0
- name: Frightful Presence
  description: "The dragon casts Fear, requiring no Material components and using\
    \ Charisma as the spellcasting ability (spell save DC 18). The dragon can\u2019\
    t take this action again until the start of its next turn."
- name: Pounce
  description: The dragon moves up to half its Speed, and it makes one Rend attack.

---
# Ancient White Dragon

*Gargantuan Dragon (Chromatic), Chaotic Evil*

### Actions

**Rend.** Melee Attack Roll: +14, reach 15 ft. Hit: 17 (2d8 + 8) Slashing damage plus 7 (2d6) Cold damage.

**Cold Breath (Recharge 5–6).** Constitution Saving Throw: DC 22, each creature in a 90-foot Cone. Failure: 63 (14d8) Cold damage. Success: Half damage.

**Freezing Burst.** Constitution Saving Throw: DC 20, each creature in a 30-foot-radius Sphere centered on a point the dragon can see within 120 feet. Failure: 14 (4d6) Cold damage, and the target’s Speed is 0 until the end of the target’s next turn. Failure or Success: The dragon can’t take this action again until the start of its next turn.

