---name: Noble
size: Medium
type: Medium Aberration
alignment: Neutral Evil
ac: '15'
hp: 45 (6d8 + 18)
speed: 30 ft.
stats:
  str: 14
  dex: 16
  con: 16
  int: 13
  wis: 10
  cha: 8
cr: 2 (XP 450; PB +2)
traits: []
actions:
- name: Multiattack
  description: The nothic makes two Claw attacks.
- name: Claw
  damage:
  - type: slashing
    base:
      dice: 1
      die: 10
      bonus: 3
  type: utility
- name: Rotting Gaze
  type: save
  ability: con
  dc: 13
  on_pass: half
  on_fail: full
  damage:
  - type: necrotic
    base:
      dice: 5
      die: 6
      bonus: 0
- name: Weird Insight (Recharge 6)
  type: save
  ability: wis
  dc: 14
  on_pass: none
  on_fail: full

---
# Noble

*Medium Aberration, Neutral Evil*

### Actions

**Claw.** Melee Attack Roll: +5, reach 5 ft. Hit: 8 (1d10 + 3) Slashing damage.

**Rotting Gaze.** Constitution Saving Throw: DC 13, one creature the nothic can see within 120 feet. Failure: 17 (5d6) Necrotic damage. Success: Half damage.

**Weird Insight (Recharge 6).** Wisdom Saving Throw: DC 14, one creature the nothic can see within 120 feet. Failure: The nothic magically learns one fact or secret about the target.

