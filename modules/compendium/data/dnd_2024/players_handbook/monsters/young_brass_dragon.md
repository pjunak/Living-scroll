---name: Young Brass Dragon
size: Large
type: Large Dragon (Metallic)
alignment: Chaotic Good
ac: '17'
hp: 110 (13d10 + 39)
speed: 40 ft., Burrow 20 ft., Fly 80 ft.
stats:
  str: 19
  dex: 10
  con: 17
  int: 12
  wis: 11
  cha: 15
cr: 6 (XP 2,300; PB +3)
traits:
- name: Immunities
  description: Fire
actions:
- name: Multiattack
  description: The dragon makes three Rend attacks. It can replace two attacks with
    a use of Sleep Breath.
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 2
      die: 10
      bonus: 4
  type: utility
- name: "Fire Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 14
  on_pass: half
  on_fail: full
  damage:
  - type: fire
    base:
      dice: 11
      die: 6
      bonus: 0
- name: Sleep Breath
  type: save
  ability: con
  dc: 14
  on_pass: none
  on_fail: full

---
# Young Brass Dragon

*Large Dragon (Metallic), Chaotic Good*

### Actions

**Rend.** Melee Attack Roll: +7, reach 10 ft. Hit: 15 (2d10 + 4) Slashing damage.

**Fire Breath (Recharge 5–6).** Dexterity Saving Throw: DC 14, each creature in a 40-foot-long, 5-foot-wide Line. Failure: 38 (11d6) Fire damage. Success: Half damage.

**Sleep Breath.** Constitution Saving Throw: DC 14, each creature in a 30-foot Cone. Failure: The target has the Incapacitated condition until the end of its next turn, at which point it repeats the save. Second Failure: The target has the Unconscious condition for 1 minute. This effect ends for the target if it takes damage or a creature within 5 feet of it takes an action to wake it.

