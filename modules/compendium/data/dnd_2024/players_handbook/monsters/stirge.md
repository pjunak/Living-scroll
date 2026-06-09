---name: Stirge
size: Huge
type: Huge Giant
alignment: Neutral
ac: '17'
hp: 126 (11d12 + 55)
speed: 40 ft.
stats:
  str: 23
  dex: 15
  con: 20
  int: 10
  wis: 12
  cha: 9
cr: 7 (XP 2,900; PB +3)
traits: []
actions:
- name: Multiattack
  description: The giant makes two attacks, using Stone Club or Boulder in any combination.
- name: Stone Club
  damage:
  - type: bludgeoning
    base:
      dice: 3
      die: 10
      bonus: 6
  type: utility
- name: Boulder
  damage:
  - type: bludgeoning
    base:
      dice: 2
      die: 8
      bonus: 6
  type: utility
- name: "Deflect Missile (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 17
  on_pass: none
  on_fail: full
  damage:
  - type: force
    base:
      dice: 1
      die: 10
      bonus: 6

---
# Stirge

*Huge Giant, Neutral*

### Actions

**Stone Club.** Melee Attack Roll: +9, reach 15 ft. Hit: 22 (3d10 + 6) Bludgeoning damage.

**Boulder.** Ranged Attack Roll: +9, range 60/240 ft. Hit: 15 (2d8 + 6) Bludgeoning damage. If the target is a Large or smaller creature, it has the Prone condition.

**Deflect Missile (Recharge 5–6).** Trigger: The giant is hit by a ranged attack roll and takes Bludgeoning, Piercing, or Slashing damage from it. Response: The giant reduces the damage it takes from the attack by 11 (1d10 + 6), and if that damage is reduced to 0, the giant can redirect some of the attack’s force. Dexterity Saving Throw: DC 17, one creature the giant can see within 60 feet. Failure: 11 (1d10 + 6) Force damage.

