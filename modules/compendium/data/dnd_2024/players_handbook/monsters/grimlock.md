---name: Grimlock
size: Large
type: Large Celestial
alignment: Lawful Good
ac: '18'
hp: 136 (16d10 + 48)
speed: 40 ft., Climb 40 ft., Swim 40 ft.
stats:
  str: 19
  dex: 18
  con: 16
  int: 16
  wis: 19
  cha: 18
cr: 10 (XP 5,900; PB +4)
traits:
- name: Immunities
  description: Poison; Charmed, Paralyzed, Poisoned, Restrained
- name: Celestial Restoration
  description: If the naga dies, it returns to life in 1d6 days and regains all its
    Hit Points unless Dispel Evil and Good is cast on its remains.
actions:
- name: Multiattack
  description: The naga makes two Bite attacks. It can replace any attack with a use
    of Poisonous Spittle.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 2
      die: 12
      bonus: 4
  - type: poison
    base:
      dice: 4
      die: 10
      bonus: 0
  type: utility
- name: Poisonous Spittle
  type: save
  ability: con
  dc: 16
  on_pass: half
  on_fail: full
  damage:
  - type: poison
    base:
      dice: 7
      die: 8
      bonus: 0
- name: Spellcasting
  description: 'The naga casts one of the following spells, requiring no Somatic or
    Material components and using Wisdom as the spellcasting ability (spell save DC
    16):'
- name: 'At Will:'
  description: Thaumaturgy
- name: '1/Day Each:'
  description: Clairvoyance, Cure Wounds (level 6 version), Flame Strike (level 6
    version), Geas, True Seeing

---
# Grimlock

*Large Celestial, Lawful Good*

### Actions

**Bite.** Melee Attack Roll: +8, reach 10 ft. Hit: 17 (2d12 + 4) Piercing damage plus 22 (4d10) Poison damage.

**Poisonous Spittle.** Constitution Saving Throw: DC 16, one creature the naga can see within 60 feet. Failure: 31 (7d8) Poison damage, and the target has the Blinded condition until the start of the naga’s next turn. Success: Half damage only.

