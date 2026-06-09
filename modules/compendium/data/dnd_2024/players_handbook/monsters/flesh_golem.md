---name: Flesh Golem
size: Huge
type: Huge Giant
alignment: Neutral Evil
ac: '15'
hp: 149 (13d12 + 65)
speed: 40 ft.
stats:
  str: 23
  dex: 9
  con: 21
  int: 9
  wis: 10
  cha: 12
cr: 8 (XP 3,900; PB +3)
traits:
- name: Immunities
  description: Cold
actions:
- name: Multiattack
  description: The giant makes two attacks, using Frost Axe or Great Bow in any combination.
- name: Frost Axe
  damage:
  - type: slashing
    base:
      dice: 2
      die: 12
      bonus: 6
  - type: cold
    base:
      dice: 2
      die: 8
      bonus: 0
  type: utility
- name: Great Bow
  damage:
  - type: piercing
    base:
      dice: 2
      die: 10
      bonus: 6
  - type: cold
    base:
      dice: 2
      die: 6
      bonus: 0
  type: utility
- name: "War Cry (Recharge 5\u20136)"
  description: "The giant or one creature of its choice that can see or hear it gains\
    \ 16 (2d10 + 5) Temporary Hit Points and has Advantage on attack rolls until the\
    \ start of the giant\u2019s next turn."

---
# Flesh Golem

*Huge Giant, Neutral Evil*

### Actions

**Frost Axe.** Melee Attack Roll: +9, reach 10 ft. Hit: 19 (2d12 + 6) Slashing damage plus 9 (2d8) Cold damage.

**Great Bow.** Ranged Attack Roll: +9, range 150/600 ft. Hit: 17 (2d10 + 6) Piercing damage plus 7 (2d6) Cold damage, and the target’s Speed decreases by 10 feet until the end of its next turn.

