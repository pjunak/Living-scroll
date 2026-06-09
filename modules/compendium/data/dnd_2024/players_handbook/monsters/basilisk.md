---name: Basilisk
size: Medium
type: Medium Fiend (Devil)
alignment: Lawful Evil
ac: '13'
hp: 58 (9d8 + 18)
speed: 30 ft.
stats:
  str: 16
  dex: 15
  con: 15
  int: 9
  wis: 11
  cha: 14
cr: 3 (XP 700; PB +2)
traits:
- name: Resistances
  description: Cold
- name: Immunities
  description: Fire, Poison; Frightened, Poisoned
- name: Magic Resistance
  description: The devil has Advantage on saving throws against spells and other magical
    effects.
actions:
- name: Multiattack
  description: The devil makes one Beard attack and one Infernal Glaive attack.
- name: Beard
  damage:
  - type: piercing
    base:
      dice: 1
      die: 8
      bonus: 3
  type: utility
- name: Infernal Glaive
  type: save
  ability: con
  dc: 12
  on_pass: none
  on_fail: full
  damage:
  - type: slashing
    base:
      dice: 1
      die: 10
      bonus: 3

---
# Basilisk

*Medium Fiend (Devil), Lawful Evil*

### Actions

**Beard.** Melee Attack Roll: +5, reach 5 ft. Hit: 7 (1d8 + 3) Piercing damage, and the target has the Poisoned condition until the start of the devil’s next turn. Until this poison ends, the target can’t regain Hit Points.

**Infernal Glaive.** Melee Attack Roll: +5, reach 10 ft. Hit: 8 (1d10 + 3) Slashing damage. If the target is a creature and doesn’t already have an infernal wound, it is subjected to the following effect. Constitution Saving Throw: DC 12. Failure: The target receives an infernal wound. While wounded, the target loses 5 (1d10) Hit Points at the start of each of its turns. The wound closes after 1 minute, after a spell restores Hit Points to the target, or after the target or a creature within 5 feet of it takes an action to stanch the wound, doing so by succeeding on a DC 12 Wisdom (Medicine) check.

