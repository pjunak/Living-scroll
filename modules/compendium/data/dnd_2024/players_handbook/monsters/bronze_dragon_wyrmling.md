---name: Bronze Dragon Wyrmling
size: Medium
type: Medium Dragon (Metallic)
alignment: Lawful Good
ac: '15'
hp: 39 (6d8 + 12)
speed: 30 ft., Fly 60 ft., Swim 30 ft.
stats:
  str: 17
  dex: 10
  con: 15
  int: 12
  wis: 11
  cha: 15
cr: 2 (XP 450; PB +2)
traits:
- name: Immunities
  description: Lightning
- name: Amphibious
  description: The dragon can breathe air and water.
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
      dice: 3
      die: 10
      bonus: 0
- name: Repulsion Breath
  type: save
  ability: str
  dc: 12
  on_pass: none
  on_fail: full

---
# Bronze Dragon Wyrmling

*Medium Dragon (Metallic), Lawful Good*

### Actions

**Rend.** Melee Attack Roll: +5, reach 5 ft. Hit: 8 (1d10 + 3) Slashing damage.

**Lightning Breath (Recharge 5–6).** Dexterity Saving Throw: DC 12, each creature in a 40-foot-long, 5-foot-wide Line. Failure: 16 (3d10) Lightning damage. Success: Half damage.

**Repulsion Breath.** Strength Saving Throw: DC 12, each creature in a 30-foot Cone. Failure: The target is pushed up to 30 feet straight away from the dragon and has the Prone condition.

