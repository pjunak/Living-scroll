---name: Ice Mephit
size: Small
type: Small Elemental
alignment: Neutral Evil
ac: '11'
hp: 21 (6d6)
speed: 30 ft., Fly 30 ft.
stats:
  str: 7
  dex: 13
  con: 10
  int: 9
  wis: 11
  cha: 12
cr: 1/2 (XP 100; PB +2)
traits:
- name: Vulnerabilities
  description: Fire
- name: Immunities
  description: Cold, Poison; Exhaustion, Poisoned
- name: Death Burst
  description: 'The mephit explodes when it dies. Constitution Saving Throw: DC 10,
    each creature in a 5-foot Emanation originating from the mephit. Failure: 5 (2d4)
    Cold damage. Success: Half damage.'
actions:
- name: Claw
  damage:
  - type: slashing
    base:
      dice: 1
      die: 4
      bonus: 1
  - type: cold
    base:
      dice: 1
      die: 4
      bonus: 0
  type: utility
- name: Fog Cloud (1/Day)
  description: The mephit casts Fog Cloud, requiring no spell components and using
    Charisma as the spellcasting ability.
- name: Frost Breath (Recharge 6)
  type: save
  ability: con
  dc: 10
  on_pass: half
  on_fail: full
  damage:
  - type: cold
    base:
      dice: 3
      die: 4
      bonus: 0

---
# Ice Mephit

*Small Elemental, Neutral Evil*

### Actions

**Claw.** Melee Attack Roll: +3, reach 5 ft. Hit: 3 (1d4 + 1) Slashing damage plus 2 (1d4) Cold damage.

**Frost Breath (Recharge 6).** Constitution Saving Throw: DC 10, each creature in a 15-foot Cone. Failure: 7 (3d4) Cold damage. Success: Half damage.

