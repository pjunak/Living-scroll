---name: Doppelganger
size: Gargantuan
type: Gargantuan Dragon
alignment: Neutral
ac: '20'
hp: 356 (23d20 + 115)
speed: 20 ft., Swim 50 ft.
stats:
  str: 25
  dex: 10
  con: 20
  int: 10
  wis: 12
  cha: 12
cr: 17 (XP 18,000; PB +6)
traits:
- name: Resistances
  description: Fire
- name: Amphibious
  description: The dragon can breathe air and water.
actions:
- name: Multiattack
  description: The dragon makes three Bite attacks. It can replace one attack with
    a Tail attack.
- name: Bite
  damage:
  - type: piercing
    base:
      dice: 3
      die: 10
      bonus: 7
  - type: fire
    base:
      dice: 2
      die: 6
      bonus: 0
  type: utility
- name: Tail
  damage:
  - type: bludgeoning
    base:
      dice: 2
      die: 10
      bonus: 7
  type: utility
- name: "Steam Breath (Recharge 5\u20136)"
  type: save
  ability: con
  dc: 19
  on_pass: half
  on_fail: full
  damage:
  - type: fire
    base:
      dice: 16
      die: 6
      bonus: 0

---
# Doppelganger

*Gargantuan Dragon, Neutral*

### Actions

**Bite.** Melee Attack Roll: +13, reach 15 ft. Hit: 23 (3d10 + 7) Piercing damage plus 7 (2d6) Fire damage. Being underwater doesn’t grant Resistance to this Fire damage.

**Tail.** Melee Attack Roll: +13, reach 15 ft. Hit: 18 (2d10 + 7) Bludgeoning damage. If the target is a Huge or smaller creature, it has the Prone condition.

**Steam Breath (Recharge 5–6).** Constitution Saving Throw: DC 19, each creature in a 60-foot Cone. Failure: 56 (16d6) Fire damage. Success: Half damage. Failure or Success: Being underwater doesn’t grant Resistance to this Fire damage.

