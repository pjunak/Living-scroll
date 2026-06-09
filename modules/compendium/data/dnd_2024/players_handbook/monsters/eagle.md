---name: Eagle
size: Huge
type: Huge Beast
alignment: Unaligned
ac: '12'
hp: 76 (8d12 + 24)
speed: 40 ft.
stats:
  str: 22
  dex: 9
  con: 17
  int: 3
  wis: 11
  cha: 6
cr: 4 (XP 1,100; PB +2)
traits: []
actions:
- name: Multiattack
  description: The elephant makes two Gore attacks.
- name: Gore
  damage:
  - type: piercing
    base:
      dice: 2
      die: 8
      bonus: 6
  type: utility
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
      bonus: 6

---
# Eagle

*Huge Beast, Unaligned*

### Actions

**Gore.** Melee Attack Roll: +8, reach 5 ft. Hit: 15 (2d8 + 6) Piercing damage. If the target is a Huge or smaller creature and the elephant moved 20+ feet straight toward it immediately before the hit, the target has the Prone condition.

**Trample.** Dexterity Saving Throw: DC 16, one creature within 5 feet that has the Prone condition. Failure: 17 (2d10 + 6) Bludgeoning damage. Success: Half damage.

