---name: Lizard
size: Huge
type: Huge Beast
alignment: Unaligned
ac: '13'
hp: 126 (11d12 + 55)
speed: 50 ft.
stats:
  str: 24
  dex: 9
  con: 21
  int: 3
  wis: 11
  cha: 6
cr: 6 (XP 2,300; PB +3)
traits: []
actions:
- name: Multiattack
  description: The mammoth makes two Gore attacks.
- name: Gore
  damage:
  - type: piercing
    base:
      dice: 2
      die: 10
      bonus: 7
  type: utility
- name: Trample
  type: save
  ability: dex
  dc: 18
  on_pass: half
  on_fail: full
  damage:
  - type: bludgeoning
    base:
      dice: 4
      die: 10
      bonus: 7

---
# Lizard

*Huge Beast, Unaligned*

### Actions

**Gore.** Melee Attack Roll: +10, reach 10 ft. Hit: 18 (2d10 + 7) Piercing damage. If the target is a Huge or smaller creature and the mammoth moved 20+ feet straight toward it immediately before the hit, the target has the Prone condition.

**Trample.** Dexterity Saving Throw: DC 18, one creature within 5 feet that has the Prone condition. Failure: 29 (4d10 + 7) Bludgeoning damage. Success: Half damage.

