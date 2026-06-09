---name: Adult Copper Dragon
size: Huge
type: Huge Dragon (Metallic)
alignment: Chaotic Good
ac: '18'
hp: 184 (16d12 + 80)
speed: 40 ft., Climb 40 ft., Fly 80 ft.
stats:
  str: 23
  dex: 12
  con: 21
  int: 18
  wis: 15
  cha: 18
cr: 14 (XP 11,500, or 13,000 in lair; PB +5)
traits:
- name: Immunities
  description: Acid
- name: Legendary Resistance (3/Day, or 4/Day in Lair)
  description: If the dragon fails a saving throw, it can choose to succeed instead.
actions:
- name: Multiattack
  description: The dragon makes three Rend attacks. It can replace one attack with
    a use of (A) Slowing Breath or (B) Spellcasting to cast Mind Spike (level 4 version).
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 2
      die: 10
      bonus: 6
  - type: acid
    base:
      dice: 1
      die: 8
      bonus: 0
  type: utility
- name: "Acid Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 18
  on_pass: half
  on_fail: full
  damage:
  - type: acid
    base:
      dice: 12
      die: 8
      bonus: 0
- name: Slowing Breath
  type: save
  ability: con
  dc: 18
  on_pass: none
  on_fail: full
- name: Spellcasting
  description: 'The dragon casts one of the following spells, requiring no Material
    components and using Charisma as the spellcasting ability (spell save DC 17):'
- name: 'At Will:'
  description: Detect Magic, Mind Spike (level 4 version), Minor Illusion, Shapechange
    (Beast or Humanoid form only, no Temporary Hit Points gained from the spell, and
    no Concentration or Temporary Hit Points required to maintain the spell)
- name: '1/Day Each:'
  description: Greater Restoration, Major Image
- name: Giggling Magic
  type: save
  ability: cha
  dc: 17
  on_pass: none
  on_fail: full
  damage:
  - type: psychic
    base:
      dice: 7
      die: 6
      bonus: 0
- name: Mind Jolt
  description: "The dragon uses Spellcasting to cast Mind Spike (level 4 version).\
    \ The dragon can\u2019t take this action again until the start of its next turn."
- name: Pounce
  description: The dragon moves up to half its Speed, and it makes one Rend attack.

---
# Adult Copper Dragon

*Huge Dragon (Metallic), Chaotic Good*

### Actions

**Rend.** Melee Attack Roll: +11, reach 10 ft. Hit: 17 (2d10 + 6) Slashing damage plus 4 (1d8) Acid damage.

**Acid Breath (Recharge 5–6).** Dexterity Saving Throw: DC 18, each creature in an 60-foot-long, 5-foot-wide Line. Failure: 54 (12d8) Acid damage. Success: Half damage.

**Slowing Breath.** Constitution Saving Throw: DC 18, each creature in a 60-foot Cone. Failure: The target can’t take Reactions; its Speed is halved; and it can take either an action or a Bonus Action on its turn, not both. This effect lasts until the end of its next turn.

**Giggling Magic.** Charisma Saving Throw: DC 17, one creature the dragon can see within 90 feet. Failure: 24 (7d6) Psychic damage. Until the end of its next turn, the target rolls 1d6 whenever it makes an ability check or attack roll and subtracts the number rolled from the D20 Test. Failure or Success: The dragon can’t take this action again until the start of its next turn.

