---name: Giant Shark
size: Large
type: Large Beast
alignment: Unaligned
ac: '14'
hp: 26 (4d10 + 4)
speed: 30 ft., Climb 30 ft.
stats:
  str: 14
  dex: 16
  con: 12
  int: 2
  wis: 11
  cha: 4
cr: 1 (XP 200; PB +2)
traits:
- name: Spider Climb
  description: The spider can climb difficult surfaces, including along ceilings,
    without needing to make an ability check.
- name: Web Walker
  description: The spider ignores movement restrictions caused by webs, and it knows
    the location of any other creature in contact with the same web.
actions:
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 1
      die: 8
      bonus: 3
  - type: poison
    base:
      dice: 2
      die: 6
      bonus: 0
  type: utility
- name: "Web (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 13
  on_pass: none
  on_fail: full

---
# Giant Shark

*Large Beast, Unaligned*

### Actions

**Bite.** Melee Attack Roll: +5, reach 5 ft. Hit: 7 (1d8 + 3) Piercing damage plus 7 (2d6) Poison damage.

**Web (Recharge 5–6).** Dexterity Saving Throw: DC 13, one creature the spider can see within 60 feet. Failure: The target has the Restrained condition until the web is destroyed (AC 10; HP 5; Vulnerability to Fire damage; Immunity to Poison and Psychic damage).

