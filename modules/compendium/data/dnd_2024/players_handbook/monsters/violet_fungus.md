---name: Violet Fungus
size: Large
type: Large Fiend (Demon)
alignment: Chaotic Evil
ac: '15'
hp: 152 (16d10 + 64)
speed: 40 ft., Fly 60 ft.
stats:
  str: 17
  dex: 15
  con: 18
  int: 8
  wis: 13
  cha: 8
cr: 6 (XP 2,300; PB +3)
traits:
- name: Resistances
  description: Cold, Fire, Lightning
- name: Immunities
  description: Poison; Poisoned
- name: Demonic Restoration
  description: If the vrock dies outside the Abyss, its body dissolves into ichor,
    and it gains a new body instantly, reviving with all its Hit Points somewhere
    in the Abyss.
- name: Magic Resistance
  description: The vrock has Advantage on saving throws against spells and other magical
    effects.
actions:
- name: Multiattack
  description: The vrock makes two Shred attacks.
- name: Shred
  damage:
  - type: piercing
    base:
      dice: 2
      die: 6
      bonus: 3
  - type: poison
    base:
      dice: 3
      die: 6
      bonus: 0
  type: utility
- name: Spores (Recharge 6)
  type: save
  ability: con
  dc: 15
  on_pass: none
  on_fail: full
  damage:
  - type: poison
    base:
      dice: 1
      die: 10
      bonus: 0
- name: Stunning Screech (1/Day)
  type: save
  ability: con
  dc: 15
  on_pass: none
  on_fail: full
  damage:
  - type: thunder
    base:
      dice: 3
      die: 6
      bonus: 0

---
# Violet Fungus

*Large Fiend (Demon), Chaotic Evil*

### Actions

**Shred.** Melee Attack Roll: +6, reach 5 ft. Hit: 10 (2d6 + 3) Piercing damage plus 10 (3d6) Poison damage.

**Spores (Recharge 6).** Constitution Saving Throw: DC 15, each creature in a 20-foot Emanation originating from the vrock. Failure: The target has the Poisoned condition and repeats the save at the end of each of its turns, ending the effect on itself on a success. While Poisoned, the target takes 5 (1d10) Poison damage at the start of each of its turns. Emptying a flask of Holy Water on the target ends the effect early.

**Stunning Screech (1/Day).** Constitution Saving Throw: DC 15, each creature in a 20-foot Emanation originating from the vrock (demons succeed automatically). Failure: 10 (3d6) Thunder damage, and the target has the Stunned condition until the end of the vrock’s next turn.

