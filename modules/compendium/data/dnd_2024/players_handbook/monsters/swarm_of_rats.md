---name: Swarm of Rats
size: Medium
type: Medium Swarm of Tiny Beasts
alignment: Unaligned
ac: '12'
hp: 11 (2d8 + 2)
speed: 10 ft., Fly 50 ft.
stats:
  str: 6
  dex: 14
  con: 12
  int: 5
  wis: 12
  cha: 6
cr: 1/4 (XP 50; PB +2)
traits:
- name: Resistances
  description: Bludgeoning, Piercing, Slashing
- name: Immunities
  description: Charmed, Frightened, Grappled, Paralyzed, Petrified, Prone, Restrained,
    Stunned
- name: Swarm
  description: "The swarm can occupy another creature\u2019s space and vice versa,\
    \ and the swarm can move through any opening large enough for a Tiny raven. The\
    \ swarm can\u2019t regain Hit Points or gain Temporary Hit Points."
actions:
- name: Beaks
  damage:
  - type: piercing
    base:
      dice: 1
      die: 6
      bonus: 2
  - type: piercing
    base:
      dice: 1
      die: 4
      bonus: 0
  type: utility
- name: Cacophony (Recharge 6)
  type: save
  ability: wis
  dc: 10
  on_pass: none
  on_fail: full

---
# Swarm of Rats

*Medium Swarm of Tiny Beasts, Unaligned*

### Actions

**Beaks.** Melee Attack Roll: +4, reach 5 ft. Hit: 5 (1d6 + 2) Piercing damage, or 2 (1d4) Piercing damage if the swarm is Bloodied.

**Cacophony (Recharge 6).** Wisdom Saving Throw: DC 10, one creature in the swarm’s space. Failure: The target has the Deafened condition until the start of the swarm’s next turn. While Deafened, the target also has Disadvantage on ability checks and attack rolls.

