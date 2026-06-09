---name: Adult Green Dragon
size: Huge
type: Huge Dragon (Chromatic)
alignment: Lawful Evil
ac: '19'
hp: 207 (18d12 + 90)
speed: 40 ft., Fly 80 ft., Swim 40 ft.
stats:
  str: 23
  dex: 12
  con: 21
  int: 18
  wis: 15
  cha: 18
cr: 15 (XP 13,000, or 15,000 in lair; PB +5)
traits:
- name: Immunities
  description: Poison; Poisoned
- name: Amphibious
  description: The dragon can breathe air and water.
- name: Legendary Resistance (3/Day, or 4/Day in Lair)
  description: If the dragon fails a saving throw, it can choose to succeed instead.
actions:
- name: Multiattack
  description: The dragon makes three Rend attacks. It can replace one attack with
    a use of Spellcasting to cast Mind Spike (level 3 version).
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 2
      die: 8
      bonus: 6
  - type: poison
    base:
      dice: 2
      die: 6
      bonus: 0
  type: utility
- name: "Poison Breath (Recharge 5\u20136)"
  type: save
  ability: con
  dc: 18
  on_pass: half
  on_fail: full
  damage:
  - type: poison
    base:
      dice: 16
      die: 6
      bonus: 0
- name: Spellcasting
  description: 'The dragon casts one of the following spells, requiring no Material
    components and using Charisma as the spellcasting ability (spell save DC 17):'
- name: 'At Will:'
  description: Detect Magic, Mind Spike (level 3 version)
- name: '1/Day:'
  description: Geas
- name: Mind Invasion
  description: The dragon uses Spellcasting to cast Mind Spike (level 3 version).
- name: Noxious Miasma
  type: save
  ability: con
  dc: 17
  on_pass: none
  on_fail: full
  damage:
  - type: poison
    base:
      dice: 2
      die: 6
      bonus: 0
- name: Pounce
  description: The dragon moves up to half its Speed, and it makes one Rend attack.

---
# Adult Green Dragon

*Huge Dragon (Chromatic), Lawful Evil*

### Actions

**Rend.** Melee Attack Roll: +11, reach 10 ft. Hit: 15 (2d8 + 6) Slashing damage plus 7 (2d6) Poison damage.

**Poison Breath (Recharge 5–6).** Constitution Saving Throw: DC 18, each creature in a 60-foot Cone. Failure: 56 (16d6) Poison damage. Success: Half damage.

**Noxious Miasma.** Constitution Saving Throw: DC 17, each creature in a 20-foot-radius Sphere centered on a point the dragon can see within 90 feet. Failure: 7 (2d6) Poison damage, and the target takes a −2 penalty to AC until the end of its next turn. Failure or Success: The dragon can’t take this action again until the start of its next turn.

