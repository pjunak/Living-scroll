---
name: Class Name
type: class
id: class:class-name
hit_die: d10
primary_ability:
  - STR
  - DEX
saves:
  - STR
  - CON
proficiencies:
  armor:
    - light
    - medium
    - heavy
    - shields
  weapons:
    - simple
    - martial
  tools: []
  skills_choose: 2
  skill_list:
    - Acrobatics
    - Athletics
spellcasting:
  ability: INT
  progression: full        # full | half | third | pact | none
  prepared: true           # true = prepares from class list / false = known spells
  has_spellbook: false     # true only for Wizard
  preparation_formula: "INT + level"   # only if prepared: true
  known_spells_table:      # only if prepared: false (level → count)
    '1': 2
    '2': 3
  known_cantrips_table:    # cantrips known per level
    '1': 4
    '4': 5
progression:
  - level: 1
    features:
      - Feature Name 1
      - Feature Name 2
    grants: {}
multiclass_requirements:
  STR|DEX: 13

# Dynamic management tabs granted by this class.
# Each entry becomes a DISTINCT TOP-LEVEL TAB in the Character Builder.
# Tab name = label field (disambiguated by class name for multiclass).
#
# Types:
#   spell_collection   – Open-ended list, no hard cap (Wizard spellbook)
#   spell_preparation  – Subset selector with formula cap (prepared casters)
#   spell_known        – Fixed-size list with swap (Sorcerer, Bard, Warlock)
#   feature_selection  – Choice picker with prerequisites (Invocations, Maneuvers)
management:
  # Open-ended spell collection (Wizard spellbook)
  - id: spellbook
    label: "Spellbook"
    type: spell_collection
    source: class_spell_list
    initial_count: 6
    gain_per_level: 2
    description: "Spells transcribed into your spellbook."

  # Formula-capped preparation (Wizard prepared, Cleric, Druid, Paladin…)
  - id: prepared
    label: "Prepared Spells"
    type: spell_preparation
    source: spellbook             # or class_spell_list
    max_formula: "INT + level"
    changeable_on: long_rest      # long_rest | level_up | short_rest

  # Table-capped known spells (Sorcerer, Warlock…)
  # - id: known_spells
  #   label: "Known Spells"
  #   type: spell_known
  #   source: class_spell_list
  #   max_table: known_spells_table  # references spellcasting.known_spells_table
  #   swap_count: 1
  #   changeable_on: level_up

  # Feature selection with table cap (Warlock Invocations, Battle Master Maneuvers)
  # - id: invocations
  #   label: "Eldritch Invocations"
  #   type: feature_selection
  #   source: invocation_list
  #   max_table: invocations_known_table
  #   changeable_on: level_up
---

# Class Name

Class descriptive text.

### Level 1: Feature Name 1
Details about feature 1.

