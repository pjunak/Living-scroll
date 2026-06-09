---name: Air Elemental
size: Large
type: Elemental
alignment: Neutral
ac: 15
hp: 90 (12d10 + 24)
speed: 10 ft., Fly 90 ft. (hover)
stats:
  str: 14
  dex: 20
  con: 14
  int: 6
  wis: 10
  cha: 6
cr: 5
traits:
- name: Air Form
  description: "The elemental can enter a creature\u2019s space and stop there. It\
    \ can move through a space as narrow as 1 inch without expending extra movement\
    \ to do so."
- name: Resistances
  description: Bludgeoning, Lightning, Piercing, Slashing
- name: Immunities
  description: Poison, Thunder; Exhaustion, Grappled, Paralyzed, Petrified, Poisoned,
    Prone, Restrained, Unconscious
actions:
- name: Multiattack
  description: The elemental makes two Thunderous Slam attacks.
- name: Thunderous Slam
  damage:
  - type: thunder
    base:
      dice: 2
      die: 8
      bonus: 5
  type: utility
- name: "Whirlwind (Recharge 4\u20136)"
  type: save
  ability: str
  dc: 13
  on_pass: half
  on_fail: full
  damage:
  - type: thunder
    base:
      dice: 4
      die: 10
      bonus: 2

---
# Air Elemental

A funneling cloud of air that turns into a whirlwind, the air elemental is a force of living atmosphere.

### Actions

**Thunderous Slam.** Melee Attack Roll: +8, reach 10 ft. Hit: 14 (2d8 + 5) Thunder damage.

**Whirlwind (Recharge 4–6).** Strength Saving Throw: DC 13, one Medium or smaller creature in the elemental’s space. Failure: 24 (4d10 + 2) Thunder damage, and the target is pushed up to 20 feet straight away from the elemental and has the Prone condition. Success: Half damage only.

