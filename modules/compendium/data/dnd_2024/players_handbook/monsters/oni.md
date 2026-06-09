---name: Oni
size: Large
type: Large Aberration
alignment: Neutral
ac: '14'
hp: 104 (11d10 + 44)
speed: 30 ft.
stats:
  str: 16
  dex: 11
  con: 19
  int: 6
  wis: 13
  cha: 6
cr: 5 (XP 1,800; PB +3)
traits: []
actions:
- name: Multiattack
  description: The otyugh makes one Bite attack and two Tentacle attacks.
- name: Bite
  type: save
  ability: con
  dc: 15
  on_pass: none
  on_fail: full
  damage:
  - type: piercing
    base:
      dice: 2
      die: 8
      bonus: 3
- name: Tentacle
  damage:
  - type: piercing
    base:
      dice: 2
      die: 8
      bonus: 3
  type: utility
- name: Tentacle Slam
  type: save
  ability: con
  dc: 14
  on_pass: half
  on_fail: full
  damage:
  - type: bludgeoning
    base:
      dice: 3
      die: 8
      bonus: 3

---
# Oni

*Large Aberration, Neutral*

### Actions

**Bite.** Melee Attack Roll: +6, reach 5 ft. Hit: 12 (2d8 + 3) Piercing damage, and the target has the Poisoned condition. Whenever the Poisoned target finishes a Long Rest, it is subjected to the following effect. Constitution Saving Throw: DC 15. Failure: The target’s Hit Point maximum decreases by 5 (1d10) and doesn’t return to normal until the Poisoned condition ends on the target. Success: The Poisoned condition ends.

**Tentacle.** Melee Attack Roll: +6, reach 10 ft. Hit: 12 (2d8 + 3) Piercing damage. If the target is a Medium or smaller creature, it has the Grappled condition (escape DC 13) from one of two tentacles.

**Tentacle Slam.** Constitution Saving Throw: DC 14, each creature Grappled by the otyugh. Failure: 16 (3d8 + 3) Bludgeoning damage, and the target has the Stunned condition until the start of the otyugh’s next turn. Success: Half damage only.

