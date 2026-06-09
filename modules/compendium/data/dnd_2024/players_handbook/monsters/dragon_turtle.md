---name: Dragon Turtle
size: Small
type: Small Fiend (Demon)
alignment: Chaotic Evil
ac: '11'
hp: 18 (4d6 + 4)
speed: 20 ft.
stats:
  str: 12
  dex: 11
  con: 12
  int: 5
  wis: 8
  cha: 3
cr: 1/4 (XP 50; PB +2)
traits:
- name: Resistances
  description: Cold, Fire, Lightning
- name: Immunities
  description: Poison; Poisoned
actions:
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 1
      die: 6
      bonus: 1
  type: utility
- name: Fetid Cloud (1/Day)
  type: save
  ability: con
  dc: 11
  on_pass: none
  on_fail: full

---
# Dragon Turtle

*Small Fiend (Demon), Chaotic Evil*

### Actions

**Rend.** Melee Attack Roll: +3, reach 5 ft. Hit: 4 (1d6 + 1) Slashing damage.

**Fetid Cloud (1/Day).** Constitution Saving Throw: DC 11, each creature in a 10-foot Emanation originating from the dretch. Failure: The target has the Poisoned condition until the end of its next turn. While Poisoned, the creature can take either an action or a Bonus Action on its turn, not both, and it can’t take Reactions.

