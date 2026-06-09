---name: Young Silver Dragon
size: Large
type: Large Dragon (Metallic)
alignment: Lawful Good
ac: '18'
hp: 168 (16d10 + 80)
speed: 40 ft., Fly 80 ft.
stats:
  str: 23
  dex: 10
  con: 21
  int: 14
  wis: 11
  cha: 19
cr: 9 (XP 5,000; PB +4)
traits:
- name: Immunities
  description: Cold
actions:
- name: Multiattack
  description: The dragon makes three Rend attacks. It can replace one attack with
    a use of Paralyzing Breath.
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 2
      die: 8
      bonus: 6
  type: utility
- name: "Cold Breath (Recharge 5\u20136)"
  type: save
  ability: con
  dc: 17
  on_pass: half
  on_fail: full
  damage:
  - type: cold
    base:
      dice: 11
      die: 8
      bonus: 0
- name: Paralyzing Breath
  type: save
  ability: con
  dc: 17
  on_pass: none
  on_fail: full

---
# Young Silver Dragon

*Large Dragon (Metallic), Lawful Good*

### Actions

**Rend.** Melee Attack Roll: +10, reach 10 ft. Hit: 15 (2d8 + 6) Slashing damage.

**Cold Breath (Recharge 5–6).** Constitution Saving Throw: DC 17, each creature in a 30-foot Cone. Failure: 49 (11d8) Cold damage. Success: Half damage.

**Paralyzing Breath.** Constitution Saving Throw: DC 17, each creature in a 30-foot Cone. First Failure: The target has the Incapacitated condition until the end of its next turn, when it repeats the save. Second Failure: The target has the Paralyzed condition, and it repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically.

