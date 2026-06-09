---name: Brass Dragon Wyrmling
size: Medium
type: Medium Dragon (Metallic)
alignment: Chaotic Good
ac: '15'
hp: 22 (4d8 + 4)
speed: 30 ft., Burrow 15 ft., Fly 60 ft.
stats:
  str: 15
  dex: 10
  con: 13
  int: 10
  wis: 11
  cha: 13
cr: 1 (XP 200; PB +2)
traits:
- name: Immunities
  description: Fire
actions:
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 1
      die: 10
      bonus: 2
  type: utility
- name: "Fire Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 11
  on_pass: half
  on_fail: full
  damage:
  - type: fire
    base:
      dice: 4
      die: 6
      bonus: 0
- name: Sleep Breath
  type: save
  ability: con
  dc: 11
  on_pass: none
  on_fail: full

---
# Brass Dragon Wyrmling

*Medium Dragon (Metallic), Chaotic Good*

### Actions

**Rend.** Melee Attack Roll: +4, reach 5 ft. Hit: 7 (1d10 + 2) Slashing damage.

**Fire Breath (Recharge 5–6).** Dexterity Saving Throw: DC 11, each creature in a 20-foot-long, 5-foot-wide Line. Failure: 14 (4d6) Fire damage. Success: Half damage.

**Sleep Breath.** Constitution Saving Throw: DC 11, each creature in a 15-foot Cone. Failure: The target has the Incapacitated condition until the end of its next turn, at which point it repeats the save. Second Failure: The target has the Unconscious condition for 1 minute. This effect ends for the target if it takes damage or a creature within 5 feet of it takes an action to wake it.

