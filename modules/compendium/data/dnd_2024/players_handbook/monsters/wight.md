---name: Wight
size: Tiny
type: Tiny Undead
alignment: Chaotic Evil
ac: '19'
hp: 27 (11d4)
speed: 5 ft., Fly 50 ft. (hover)
stats:
  str: 1
  dex: 28
  con: 10
  int: 13
  wis: 14
  cha: 11
cr: 2 (XP 450; PB +2)
traits:
- name: Resistances
  description: Acid, Bludgeoning, Cold, Fire, Necrotic, Piercing, Slashing
- name: Immunities
  description: Lightning, Poison; Exhaustion, Grappled, Paralyzed, Petrified, Poisoned,
    Prone, Restrained, Unconscious
- name: Ephemeral
  description: "The wisp can\u2019t wear or carry anything."
- name: Illumination
  description: The wisp sheds Bright Light in a 20-foot radius and Dim Light for an
    additional 20 feet.
- name: Incorporeal Movement
  description: The wisp can move through other creatures and objects as if they were
    Difficult Terrain. It takes 5 (1d10) Force damage if it ends its turn inside an
    object.
actions:
- name: Shock
  damage:
  - type: lightning
    base:
      dice: 2
      die: 8
      bonus: 2
  type: utility
- name: Consume Life
  type: save
  ability: con
  dc: 10
  on_pass: none
  on_fail: full
- name: Vanish
  description: "The wisp and its light have the Invisible condition until the wisp\u2019\
    s Concentration ends on this effect, which ends early immediately after the wisp\
    \ makes an attack roll or uses Consume Life."

---
# Wight

*Tiny Undead, Chaotic Evil*

### Actions

**Shock.** Melee Attack Roll: +4, reach 5 ft. Hit: 11 (2d8 + 2) Lightning damage.

**Consume Life.** Constitution Saving Throw: DC 10, one living creature the wisp can see within 5 feet that has 0 Hit Points. Failure: The target dies, and the wisp regains 10 (3d6) Hit Points.

