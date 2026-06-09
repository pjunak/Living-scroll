---name: Pirate
size: Medium
type: Medium or Small Humanoid
alignment: Neutral
ac: '14'
hp: 33 (6d8 + 6)
speed: 30 ft.
stats:
  str: 10
  dex: 16
  con: 12
  int: 8
  wis: 12
  cha: 14
cr: 1 (XP 200; PB +2)
traits: []
actions:
- name: Multiattack
  description: The pirate makes two Dagger attacks. It can replace one attack with
    a use of Enthralling Panache.
- name: Dagger
  damage:
  - type: piercing
    base:
      dice: 1
      die: 4
      bonus: 3
  type: utility
- name: Enthralling Panache
  type: save
  ability: wis
  dc: 12
  on_pass: none
  on_fail: full

---
# Pirate

*Medium or Small Humanoid, Neutral*

### Actions

**Dagger.** Melee or Ranged Attack Roll: +5, reach 5 ft. or range 20/60 ft. Hit: 5 (1d4 + 3) Piercing damage.

**Enthralling Panache.** Wisdom Saving Throw: DC 12, one creature the pirate can see within 30 feet. Failure: The target has the Charmed condition until the start of the pirate’s next turn.

