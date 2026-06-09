---name: Djinni
size: Medium
type: Medium Monstrosity
alignment: Neutral
ac: '14'
hp: 52 (8d8 + 16)
speed: 30 ft.
stats:
  str: 11
  dex: 18
  con: 14
  int: 11
  wis: 12
  cha: 14
cr: 3 (XP 700; PB +2)
traits:
- name: Immunities
  description: Charmed
actions:
- name: Multiattack
  description: The doppelganger makes two Slam attacks and uses Unsettling Visage
    if available.
- name: Slam
  damage:
  - type: bludgeoning
    base:
      dice: 2
      die: 6
      bonus: 4
  type: utility
- name: Read Thoughts
  description: The doppelganger casts Detect Thoughts, requiring no spell components
    and using Charisma as the spellcasting ability (spell save DC 12).
- name: Unsettling Visage (Recharge 6)
  type: save
  ability: wis
  dc: 12
  on_pass: none
  on_fail: full
- name: Shape-Shift
  description: "The doppelganger shape-shifts into a Medium or Small Humanoid, or\
    \ it returns to its true form. Its game statistics, other than its size, are the\
    \ same in each form. Any equipment it is wearing or carrying isn\u2019t transformed."

---
# Djinni

*Medium Monstrosity, Neutral*

### Actions

**Slam.** Melee Attack Roll: +6 (with Advantage during the first round of each combat), reach 5 ft. Hit: 11 (2d6 + 4) Bludgeoning damage.

**Unsettling Visage (Recharge 6).** Wisdom Saving Throw: DC 12, each creature in a 15-foot Emanation originating from the doppelganger that can see the doppelganger. Failure: The target has the Frightened condition and repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically.

