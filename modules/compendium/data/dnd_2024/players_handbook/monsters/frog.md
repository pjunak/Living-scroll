---name: Frog
size: Huge
type: Huge Beast
alignment: Unaligned
ac: '12'
hp: 168 (16d12 + 64)
speed: 40 ft., Climb 40 ft.
stats:
  str: 23
  dex: 14
  con: 18
  int: 5
  wis: 12
  cha: 7
cr: 7 (XP 2,900; PB +3)
traits: []
actions:
- name: Multiattack
  description: The ape makes two Fist attacks.
- name: Fist
  damage:
  - type: bludgeoning
    base:
      dice: 3
      die: 10
      bonus: 6
  type: utility
- name: Boulder Toss (Recharge 6)
  type: save
  ability: dex
  dc: 17
  on_pass: half
  on_fail: full
  damage:
  - type: bludgeoning
    base:
      dice: 7
      die: 6
      bonus: 0
- name: Leap
  description: The ape jumps up to 30 feet by spending 10 feet of movement.

---
# Frog

*Huge Beast, Unaligned*

### Actions

**Fist.** Melee Attack Roll: +9, reach 10 ft. Hit: 22 (3d10 + 6) Bludgeoning damage.

**Boulder Toss (Recharge 6).** The ape hurls a boulder at a point it can see within 90 feet. Dexterity Saving Throw: DC 17, each creature in a 5-foot-radius Sphere centered on that point. Failure: 24 (7d6) Bludgeoning damage. If the target is a Large or smaller creature, it has the Prone condition. Success: Half damage only.

