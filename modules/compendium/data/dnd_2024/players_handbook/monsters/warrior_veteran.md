---name: Warrior Veteran
size: Medium
type: Medium or Small Humanoid
alignment: Neutral
ac: '17'
hp: 65 (10d8 + 20)
speed: 30 ft.
stats:
  str: 16
  dex: 13
  con: 14
  int: 10
  wis: 11
  cha: 10
cr: 3 (XP 700; PB +2)
traits: []
actions:
- name: Multiattack
  description: The warrior makes two Greatsword or Heavy Crossbow attacks.
- name: Greatsword
  damage:
  - type: slashing
    base:
      dice: 2
      die: 6
      bonus: 3
  type: utility
- name: Heavy Crossbow
  damage:
  - type: piercing
    base:
      dice: 2
      die: 10
      bonus: 1
  type: utility
- name: Parry
  description: 'Trigger: The warrior is hit by a melee attack roll while holding a
    weapon. Response: The warrior adds 2 to its AC against that attack, possibly causing
    it to miss.'

---
# Warrior Veteran

*Medium or Small Humanoid, Neutral*

### Actions

**Greatsword.** Melee Attack Roll: +5, reach 5 ft. Hit: 10 (2d6 + 3) Slashing damage.

**Heavy Crossbow.** Ranged Attack Roll: +3, range 100/400 ft. Hit: 12 (2d10 + 1) Piercing damage.

