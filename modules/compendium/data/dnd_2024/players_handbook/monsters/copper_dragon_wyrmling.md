---name: Copper Dragon Wyrmling
size: Medium
type: Medium Dragon (Metallic)
alignment: Chaotic Good
ac: '16'
hp: 22 (4d8 + 4)
speed: 30 ft., Climb 30 ft., Fly 60 ft.
stats:
  str: 15
  dex: 12
  con: 13
  int: 14
  wis: 11
  cha: 13
cr: 1 (XP 200; PB +2)
traits:
- name: Immunities
  description: Acid
actions:
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 1
      die: 10
      bonus: 2
  type: utility
- name: "Acid Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 11
  on_pass: half
  on_fail: full
  damage:
  - type: acid
    base:
      dice: 4
      die: 8
      bonus: 0
- name: Slowing Breath
  type: save
  ability: con
  dc: 11
  on_pass: none
  on_fail: full

---
# Copper Dragon Wyrmling

*Medium Dragon (Metallic), Chaotic Good*

### Actions

**Rend.** Melee Attack Roll: +4, reach 5 ft. Hit: 7 (1d10 + 2) Slashing damage.

**Acid Breath (Recharge 5–6).** Dexterity Saving Throw: DC 11, each creature in a 20-foot-long, 5-foot-wide Line. Failure: 18 (4d8) Acid damage. Success: Half damage.

**Slowing Breath.** Constitution Saving Throw: DC 11, each creature in a 15-foot Cone. Failure: The target can’t take Reactions; its Speed is halved; and it can take either an action or a Bonus Action on its turn, not both. This effect lasts until the end of its next turn.

