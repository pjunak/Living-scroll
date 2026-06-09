---name: Mass Cure Wounds
type: spell
level: 5
school: Abjuration
ritual: false
casting_time: Action
range: 60 feet
components:
- V
- S
material: ''
duration: Instantaneous
concentration: false
classes:
- Bard
- Cleric
- Druid
id: spell:mass-cure-wounds
material_price: ''
actions:
- type: heal
  healing:
    base:
      dice: 5
      die: 8
      bonus: spellcasting_modifier
---
# Mass Cure Wounds
*5th-Level Abjuration (Bard, Cleric, Druid)*
**Casting Time:** Action
**Range:** 60 feet
**Components:** V, S
**Duration:** Instantaneous

A wave of healing energy washes out from a point you can see within range. Choose up to six creatures in a 30-foot-radius Sphere centered on that point. Each target regains Hit Points equal to 5d8 plus your spellcasting ability modifier.

**Using a Higher-Level Spell Slot.** The healing increases by 1d8 for each spell slot level above 5.