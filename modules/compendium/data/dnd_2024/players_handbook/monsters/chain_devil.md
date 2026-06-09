---name: Chain Devil
size: Large
type: Large Monstrosity
alignment: Chaotic Evil
ac: '14'
hp: 114 (12d10 + 48)
speed: 30 ft., Fly 60 ft.
stats:
  str: 19
  dex: 11
  con: 19
  int: 3
  wis: 14
  cha: 10
cr: 6 (XP 2,300; PB +3)
traits: []
actions:
- name: Multiattack
  description: The chimera makes one Ram attack, one Bite attack, and one Claw attack.
    It can replace the Claw attack with a use of Fire Breath if available.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 2
      die: 6
      bonus: 4
  - type: piercing
    base:
      dice: 4
      die: 6
      bonus: 4
  type: utility
- name: Claw
  damage:
  - type: slashing
    base:
      dice: 1
      die: 6
      bonus: 4
  type: utility
- name: Ram
  damage:
  - type: bludgeoning
    base:
      dice: 1
      die: 12
      bonus: 4
  type: utility
- name: "Fire Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 15
  on_pass: half
  on_fail: full
  damage:
  - type: fire
    base:
      dice: 7
      die: 8
      bonus: 0

---
# Chain Devil

*Large Monstrosity, Chaotic Evil*

### Actions

**Bite.** Melee Attack Roll: +7, reach 5 ft. Hit: 11 (2d6 + 4) Piercing damage, or 18 (4d6 + 4) Piercing damage if the chimera had Advantage on the attack roll.

**Claw.** Melee Attack Roll: +7, reach 5 ft. Hit: 7 (1d6 + 4) Slashing damage.

**Ram.** Melee Attack Roll: +7, reach 5 ft. Hit: 10 (1d12 + 4) Bludgeoning damage. If the target is a Medium or smaller creature, it has the Prone condition.

**Fire Breath (Recharge 5–6).** Dexterity Saving Throw: DC 15, each creature in a 15-foot Cone. Failure: 31 (7d8) Fire damage. Success: Half damage.

