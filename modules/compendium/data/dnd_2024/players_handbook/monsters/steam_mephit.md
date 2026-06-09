---name: Steam Mephit
size: Small
type: Small Elemental
alignment: Neutral Evil
ac: '10'
hp: 17 (5d6)
speed: 30 ft., Fly 30 ft.
stats:
  str: 5
  dex: 11
  con: 10
  int: 11
  wis: 10
  cha: 12
cr: 1/4 (XP 50; PB +2)
traits:
- name: Immunities
  description: Fire, Poison; Exhaustion, Poisoned
- name: Blurred Form
  description: Attack rolls against the mephit are made with Disadvantage unless the
    mephit has the Incapacitated condition.
- name: Death Burst
  description: 'The mephit explodes when it dies. Dexterity Saving Throw: DC 10, each
    creature in a 5-foot Emanation originating from the mephit. Failure: 5 (2d4) Fire
    damage. Success: Half damage.'
actions:
- name: Claw
  damage:
  - type: slashing
    base:
      dice: 1
      die: 4
      bonus: 0
  - type: fire
    base:
      dice: 1
      die: 4
      bonus: 0
  type: utility
- name: Steam Breath (Recharge 6)
  type: save
  ability: con
  dc: 10
  on_pass: half
  on_fail: full
  damage:
  - type: fire
    base:
      dice: 2
      die: 4
      bonus: 0

---
# Steam Mephit

*Small Elemental, Neutral Evil*

### Actions

**Claw.** Melee Attack Roll: +2, reach 5 ft. Hit: 2 (1d4) Slashing damage plus 2 (1d4) Fire damage.

**Steam Breath (Recharge 6).** Constitution Saving Throw: DC 10, each creature in a 15-foot Cone. Failure: 5 (2d4) Fire damage, and the target’s Speed decreases by 10 feet until the end of the mephit’s next turn. Success: Half damage only. Failure or Success: Being underwater doesn’t grant Resistance to this Fire damage.

