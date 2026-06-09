---name: Slaad Tadpole
size: Large
type: Large Celestial (Angel)
alignment: Lawful Good
ac: '21'
hp: 297 (22d10 + 176)
speed: 50 ft., Fly 150 ft. (hover)
stats:
  str: 26
  dex: 22
  con: 26
  int: 25
  wis: 25
  cha: 30
cr: 21 (XP 33,000; PB +7)
traits:
- name: Immunities
  description: Poison, Radiant; Charmed, Exhaustion, Frightened, Poisoned
- name: Divine Awareness
  description: The solar knows if it hears a lie.
- name: Exalted Restoration
  description: If the solar dies outside Mount Celestia, its body disappears, and
    it gains a new body instantly, reviving with all its Hit Points somewhere in Mount
    Celestia.
- name: Legendary Resistance (4/Day)
  description: If the solar fails a saving throw, it can choose to succeed instead.
- name: Magic Resistance
  description: The solar has Advantage on saving throws against spells and other magical
    effects.
actions:
- name: Multiattack
  description: The solar makes two Flying Sword attacks. It can replace one attack
    with a use of Slaying Bow.
- name: Flying Sword
  damage:
  - type: slashing
    base:
      dice: 4
      die: 6
      bonus: 8
  - type: radiant
    base:
      dice: 8
      die: 8
      bonus: 0
  type: utility
- name: Slaying Bow
  type: save
  ability: dex
  dc: 21
  on_pass: none
  on_fail: full
  damage:
  - type: piercing
    base:
      dice: 4
      die: 8
      bonus: 6
  - type: radiant
    base:
      dice: 8
      die: 8
      bonus: 0
- name: Spellcasting
  description: 'The solar casts one of the following spells, requiring no Material
    components and using Charisma as the spellcasting ability (spell save DC 25):'
- name: 'At Will:'
  description: Detect Evil and Good
- name: '1/Day Each:'
  description: Commune, Control Weather, Dispel Evil and Good, Resurrection
- name: Divine Aid (3/Day)
  description: The solar casts Cure Wounds (level 2 version), Lesser Restoration,
    or Remove Curse, using the same spellcasting ability as Spellcasting.
- name: Blinding Gaze
  type: save
  ability: con
  dc: 25
  on_pass: none
  on_fail: full
- name: Radiant Teleport
  type: save
  ability: dex
  dc: 25
  on_pass: half
  on_fail: full
  damage:
  - type: radiant
    base:
      dice: 2
      die: 10
      bonus: 0

---
# Slaad Tadpole

*Large Celestial (Angel), Lawful Good*

### Actions

**Flying Sword.** Melee or Ranged Attack Roll: +15, reach 10 ft. or range 120 ft. Hit: 22 (4d6 + 8) Slashing damage plus 36 (8d8) Radiant damage. Hit or Miss: The sword magically returns to the solar’s hand or hovers within 5 feet of the solar immediately after a ranged attack.

**Slaying Bow.** Dexterity Saving Throw: DC 21, one creature the solar can see within 600 feet. Failure: If the creature has 100 Hit Points or fewer, it dies. It otherwise takes 24 (4d8 + 6) Piercing damage plus 36 (8d8) Radiant damage.

**Blinding Gaze.** Constitution Saving Throw: DC 25, one creature the solar can see within 120 feet. Failure: The target has the Blinded condition for 1 minute. Failure or Success: The solar can’t take this action again until the start of its next turn.

**Radiant Teleport.** The solar teleports up to 60 feet to an unoccupied space it can see. Dexterity Saving Throw: DC 25, each creature in a 10-foot Emanation originating from the solar at its destination space. Failure: 11 (2d10) Radiant damage. Success: Half damage.

