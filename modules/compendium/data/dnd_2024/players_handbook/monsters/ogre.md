---name: Ogre
size: Large
type: Large Fiend
alignment: Lawful Evil
ac: '17'
hp: 119 (14d10 + 42)
speed: 30 ft., Fly 30 ft. (hover)
stats:
  str: 19
  dex: 11
  con: 16
  int: 14
  wis: 12
  cha: 15
cr: 7 (XP 2,900; PB +3)
traits:
- name: Resistances
  description: Cold
- name: Regeneration
  description: The oni regains 10 Hit Points at the start of each of its turns if
    it has at least 1 Hit Point.
actions:
- name: Multiattack
  description: The oni makes two Claw or Nightmare Ray attacks. It can replace one
    attack with a use of Spellcasting.
- name: Claw
  damage:
  - type: slashing
    base:
      dice: 1
      die: 12
      bonus: 4
  - type: necrotic
    base:
      dice: 2
      die: 8
      bonus: 0
  type: utility
- name: Nightmare Ray
  damage:
  - type: psychic
    base:
      dice: 2
      die: 6
      bonus: 2
  type: utility
- name: Shape-Shift
  description: "The oni shape-shifts into a Small or Medium Humanoid or a Large Giant,\
    \ or it returns to its true form. Other than its size, its game statistics are\
    \ the same in each form. Any equipment it is wearing or carrying isn\u2019t transformed."
- name: Spellcasting
  description: 'The oni casts one of the following spells, requiring no Material components
    and using Charisma as the spellcasting ability (spell save DC 13):'
- name: '1/Day Each:'
  description: Charm Person (level 2 version), Darkness, Gaseous Form, Sleep
- name: Invisibility
  description: The oni casts Invisibility on itself, requiring no spell components
    and using the same spellcasting ability as Spellcasting.

---
# Ogre

*Large Fiend, Lawful Evil*

### Actions

**Claw.** Melee Attack Roll: +7, reach 10 ft. Hit: 10 (1d12 + 4) Slashing damage plus 9 (2d8) Necrotic damage.

**Nightmare Ray.** Ranged Attack Roll: +5, range 60 ft. Hit: 9 (2d6 + 2) Psychic damage, and the target has the Frightened condition until the start of the oni’s next turn.

