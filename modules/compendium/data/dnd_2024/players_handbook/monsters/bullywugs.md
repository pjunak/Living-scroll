---name: Bullywugs
size: Large
type: Large Monstrosity
alignment: Unaligned
ac: '17'
hp: 94 (9d10 + 45)
speed: 40 ft., Burrow 40 ft.
stats:
  str: 19
  dex: 11
  con: 21
  int: 2
  wis: 10
  cha: 5
cr: 5 (XP 1,800; PB +3)
traits: []
actions:
- name: Multiattack
  description: The bulette makes two Bite attacks.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 2
      die: 12
      bonus: 4
  type: utility
- name: Deadly Leap
  type: save
  ability: dex
  dc: 15
  on_pass: half
  on_fail: full
  damage:
  - type: bludgeoning
    base:
      dice: 3
      die: 12
      bonus: 0
- name: Leap
  description: The bulette jumps up to 30 feet by spending 10 feet of movement.

---
# Bullywugs

*Large Monstrosity, Unaligned*

### Actions

**Bite.** Melee Attack Roll: +7, reach 5 ft. Hit: 17 (2d12 + 4) Piercing damage.

**Deadly Leap.** The bulette spends 5 feet of movement to jump to a space within 15 feet that contains one or more Large or smaller creatures. Dexterity Saving Throw: DC 15, each creature in the bulette’s destination space. Failure: 19 (3d12) Bludgeoning damage, and the target has the Prone condition. Success: Half damage, and the target is pushed 5 feet straight away from the bulette.

