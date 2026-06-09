---name: Shadow
size: Large
type: Large Plant
alignment: Unaligned
ac: '15'
hp: 110 (13d10 + 39)
speed: 30 ft., Swim 20 ft.
stats:
  str: 18
  dex: 8
  con: 16
  int: 5
  wis: 10
  cha: 5
cr: 5 (XP 1,800; PB +3)
traits:
- name: Resistances
  description: Cold, Fire
- name: Immunities
  description: Lightning; Deafened, Exhaustion
- name: Lightning Absorption
  description: . Whenever the shambling mound is subjected to Lightning damage, it
    regains a number of Hit Points equal to the Lightning damage dealt.
actions:
- name: Multiattack
  description: The shambling mound makes three Charged Tendril attacks. It can replace
    one attack with a use of Engulf.
- name: Charged Tendril
  damage:
  - type: bludgeoning
    base:
      dice: 1
      die: 6
      bonus: 4
  - type: lightning
    base:
      dice: 2
      die: 4
      bonus: 0
  type: utility
- name: Engulf
  type: save
  ability: str
  dc: 15
  on_pass: none
  on_fail: full
  damage:
  - type: lightning
    base:
      dice: 3
      die: 6
      bonus: 0

---
# Shadow

*Large Plant, Unaligned*

### Actions

**Charged Tendril.** Melee Attack Roll: +7, reach 10 ft. Hit: 7 (1d6 + 4) Bludgeoning damage plus 5 (2d4) Lightning damage. If the target is a Medium or smaller creature, the shambling mound pulls the target 5 feet straight toward itself.

**Engulf.** Strength Saving Throw: DC 15, one Medium or smaller creature within 5 feet. Failure: The target is pulled into the shambling mound’s space and has the Grappled condition (escape DC 14). Until the grapple ends, the target has the Blinded and Restrained conditions, and it takes 10 (3d6) Lightning damage at the start of each of its turns. When the shambling mound moves, the Grappled target moves with it, costing it no extra movement. The shambling mound can have only one creature Grappled by this action at a time.

