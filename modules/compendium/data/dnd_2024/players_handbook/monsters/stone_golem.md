---name: Stone Golem
size: Huge
type: Huge Giant
alignment: Chaotic Good
ac: '16'
hp: 230 (20d12 + 100)
speed: 50 ft., Fly 25 ft. (hover), Swim 50 ft.
stats:
  str: 29
  dex: 14
  con: 20
  int: 16
  wis: 20
  cha: 18
cr: 13 (XP 10,000; PB +5)
traits:
- name: Resistances
  description: Cold
- name: Immunities
  description: Lightning, Thunder
- name: Amphibious
  description: The giant can breathe air and water.
actions:
- name: Multiattack
  description: The giant makes two attacks, using Storm Sword or Thunderbolt in any
    combination.
- name: Storm Sword
  damage:
  - type: slashing
    base:
      dice: 4
      die: 6
      bonus: 9
  - type: lightning
    base:
      dice: 3
      die: 8
      bonus: 0
  type: utility
- name: Thunderbolt
  damage:
  - type: lightning
    base:
      dice: 2
      die: 12
      bonus: 9
  type: utility
- name: "Lightning Storm (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 18
  on_pass: half
  on_fail: full
  damage:
  - type: lightning
    base:
      dice: 10
      die: 10
      bonus: 0
- name: Spellcasting
  description: 'The giant casts one of the following spells, requiring no Material
    components and using Wisdom as the spellcasting ability (spell save DC 18):'
- name: 'At Will:'
  description: Detect Magic, Light
- name: '1/Day:'
  description: Control Weather

---
# Stone Golem

*Huge Giant, Chaotic Good*

### Actions

**Storm Sword.** Melee Attack Roll: +14, reach 10 ft. Hit: 23 (4d6 + 9) Slashing damage plus 13 (3d8) Lightning damage.

**Thunderbolt.** Ranged Attack Roll: +14, range 500 ft. Hit: 22 (2d12 + 9) Lightning damage, and the target has the Blinded and Deafened conditions until the start of the giant’s next turn.

**Lightning Storm (Recharge 5–6).** Dexterity Saving Throw: DC 18, each creature in a 10-foot-radius, 40-foot-high Cylinder originating from a point the giant can see within 500 feet. Failure: 55 (10d10) Lightning damage. Success: Half damage.

