---
name: Weapon Name
type: Weapon
id: weapon:weapon-name
category: Martial Melee Weapons # Simple Melee Weapons, Simple Ranged Weapons, Martial Melee Weapons, Martial Ranged Weapons
cost: 15 GP # Price in GP, SP, or CP
weight: 3 lb. # Weight string
damage:
  - type: slashing # acid, bludgeoning, cold, fire, force, lightning, necrotic, piercing, poison, psychic, radiant, slashing, thunder
    base:
      dice: 1 # Number of dice
      die: 8 # Size of die
      bonus: 0
properties: # List of weapon properties
  - name: versatile # ammunition, finesse, heavy, light, loading, range, reach, special, thrown, two-handed, versatile
    damage:
      type: slashing
      base:
        dice: 1
        die: 10
mastery: Sap # Cleave, Graze, Nick, Push, Sap, Slow, Topple, Vex
tags:
  - weapon
  - sword # sword, axe, bow, crossbow, hammer, polearm, etc.
---

# Weapon Name
*Weapon, Martial Melee Weapons*

**Damage:** 1d8 Slashing
**Properties:** Versatile(1d10)
**Mastery:** Sap
**Weight:** 3 lb.
**Cost:** 15 GP

Extra description.
