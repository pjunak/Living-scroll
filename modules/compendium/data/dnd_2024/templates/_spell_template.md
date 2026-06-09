---
name: Spell Name
type: spell
id: spell:spell-name
level: 0 # 0 for Cantrip, 1-9 for Leveled Spells
school: Evocation # Abjuration, Conjuration, Divination, Enchantment, Evocation, Illusion, Necromancy, Transmutation
ritual: false # true or false
casting_time: 1 Action # 1 Action, 1 Bonus Action, 1 Reaction, 1 Minute, 10 Minutes, 1 Hour, 8 Hours, 12 Hours, 24 Hours
range: 60 feet # Self, Touch, X feet, Sight, Unlimited
components: # V (Verbal), S (Somatic), M (Material)
  - V
  - S
  - M
material: A bit of down or feathers # Component description. Include cost in GP if applicable.
duration: Instantaneous # Instantaneous, 1 Round, 1 Minute, 10 Minutes, 1 Hour, 8 Hours, 24 Hours, Until Dispelled
concentration: false # true or false
classes: # Artificer, Bard, Cleric, Druid, Fighter, Monk, Paladin, Ranger, Rogue, Sorcerer, Warlock, Wizard
  - Wizard
  - Sorcerer
actions:
  # First Action / Primary Effect
  - type: save # save, attack, utility, heal
    ability: dex # str, dex, con, int, wis, cha (Applicable if type is 'save')
    on_pass: half # half, none (Applicable if type is 'save')
    on_fail: full # full, none (Applicable if type is 'save')
    
    damage:
      - type: fire # acid, bludgeoning, cold, fire, force, lightning, necrotic, piercing, poison, psychic, radiant, slashing, thunder
        base:
          dice: 8 # Number of dice (e.g. 8)
          die: 6 # Size of die (e.g. 4, 6, 8, 10, 12, 20)
          bonus: 0 # Flat modifier added to the roll
        scaling: # Optional. Defines how damage increases at higher levels.
          dice_per_slot: 1
          die: 6
          mode: spell_level # spell_level (for leveled spells), character_level (for cantrips)
          
    healing: # Optional.
      base:
        dice: 0
        die: 0
        bonus: 0 # Can be an integer or special string like 'spellcasting_modifier'
        
    conditions: # Optional. Status effects imposed by this action.
      - name: prone # blinded, charmed, deafened, frightened, grappled, incapacitated, invisible, paralyzed, petrified, poisoned, prone, restrained, stunned, unconscious, exhaustion
        duration: 1 minute
        save_ends: end_of_turn # start_of_turn, end_of_turn, none
        
  # Second Action / Secondary Effect (If the spell does multiple things)
  - type: utility
    conditions:
      - name: deafened
        duration: 1 minute
        save_ends: none
---

# Spell Name
*0-Level Evocation (Sorcerer, Wizard)*
**Casting Time:** 1 Action
**Range:** 60 feet
**Components:** V, S, M (A bit of down or feathers)
**Duration:** Instantaneous

Plaintext descriptive rules here. Ensure all mechanics are described thoroughly for human reading, while the YAML frontmatter handles the strict logic for the engine.
