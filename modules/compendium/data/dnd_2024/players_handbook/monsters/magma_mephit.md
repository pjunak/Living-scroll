---name: Magma Mephit
size: Small
type: Small Elemental
alignment: Neutral Evil
ac: '11'
hp: 18 (4d6 + 4)
speed: 30 ft., Fly 30 ft.
stats:
  str: 8
  dex: 12
  con: 12
  int: 7
  wis: 10
  cha: 10
cr: 1/2 (XP 100; PB +2)
traits:
- name: Vulnerabilities
  description: Cold
- name: Immunities
  description: Fire, Poison; Exhaustion, Poisoned
- name: Death Burst
  description: 'The mephit explodes when it dies. Dexterity Saving Throw: DC 11, each
    creature in a 5-foot Emanation originating from the mephit. Failure: 7 (2d6) Fire
    damage. Success: Half damage.'
actions:
- name: Claw
  damage:
  - type: slashing
    base:
      dice: 1
      die: 4
      bonus: 1
  - type: fire
    base:
      dice: 1
      die: 6
      bonus: 0
  type: utility
- name: Fire Breath (Recharge 6)
  type: save
  ability: dex
  dc: 11
  on_pass: half
  on_fail: full
  damage:
  - type: fire
    base:
      dice: 2
      die: 6
      bonus: 0

---
# Magma Mephit

*Small Elemental, Neutral Evil*

### Actions

**Claw.** Melee Attack Roll: +3, reach 5 ft. Hit: 3 (1d4 + 1) Slashing damage plus 3 (1d6) Fire damage.

**Fire Breath (Recharge 6).** Dexterity Saving Throw: DC 11, each creature in a 15-foot Cone. Failure: 7 (2d6) Fire damage. Success: Half damage.

