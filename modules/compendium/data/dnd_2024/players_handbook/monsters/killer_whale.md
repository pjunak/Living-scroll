---name: Killer Whale
size: Large
type: Large Beast
alignment: Unaligned
ac: '12'
hp: 22 (4d10)
speed: 50 ft.
stats:
  str: 17
  dex: 15
  con: 11
  int: 3
  wis: 12
  cha: 8
cr: 1 (XP 200; PB +2)
traits:
- name: Pack Tactics
  description: "The lion has Advantage on an attack roll against a creature if at\
    \ least one of the lion\u2019s allies is within 5 feet of the creature and the\
    \ ally doesn\u2019t have the Incapacitated condition."
- name: Running Leap
  description: With a 10-foot running start, the lion can Long Jump up to 25 feet.
actions:
- name: Multiattack
  description: The lion makes two Rend attacks. It can replace one attack with a use
    of Roar.
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 1
      die: 8
      bonus: 3
  type: utility
- name: Roar
  type: save
  ability: wis
  dc: 11
  on_pass: none
  on_fail: full

---
# Killer Whale

*Large Beast, Unaligned*

### Actions

**Rend.** Melee Attack Roll: +5, reach 5 ft. Hit: 7 (1d8 + 3) Slashing damage.

**Roar.** Wisdom Saving Throw: DC 11, one creature within 15 feet. Failure: The target has the Frightened condition until the start of the lion’s next turn.

