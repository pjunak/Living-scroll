---name: Kobold Warrior
size: Gargantuan
type: Gargantuan Monstrosity (Titan)
alignment: Chaotic Evil
ac: '18'
hp: 481 (26d20 + 208)
speed: 30 ft., Swim 120 ft.
stats:
  str: 30
  dex: 11
  con: 26
  int: 22
  wis: 18
  cha: 20
cr: 23 (XP 50,000, or 62,000 in lair; PB +7)
traits:
- name: Immunities
  description: Cold, Lightning; Frightened, Grappled, Paralyzed, Restrained
- name: Amphibious
  description: The kraken can breathe air and water.
- name: Legendary Resistance (4/Day, or 5/Day in Lair)
  description: If the kraken fails a saving throw, it can choose to succeed instead.
- name: Siege Monster
  description: The kraken deals double damage to objects and structures.
actions:
- name: Multiattack
  description: The kraken makes two Tentacle attacks and uses Fling, Lightning Strike,
    or Swallow.
- name: Tentacle
  damage:
  - type: bludgeoning
    base:
      dice: 4
      die: 6
      bonus: 10
  type: utility
- name: Fling
  type: save
  ability: dex
  dc: 25
  on_pass: half
  on_fail: full
  damage:
  - type: bludgeoning
    base:
      dice: 4
      die: 8
      bonus: 0
- name: Lightning Strike
  type: save
  ability: dex
  dc: 23
  on_pass: half
  on_fail: full
  damage:
  - type: lightning
    base:
      dice: 6
      die: 10
      bonus: 0
- name: Swallow
  type: save
  ability: dex
  dc: 25
  on_pass: none
  on_fail: full
  damage:
  - type: piercing
    base:
      dice: 3
      die: 8
      bonus: 10
  - type: acid
    base:
      dice: 7
      die: 6
      bonus: 0
- name: Storm Bolt
  description: The kraken uses Lightning Strike.
- name: Toxic Ink
  type: save
  ability: con
  dc: 23
  on_pass: none
  on_fail: full

---
# Kobold Warrior

*Gargantuan Monstrosity (Titan), Chaotic Evil*

### Actions

**Tentacle.** Melee Attack Roll: +17, reach 30 ft. Hit: 24 (4d6 + 10) Bludgeoning damage. The target has the Grappled condition (escape DC 20) from one of ten tentacles, and it has the Restrained condition until the grapple ends.

**Fling.** The kraken throws a Large or smaller creature Grappled by it to a space it can see within 60 feet of itself that isn’t in the air. Dexterity Saving Throw: DC 25, the creature thrown and each creature in the destination space. Failure: 18 (4d8) Bludgeoning damage, and the target has the Prone condition. Success: Half damage only.

**Lightning Strike.** Dexterity Saving Throw: DC 23, one creature the kraken can see within 120 feet. Failure: 33 (6d10) Lightning damage. Success: Half damage.

**Swallow.** Dexterity Saving Throw: DC 25, one creature Grappled by the kraken (it can have up to four creatures swallowed at a time). Failure: 23 (3d8 + 10) Piercing damage. If the target is Large or smaller, it is swallowed and no longer Grappled. A swallowed creature has the Restrained condition, has Total Cover against attacks and other effects outside the kraken, and takes 24 (7d6) Acid damage at the start of each of its turns.

**Toxic Ink.** Constitution Saving Throw: DC 23, each creature in a 15-foot Emanation originating from the kraken while it is underwater. Failure: The target has the Blinded and Poisoned conditions until the end of the kraken’s next turn. The kraken then moves up to its Speed. Failure or Success: The kraken can’t take this action again until the start of its next turn.

