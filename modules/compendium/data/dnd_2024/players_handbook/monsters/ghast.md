---name: Ghast
size: Medium
type: Medium Undead
alignment: Neutral
ac: '11'
hp: 45 (10d8)
speed: 5 ft., Fly 40 ft. (hover)
stats:
  str: 7
  dex: 13
  con: 10
  int: 10
  wis: 12
  cha: 17
cr: 4 (XP 1,100; PB +2)
traits:
- name: Resistances
  description: Acid, Bludgeoning, Cold, Fire, Lightning, Piercing, Slashing, Thunder
- name: Immunities
  description: Necrotic, Poison; Charmed, Exhaustion, Frightened, Grappled, Paralyzed,
    Petrified, Poisoned, Prone, Restrained
- name: Ethereal Sight
  description: The ghost can see 60 feet into the Ethereal Plane when it is on the
    Material Plane.
- name: Incorporeal Movement
  description: The ghost can move through other creatures and objects as if they were
    Difficult Terrain. It takes 5 (1d10) Force damage if it ends its turn inside an
    object.
actions:
- name: Multiattack
  description: The ghost makes two Withering Touch attacks.
- name: Withering Touch
  damage:
  - type: necrotic
    base:
      dice: 3
      die: 10
      bonus: 3
  type: utility
- name: Etherealness
  description: "The ghost casts the Etherealness spell, requiring no spell components\
    \ and using Charisma as the spellcasting ability. The ghost is visible on the\
    \ Material Plane while on the Border Ethereal and vice versa, but it can\u2019\
    t affect or be affected by anything on the other plane."
- name: Horrific Visage
  type: save
  ability: wis
  dc: 13
  on_pass: none
  on_fail: full
  damage:
  - type: psychic
    base:
      dice: 2
      die: 6
      bonus: 3
- name: Possession (Recharge 6)
  type: save
  ability: cha
  dc: 13
  on_pass: none
  on_fail: full

---
# Ghast

*Medium Undead, Neutral*

### Actions

**Withering Touch.** Melee Attack Roll: +5, reach 5 ft. Hit: 19 (3d10 + 3) Necrotic damage.

**Horrific Visage.** Wisdom Saving Throw: DC 13, each creature in a 60-foot Cone that can see the ghost and isn’t an Undead. Failure: 10 (2d6 + 3) Psychic damage, and the target has the Frightened condition until the start of the ghost’s next turn. Success: The target is immune to this ghost’s Horrific Visage for 24 hours.

**Possession (Recharge 6).** Charisma Saving Throw: DC 13, one Humanoid the ghost can see within 5 feet. Failure: The target is possessed by the ghost; the ghost disappears, and the target has the Incapacitated condition and loses control of its body. The ghost now controls the body, but the target retains awareness. The ghost can’t be targeted by any attack, spell, or other effect, except ones that specifically target Undead. The ghost’s game statistics are the same, except it uses the possessed target’s Speed, as well as the target’s Strength, Dexterity, and Constitution modifiers.

