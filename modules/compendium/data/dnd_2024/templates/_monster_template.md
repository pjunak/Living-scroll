---
name: Monster Name
type: monster
id: monster:monster-name
size: Medium # Tiny, Small, Medium, Large, Huge, Gargantuan
creature_type: Humanoid # Aberration, Beast, Celestial, Construct, Dragon, Elemental, Fey, Fiend, Giant, Humanoid, Monstrosity, Ooze, Plant, Undead
alignment: Any alignment # Lawful Good, Neutral Good, Chaotic Good, Lawful Neutral, True Neutral, Chaotic Neutral, Lawful Evil, Neutral Evil, Chaotic Evil, Unaligned, Any alignment
ac:
  base: 15
  source: Natural Armor # Natural Armor, Leather Armor, Shield, etc.
hp:
  average: 11
  formula: 2d8 + 2
speed:
  walk: 30 # Walk speed in feet
  fly: 0 # Fly speed in feet
  swim: 0 # Swim speed in feet
  climb: 0 # Climb speed in feet
  burrow: 0 # Burrow speed in feet
ability_scores:
  STR: 10
  DEX: 10
  CON: 10
  INT: 10
  WIS: 10
  CHA: 10
saves: # Proficient saving throws
  - STR
  - DEX
skills: # Proficient skills. Acrobatics, Animal Handling, Arcana, Athletics, Deception, History, Insight, Intimidation, Investigation, Medicine, Nature, Perception, Performance, Persuasion, Religion, Sleight of Hand, Stealth, Survival
  - Perception
  - Stealth
resistances: # acid, bludgeoning, cold, fire, force, lightning, necrotic, piercing, poison, psychic, radiant, slashing, thunder
  - fire
immunities: # Damage immunities
  - poison
condition_immunities: # condition names
  - poisoned
senses:
  darkvision: 60
  blindsight: 0
  tremorsense: 0
  truesight: 0
  passive_perception: 12
languages: # Common, Elvish, Dwarvish, etc.
  - Common
cr: "1" # Challenge Rating (e.g. 1/8, 1/4, 1/2, 1, 2... 30)
xp: 200 # Experience Points
traits: # Passive abilities
  - name: Pack Tactics
    description: The monster has advantage on attack rolls against a creature if at least one of the monster's allies is within 5 feet of the creature and the ally isn't incapacitated.
actions: # Active abilities used in combat
  - name: Multiattack
    type: utility
    description: The monster makes two melee attacks.
  - name: Shortsword
    type: attack
    attack_type: melee_weapon # melee_weapon, ranged_weapon, melee_spell, ranged_spell
    reach: 5 # feet
    target: one target
    hit_bonus: 4
    damage:
      - type: piercing
        base:
          dice: 1
          die: 6
          bonus: 2
bonus_actions: []
reactions: []
legendary_actions: []
---

# Monster Name

*Medium Humanoid, Any alignment*

**Armor Class** 15 (Natural Armor)
**Hit Points** 11 (2d8 + 2)
**Speed** 30 ft.

| STR | DEX | CON | INT | WIS | CHA |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 10 (+0) | 10 (+0) | 10 (+0) | 10 (+0) | 10 (+0) | 10 (+0) |

**Saving Throws** Str +2, Dex +2
**Skills** Perception +2, Stealth +2
**Damage Resistances** Fire
**Damage Immunities** Poison
**Condition Immunities** Poisoned
**Senses** Darkvision 60 ft., passive Perception 12
**Languages** Common
**Challenge** 1 (200 XP)

### Traits

**Pack Tactics.** The monster has advantage on attack rolls against a creature if at least one of the monster's allies is within 5 feet of the creature and the ally isn't incapacitated.

### Actions

**Multiattack.** The monster makes two melee attacks.

**Shortsword.** *Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 5 (1d6 + 2) piercing damage.
