---name: Mummies
size: Large
type: Large Fiend (Demon)
alignment: Chaotic Evil
ac: '18'
hp: 184 (16d10 + 96)
speed: 20 ft., Fly 30 ft.
stats:
  str: 21
  dex: 10
  con: 22
  int: 19
  wis: 12
  cha: 15
cr: 13 (XP 10,000; PB +5)
traits:
- name: Resistances
  description: Cold, Fire, Lightning
- name: Immunities
  description: Poison; Frightened, Poisoned
- name: Demonic Restoration
  description: If the nalfeshnee dies outside the Abyss, its body dissolves into ichor,
    and it gains a new body instantly, reviving with all its Hit Points somewhere
    in the Abyss.
- name: Magic Resistance
  description: The nalfeshnee has Advantage on saving throws against spells and other
    magical effects.
actions:
- name: Multiattack
  description: The nalfeshnee makes three Rend attacks.
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 2
      die: 10
      bonus: 5
  - type: force
    base:
      dice: 2
      die: 10
      bonus: 0
  type: utility
- name: Teleport
  description: The nalfeshnee teleports up to 120 feet to an unoccupied space it can
    see.
- name: "Horror Nimbus (Recharge 5\u20136)"
  type: save
  ability: wis
  dc: 15
  on_pass: none
  on_fail: full
  damage:
  - type: psychic
    base:
      dice: 8
      die: 6
      bonus: 0
- name: Pursuit
  description: 'Trigger: Another creature the nalfeshnee can see ends its move within
    120 feet of the nalfeshnee. Response: The nalfeshnee uses Teleport, but its destination
    space must be within 10 feet of the triggering creature.'

---
# Mummies

*Large Fiend (Demon), Chaotic Evil*

### Actions

**Rend.** Melee Attack Roll: +10, reach 10 ft. Hit: 16 (2d10 + 5) Slashing damage plus 11 (2d10) Force damage.

**Horror Nimbus (Recharge 5–6).** Wisdom Saving Throw: DC 15, each creature in a 15-foot Emanation originating from the nalfeshnee. Failure: 28 (8d6) Psychic damage, and the target has the Frightened condition for 1 minute, until it takes damage, or until it ends its turn with the nalfeshnee out of line of sight. Success: The target is immune to this nalfeshnee’s Horror Nimbus for 24 hours.

