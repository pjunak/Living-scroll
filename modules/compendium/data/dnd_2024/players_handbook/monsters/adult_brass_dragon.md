---name: Adult Brass Dragon
size: Huge
type: Huge Dragon (Metallic)
alignment: Chaotic Good
ac: '18'
hp: 172 (15d12 + 75)
speed: 40 ft., Burrow 30 ft., Fly 80 ft.
stats:
  str: 23
  dex: 10
  con: 21
  int: 14
  wis: 13
  cha: 17
cr: 13 (XP 10,000, or 11,500 in lair; PB +5)
traits:
- name: Immunities
  description: Fire
- name: Legendary Resistance (3/Day, or 4/Day in Lair)
  description: If the dragon fails a saving throw, it can choose to succeed instead.
actions:
- name: Multiattack
  description: The dragon makes three Rend attacks. It can replace one attack with
    a use of (A) Sleep Breath or (B) Spellcasting to cast Scorching Ray.
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 2
      die: 10
      bonus: 6
  - type: fire
    base:
      dice: 1
      die: 8
      bonus: 0
  type: utility
- name: "Fire Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 18
  on_pass: half
  on_fail: full
  damage:
  - type: fire
    base:
      dice: 10
      die: 8
      bonus: 0
- name: Sleep Breath
  type: save
  ability: con
  dc: 18
  on_pass: none
  on_fail: full
- name: Spellcasting
  description: 'The dragon casts one of the following spells, requiring no Material
    components and using Charisma as the spellcasting ability (spell save DC 16):'
- name: 'At Will:'
  description: Detect Magic, Minor Illusion, Scorching Ray, Shapechange (Beast or
    Humanoid form only, no Temporary Hit Points gained from the spell, and no Concentration
    or Temporary Hit Points required to maintain the spell), Speak with Animals
- name: '1/Day Each:'
  description: Detect Thoughts, Control Weather
- name: Blazing Light
  description: The dragon uses Spellcasting to cast Scorching Ray.
- name: Pounce
  description: The dragon moves up to half its Speed, and it makes one Rend attack.
- name: Scorching Sands
  type: save
  ability: dex
  dc: 16
  on_pass: none
  on_fail: full
  damage:
  - type: fire
    base:
      dice: 6
      die: 8
      bonus: 0

---
# Adult Brass Dragon

*Huge Dragon (Metallic), Chaotic Good*

### Actions

**Rend.** Melee Attack Roll: +11, reach 10 ft. Hit: 17 (2d10 + 6) Slashing damage plus 4 (1d8) Fire damage.

**Fire Breath (Recharge 5–6).** Dexterity Saving Throw: DC 18, each creature in a 60-foot-long, 5-foot-wide Line. Failure: 45 (10d8) Fire damage. Success: Half damage.

**Sleep Breath.** Constitution Saving Throw: DC 18, each creature in a 60-foot Cone. Failure: The target has the Incapacitated condition until the end of its next turn, at which point it repeats the save. Second Failure: The target has the Unconscious condition for 10 minutes. This effect ends for the target if it takes damage or a creature within 5 feet of it takes an action to wake it.

**Scorching Sands.** Dexterity Saving Throw: DC 16, one creature the dragon can see within 120 feet. Failure: 27 (6d8) Fire damage, and the target’s Speed is halved until the end of its next turn. Failure or Success: The dragon can’t take this action again until the start of its next turn.

