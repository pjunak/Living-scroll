---name: Bearded Devil
size: Huge
type: Huge Monstrosity
alignment: Neutral Evil
ac: '17'
hp: 168 (16d12 + 64)
speed: 50 ft., Climb 50 ft.
stats:
  str: 23
  dex: 16
  con: 18
  int: 7
  wis: 14
  cha: 12
cr: 11 (XP 7,200; PB +4)
traits:
- name: Immunities
  description: Lightning
actions:
- name: Multiattack
  description: The behir makes one Bite attack and uses Constrict.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 2
      die: 12
      bonus: 6
  - type: lightning
    base:
      dice: 2
      die: 10
      bonus: 0
  type: utility
- name: Constrict
  type: save
  ability: str
  dc: 18
  on_pass: none
  on_fail: full
  damage:
  - type: bludgeoning
    base:
      dice: 5
      die: 8
      bonus: 6
- name: "Lightning Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 16
  on_pass: half
  on_fail: full
  damage:
  - type: lightning
    base:
      dice: 12
      die: 10
      bonus: 0
- name: Swallow
  type: save
  ability: dex
  dc: 18
  on_pass: none
  on_fail: full
  damage:
  - type: acid
    base:
      dice: 6
      die: 6
      bonus: 0

---
# Bearded Devil

*Huge Monstrosity, Neutral Evil*

### Actions

**Bite.** Melee Attack Roll: +10, reach 10 ft. Hit: 19 (2d12 + 6) Piercing damage plus 11 (2d10) Lightning damage.

**Constrict.** Strength Saving Throw: DC 18, one Large or smaller creature the behir can see within 5 feet. Failure: 28 (5d8 + 6) Bludgeoning damage. The target has the Grappled condition (escape DC 16), and it has the Restrained condition until the grapple ends.

**Lightning Breath (Recharge 5–6).** Dexterity Saving Throw: DC 16, each creature in a 90-foot-long, 5-foot-wide Line. Failure: 66 (12d10) Lightning damage. Success: Half damage.

**Swallow.** Dexterity Saving Throw: DC 18, one Large or smaller creature Grappled by the behir (the behir can have only one creature swallowed at a time). Failure: The behir swallows the target, which is no longer Grappled. While swallowed, a creature has the Blinded and Restrained conditions, has Total Cover against attacks and other effects outside the behir, and takes 21 (6d6) Acid damage at the start of each of the behir’s turns.

