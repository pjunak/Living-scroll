---name: Imp
size: Medium
type: Medium Fiend
alignment: Neutral Evil
ac: '15'
hp: 66 (12d8 + 12)
speed: 30 ft., Fly 60 ft.
stats:
  str: 8
  dex: 17
  con: 13
  int: 15
  wis: 12
  cha: 20
cr: 4 (XP 1,100; PB +2)
traits:
- name: Resistances
  description: Cold, Fire, Poison, Psychic
- name: Succubus Form
  description: "When the incubus finishes a Long Rest, it can shape-shift into a Succubus,\
    \ using that stat block instead of this one. Any equipment it is wearing or carrying\
    \ isn\u2019t transformed."
actions:
- name: Multiattack
  description: The incubus makes two Restless Touch attacks.
- name: Restless Touch
  damage:
  - type: psychic
    base:
      dice: 3
      die: 6
      bonus: 5
  type: utility
- name: Spellcasting
  description: 'The incubus casts one of the following spells, requiring no Material
    components and using Charisma as the spellcasting ability (spell save DC 15):'
- name: 'At Will:'
  description: Disguise Self, Etherealness
- name: '1/Day Each:'
  description: Dream, Hypnotic Pattern
- name: Nightmare (Recharge 6)
  type: save
  ability: wis
  dc: 15
  on_pass: none
  on_fail: full
  damage:
  - type: psychic
    base:
      dice: 4
      die: 8
      bonus: 0

---
# Imp

*Medium Fiend, Neutral Evil*

### Actions

**Restless Touch.** Melee Attack Roll: +7, reach 5 ft. Hit: 15 (3d6 + 5) Psychic damage, and the target is cursed for 24 hours or until the incubus dies. Until the curse ends, the target gains no benefit from finishing Short Rests.

**Nightmare (Recharge 6).** Wisdom Saving Throw: DC 15, one creature the incubus can see within 60 feet. Failure: If the target has 20 Hit Points or fewer, it has the Unconscious condition for 1 hour, until it takes damage, or until a creature within 5 feet of it takes an action to wake it. Otherwise, the target takes 18 (4d8) Psychic damage.

