---name: Triceratops
size: Huge
type: Huge Beast (Dinosaur)
alignment: Unaligned
ac: '13'
hp: 136 (13d12 + 52)
speed: 50 ft.
stats:
  str: 25
  dex: 10
  con: 19
  int: 2
  wis: 12
  cha: 9
cr: 8 (XP 3,900; PB +3)
traits: []
actions:
- name: Multiattack
  description: The tyrannosaurus makes one Bite attack and one Tail attack.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 4
      die: 12
      bonus: 7
  type: utility
- name: Tail
  damage:
  - type: bludgeoning
    base:
      dice: 4
      die: 8
      bonus: 7
  type: utility

---
# Triceratops

*Huge Beast (Dinosaur), Unaligned*

### Actions

**Bite.** Melee Attack Roll: +10, reach 10 ft. Hit: 33 (4d12 + 7) Piercing damage. If the target is a Large or smaller creature, it has the Grappled condition (escape DC 17). While Grappled, the target has the Restrained condition and can’t be targeted by the tyrannosaurus’s Tail.

**Tail.** Melee Attack Roll: +10, reach 15 ft. Hit: 25 (4d8 + 7) Bludgeoning damage. If the target is a Huge or smaller creature, it has the Prone condition.

