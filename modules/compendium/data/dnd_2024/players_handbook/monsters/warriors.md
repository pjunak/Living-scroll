---name: Warriors
size: Large
type: Large Elemental
alignment: Neutral
ac: '14'
hp: 114 (12d10 + 48)
speed: 30 ft., Swim 90 ft.
stats:
  str: 18
  dex: 14
  con: 18
  int: 5
  wis: 10
  cha: 8
cr: 5 (XP 1,800; PB +3)
traits:
- name: Resistances
  description: Acid, Fire
- name: Immunities
  description: Poison; Exhaustion, Grappled, Paralyzed, Petrified, Poisoned, Prone,
    Restrained, Unconscious
- name: Freeze
  description: If the elemental takes Cold damage, its Speed decreases by 20 feet
    until the end of its next turn.
- name: Water Form
  description: "The elemental can enter an enemy\u2019s space and stop there. It can\
    \ move through a space as narrow as 1 inch without expending extra movement to\
    \ do so."
actions:
- name: Multiattack
  description: The elemental makes two Slam attacks.
- name: Slam
  damage:
  - type: bludgeoning
    base:
      dice: 2
      die: 8
      bonus: 4
  type: utility
- name: "Whelm (Recharge 4\u20136)"
  type: save
  ability: str
  dc: 15
  on_pass: half
  on_fail: full
  damage:
  - type: bludgeoning
    base:
      dice: 4
      die: 8
      bonus: 4
  - type: bludgeoning
    base:
      dice: 2
      die: 8
      bonus: 0

---
# Warriors

*Large Elemental, Neutral*

### Actions

**Slam.** Melee Attack Roll: +7, reach 5 ft. Hit: 13 (2d8 + 4) Bludgeoning damage. If the target is a Medium or smaller creature, it has the Prone condition.

**Whelm (Recharge 4–6).** Strength Saving Throw: DC 15, each creature in the elemental’s space. Failure: 22 (4d8 + 4) Bludgeoning damage. If the target is a Large or smaller creature, it has the Grappled condition (escape DC 14). Until the grapple ends, the target has the Restrained condition, is suffocating unless it can breathe water, and takes 9 (2d8) Bludgeoning damage at the start of each of the elemental’s turns. The elemental can grapple one Large creature or up to two Medium or smaller creatures at a time with Whelm. As an action, a creature within 5 feet of the elemental can pull a creature out of it by succeeding on a DC 14 Strength (Athletics) check. Success: Half damage only.

