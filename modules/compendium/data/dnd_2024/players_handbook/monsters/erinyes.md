---name: Erinyes
size: Medium
type: Medium Monstrosity
alignment: Neutral Evil
ac: '13'
hp: 44 (8d8 + 8)
speed: 30 ft., Climb 30 ft.
stats:
  str: 14
  dex: 15
  con: 13
  int: 7
  wis: 12
  cha: 8
cr: 2 (XP 450; PB +2)
traits:
- name: Spider Climb
  description: The ettercap can climb difficult surfaces, including along ceilings,
    without needing to make an ability check.
- name: Web Walker
  description: The ettercap ignores movement restrictions caused by webs, and the
    ettercap knows the location of any other creature in contact with the same web.
actions:
- name: Multiattack
  description: The ettercap makes one Bite attack and one Claw attack.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 1
      die: 6
      bonus: 2
  - type: poison
    base:
      dice: 1
      die: 4
      bonus: 0
  type: utility
- name: Claw
  damage:
  - type: slashing
    base:
      dice: 2
      die: 4
      bonus: 2
  type: utility
- name: "Web Strand (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 12
  on_pass: none
  on_fail: full
- name: Reel
  description: The ettercap pulls one creature within 30 feet of itself that is Restrained
    by its Web Strand up to 25 feet straight toward itself.

---
# Erinyes

*Medium Monstrosity, Neutral Evil*

### Actions

**Bite.** Melee Attack Roll: +4, reach 5 ft. Hit: 5 (1d6 + 2) Piercing damage plus 2 (1d4) Poison damage, and the target has the Poisoned condition until the start of the ettercap’s next turn.

**Claw.** Melee Attack Roll: +4, reach 5 ft. Hit: 7 (2d4 + 2) Slashing damage.

**Web Strand (Recharge 5–6).** Dexterity Saving Throw: DC 12, one Large or smaller creature the ettercap can see within 30 feet. Failure: The target has the Restrained condition until the web is destroyed (AC 10; HP 5; Vulnerability to Fire damage; Immunity to Bludgeoning, Poison, and Psychic damage).

