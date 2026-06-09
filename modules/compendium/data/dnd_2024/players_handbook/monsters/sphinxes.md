---name: Sphinxes
size: Large
type: Large Fiend
alignment: Chaotic Evil
ac: '17'
hp: 135 (18d10 + 36)
speed: 40 ft.
stats:
  str: 18
  dex: 17
  con: 14
  int: 16
  wis: 15
  cha: 16
cr: 8 (XP 3,900; PB +3)
traits:
- name: Immunities
  description: Poison; Charmed, Poisoned
- name: Fiendish Restoration
  description: If it dies, the naga returns to life in 1d6 days and regains all its
    Hit Points. Only a Wish spell can prevent this trait from functioning.
actions:
- name: Multiattack
  description: The naga makes three attacks, using Bite or Necrotic Ray in any combination.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 1
      die: 6
      bonus: 4
  - type: poison
    base:
      dice: 4
      die: 6
      bonus: 0
  type: utility
- name: Necrotic Ray
  damage:
  - type: necrotic
    base:
      dice: 6
      die: 6
      bonus: 0
  type: utility
- name: Spellcasting
  description: 'The naga casts one of the following spells, requiring no Somatic or
    Material components and using Intelligence as the spellcasting ability (spell
    save DC 14):'
- name: 'At Will:'
  description: Detect Magic, Mage Hand, Minor Illusion, Water Breathing
- name: '2/Day Each:'
  description: Detect Thoughts, Dimension Door, Hold Person (level 3 version), Lightning
    Bolt (level 4 version)

---
# Sphinxes

*Large Fiend, Chaotic Evil*

### Actions

**Bite.** Melee Attack Roll: +7, reach 10 ft. Hit: 7 (1d6 + 4) Piercing damage plus 14 (4d6) Poison damage.

**Necrotic Ray.** Ranged Attack Roll: +6, range 60 ft. Hit: 21 (6d6) Necrotic damage.

