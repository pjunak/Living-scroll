---name: Incubus
size: Large
type: Large Elemental
alignment: Neutral
ac: '14'
hp: 97 (13d10 + 26)
speed: 50 ft., Fly 50 ft. (hover)
stats:
  str: 16
  dex: 19
  con: 14
  int: 10
  wis: 15
  cha: 11
cr: 6 (XP 2,300; PB +3)
traits:
- name: Resistances
  description: Bludgeoning, Piercing, Slashing
- name: Immunities
  description: Poison; Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone,
    Restrained, Unconscious
- name: Air Form
  description: "The stalker can enter an enemy\u2019s space and stop there. It can\
    \ move through a space as narrow as 1 inch without expending extra movement to\
    \ do so."
- name: Invisibility
  description: The stalker has the Invisible condition.
actions:
- name: Multiattack
  description: The stalker makes three Wind Swipe attacks. It can replace one attack
    with a use of Vortex.
- name: Wind Swipe
  damage:
  - type: force
    base:
      dice: 2
      die: 6
      bonus: 4
  type: utility
- name: Vortex
  type: save
  ability: con
  dc: 14
  on_pass: none
  on_fail: full
  damage:
  - type: thunder
    base:
      dice: 1
      die: 8
      bonus: 3
  - type: thunder
    base:
      dice: 2
      die: 6
      bonus: 0

---
# Incubus

*Large Elemental, Neutral*

### Actions

**Wind Swipe.** Melee Attack Roll: +7, reach 5 ft. Hit: 11 (2d6 + 4) Force damage.

**Vortex.** Constitution Saving Throw: DC 14, one Large or smaller creature in the stalker’s space. Failure: 7 (1d8 + 3) Thunder damage, and the target has the Grappled condition (escape DC 13). Until the grapple ends, the target can’t cast spells with a Verbal component and takes 7 (2d6) Thunder damage at the start of each of the stalker’s turns.

