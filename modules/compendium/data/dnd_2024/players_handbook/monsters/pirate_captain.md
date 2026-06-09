---name: Pirate Captain
size: Medium
type: Medium or Small Humanoid
alignment: Neutral
ac: '17'
hp: 84 (13d8 + 26)
speed: 30 ft.
stats:
  str: 10
  dex: 18
  con: 14
  int: 10
  wis: 14
  cha: 17
cr: 6 (XP 2,300; PB +3)
traits: []
actions:
- name: Multiattack
  description: The pirate makes three attacks, using Rapier or Pistol in any combination.
- name: Rapier
  damage:
  - type: piercing
    base:
      dice: 2
      die: 8
      bonus: 4
  type: utility
- name: Pistol
  damage:
  - type: piercing
    base:
      dice: 2
      die: 10
      bonus: 4
  type: utility
- name: "Captain\u2019s Charm"
  type: save
  ability: wis
  dc: 14
  on_pass: none
  on_fail: full
- name: Riposte
  description: 'Trigger: The pirate is hit by a melee attack roll while holding a
    weapon. Response: The pirate adds 3 to its AC against that attack, possibly causing
    it to miss. On a miss, the pirate makes one Rapier attack against the triggering
    creature if within range.'

---
# Pirate Captain

*Medium or Small Humanoid, Neutral*

### Actions

**Rapier.** Melee Attack Roll: +7, reach 5 ft. Hit: 13 (2d8 + 4) Piercing damage, and the pirate has Advantage on the next attack roll it makes before the end of this turn.

**Pistol.** Ranged Attack Roll: +7, range 30/90 ft. Hit: 15 (2d10 + 4) Piercing damage.

**Captain’s Charm.** Wisdom Saving Throw: DC 14, one creature the pirate can see within 30 feet. Failure: The target has the Charmed condition until the start of the pirate’s next turn.

