---name: "Will-o\u2019-Wisp"
size: Large
type: Large Monstrosity
alignment: Neutral Evil
ac: '13'
hp: 75 (10d10 + 20)
speed: 50 ft.
stats:
  str: 18
  dex: 13
  con: 14
  int: 7
  wis: 12
  cha: 8
cr: 3 (XP 700; PB +2)
traits:
- name: Immunities
  description: Cold
- name: Pack Tactics
  description: "The wolf has Advantage on an attack roll against a creature if at\
    \ least one of the wolf\u2019s allies is within 5 feet of the creature and the\
    \ ally doesn\u2019t have the Incapacitated condition."
actions:
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 2
      die: 6
      bonus: 4
  type: utility
- name: "Cold Breath (Recharge 5\u20136)"
  type: save
  ability: con
  dc: 12
  on_pass: half
  on_fail: full
  damage:
  - type: cold
    base:
      dice: 4
      die: 8
      bonus: 0

---
# Will-o’-Wisp

*Large Monstrosity, Neutral Evil*

### Actions

**Bite.** Melee Attack Roll: +6, reach 5 ft. Hit: 11 (2d6 + 4) Piercing damage. If the target is a Large or smaller creature, it has the Prone condition.

**Cold Breath (Recharge 5–6).** Constitution Saving Throw: DC 12, each creature in a 15-foot Cone. Failure: 18 (4d8) Cold damage. Success: Half damage.

