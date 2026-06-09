---name: Mummy
size: Medium
type: Medium or Small Undead
alignment: Lawful Evil
ac: '11'
hp: 58 (9d8 + 18)
speed: 20 ft.
stats:
  str: 16
  dex: 8
  con: 15
  int: 6
  wis: 12
  cha: 12
cr: 3 (XP 700; PB +2)
traits:
- name: Vulnerabilities
  description: Fire
- name: Immunities
  description: Necrotic, Poison; Charmed, Exhaustion, Frightened, Paralyzed, Poisoned
actions:
- name: Multiattack
  description: The mummy makes two Rotting Fist attacks and uses Dreadful Glare.
- name: Rotting Fist
  damage:
  - type: bludgeoning
    base:
      dice: 1
      die: 10
      bonus: 3
  - type: necrotic
    base:
      dice: 3
      die: 6
      bonus: 0
  type: utility
- name: Dreadful Glare
  type: save
  ability: wis
  dc: 11
  on_pass: none
  on_fail: full

---
# Mummy

*Medium or Small Undead, Lawful Evil*

### Actions

**Rotting Fist.** Melee Attack Roll: +5, reach 5 ft. Hit: 8 (1d10 + 3) Bludgeoning damage plus 10 (3d6) Necrotic damage. If the target is a creature, it is cursed. While cursed, the target can’t regain Hit Points, its Hit Point maximum doesn’t return to normal when finishing a Long Rest, and its Hit Point maximum decreases by 10 (3d6) every 24 hours that elapse. A creature dies and turns to dust if reduced to 0 Hit Points by this attack.

**Dreadful Glare.** Wisdom Saving Throw: DC 11, one creature the mummy can see within 60 feet. Failure: The target has the Frightened condition until the end of the mummy’s next turn. Success: The target is immune to this mummy’s Dreadful Glare for 24 hours.

