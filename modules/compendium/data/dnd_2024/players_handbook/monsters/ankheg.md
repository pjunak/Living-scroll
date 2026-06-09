---name: Ankheg
size: Medium
type: Medium or Small Humanoid
alignment: Neutral
ac: '16'
hp: 97 (15d8 + 30)
speed: 30 ft.
stats:
  str: 11
  dex: 18
  con: 14
  int: 16
  wis: 11
  cha: 10
cr: 8 (XP 3,900; PB +3)
traits:
- name: Resistances
  description: Poison
- name: Evasion
  description: "If the assassin is subjected to an effect that allows it to make a\
    \ Dexterity saving throw to take only half damage, the assassin instead takes\
    \ no damage if it succeeds on the save and only half damage if it fails. It can\u2019\
    t use this trait if it has the Incapacitated condition."
actions:
- name: Multiattack
  description: The assassin makes three attacks, using Shortsword or Light Crossbow
    in any combination.
- name: Shortsword
  damage:
  - type: piercing
    base:
      dice: 1
      die: 6
      bonus: 4
  - type: poison
    base:
      dice: 5
      die: 6
      bonus: 0
  type: utility
- name: Light Crossbow
  damage:
  - type: piercing
    base:
      dice: 1
      die: 8
      bonus: 4
  - type: poison
    base:
      dice: 6
      die: 6
      bonus: 0
  type: utility
- name: Cunning Action
  description: The assassin takes the Dash, Disengage, or Hide action.

---
# Ankheg

*Medium or Small Humanoid, Neutral*

### Actions

**Shortsword.** Melee Attack Roll: +7, reach 5 ft. Hit: 7 (1d6 + 4) Piercing damage plus 17 (5d6) Poison damage, and the target has the Poisoned condition until the start of the assassin’s next turn.

**Light Crossbow.** Ranged Attack Roll: +7, range 80/320 ft. Hit: 8 (1d8 + 4) Piercing damage plus 21 (6d6) Poison damage.

