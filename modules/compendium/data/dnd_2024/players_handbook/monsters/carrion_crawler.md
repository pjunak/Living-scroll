---name: Carrion Crawler
size: Large
type: Large Fey
alignment: Neutral Good
ac: '16'
hp: 45 (6d10 + 12)
speed: 50 ft.
stats:
  str: 18
  dex: 14
  con: 14
  int: 9
  wis: 13
  cha: 11
cr: 2 (XP 450; PB +2)
traits: []
actions:
- name: Multiattack
  description: The centaur makes two attacks, using Pike or Longbow in any combination.
- name: Pike
  damage:
  - type: piercing
    base:
      dice: 1
      die: 10
      bonus: 4
  type: utility
- name: Longbow
  damage:
  - type: piercing
    base:
      dice: 1
      die: 8
      bonus: 2
  type: utility
- name: "Trampling Charge (Recharge 5\u20136)"
  type: save
  ability: str
  dc: 14
  on_pass: none
  on_fail: full
  damage:
  - type: bludgeoning
    base:
      dice: 1
      die: 6
      bonus: 4

---
# Carrion Crawler

*Large Fey, Neutral Good*

### Actions

**Pike.** Melee Attack Roll: +6, reach 10 ft. Hit: 9 (1d10 + 4) Piercing damage.

**Longbow.** Ranged Attack Roll: +4, range 150/600 ft. Hit: 6 (1d8 + 2) Piercing damage.

**Trampling Charge (Recharge 5–6).** The centaur moves up to its Speed without provoking Opportunity Attacks and can move through the spaces of Medium or smaller creatures. Each creature whose space the centaur enters is targeted once by the following effect. Strength Saving Throw: DC 14. Failure: 7 (1d6 + 4) Bludgeoning damage, and the target has the Prone condition.

