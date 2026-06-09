---name: Gold Dragons
size: Large
type: Large Construct
alignment: Unaligned
ac: '19'
hp: 114 (12d10 + 48)
speed: 40 ft.
stats:
  str: 20
  dex: 11
  con: 18
  int: 2
  wis: 12
  cha: 7
cr: 5 (XP 1,800; PB +3)
traits:
- name: Immunities
  description: Exhaustion, Petrified
actions:
- name: Gore
  damage:
  - type: piercing
    base:
      dice: 2
      die: 12
      bonus: 5
  type: utility
- name: "Petrifying Breath (Recharge 5\u20136)"
  type: save
  ability: con
  dc: 15
  on_pass: none
  on_fail: full
- name: Trample
  type: save
  ability: dex
  dc: 16
  on_pass: half
  on_fail: full
  damage:
  - type: bludgeoning
    base:
      dice: 2
      die: 10
      bonus: 5

---
# Gold Dragons

*Large Construct, Unaligned*

### Actions

**Gore.** Melee Attack Roll: +8, reach 5 ft. Hit: 18 (2d12 + 5) Piercing damage. If the target is a Large or smaller creature and the gorgon moved 20+ feet straight toward it immediately before the hit, the target has the Prone condition.

**Petrifying Breath (Recharge 5–6).** Constitution Saving Throw: DC 15, each creature in a 30-foot Cone. First Failure: The target has the Restrained condition and repeats the save at the end of its next turn if it is still Restrained, ending the effect on itself on a success. Second Failure: The target has the Petrified condition instead of the Restrained condition.

**Trample.** Dexterity Saving Throw: DC 16, one creature within 5 feet that has the Prone condition. Failure: 16 (2d10 + 5) Bludgeoning damage. Success: Half damage.

