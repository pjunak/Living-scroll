---
name: Feat Name
type: feat
category: general # general, origin, fighting_style, epic_boon
prerequisite: "Level 4+, Spellcasting or Pact Magic Feature" # Plaintext string of prerequisites
id: feat:feat-name
attribute_increase: # Attributes this feat allows players to increase.
  - STR
  - DEX
  - CON
  - INT
  - WIS
  - CHA
proficiency: # Specific skill or saving throw proficiencies granted
  - Perception
expertise: null
repeatable: false # Can this feat be taken multiple times?
grants: # Complex mechanics granted by the feat
  resistances:
    - fire
  spells:
    - spell:light
  actions:
    - name: Feat Action
      type: utility
      reset: short_rest # none, short_rest, long_rest
---

# Feat Name

*Prerequisite: Level 4+, Spellcasting or Pact Magic Feature*

You gain the following benefits.

**Ability Score Increase.** Increase your Strength, Dexterity, Constitution, Intelligence, Wisdom, or Charisma score by 1, to a maximum of 20.

**Trait 1.** Describe the first trait of the feat.

**Trait 2.** Describe the second trait of the feat.
