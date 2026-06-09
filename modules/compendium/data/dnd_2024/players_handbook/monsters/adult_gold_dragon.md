---name: Adult Gold Dragon
size: Huge
type: Huge Dragon (Metallic)
alignment: Lawful Good
ac: '19'
hp: 243 (18d12 + 126)
speed: 40 ft., Fly 80 ft., Swim 40 ft.
stats:
  str: 27
  dex: 14
  con: 25
  int: 16
  wis: 15
  cha: 24
cr: 17 (XP 18,000, or 20,000 in lair; PB +6)
traits:
- name: Immunities
  description: Fire
- name: Amphibious
  description: The dragon can breathe air and water.
- name: Legendary Resistance (3/Day, or 4/Day in Lair)
  description: If the dragon fails a saving throw, it can choose to succeed instead.
actions:
- name: Multiattack
  description: The dragon makes three Rend attacks. It can replace one attack with
    a use of (A) Spellcasting to cast Guiding Bolt (level 2 version) or (B) Weakening
    Breath.
- name: Rend
  damage:
  - type: slashing
    base:
      dice: 2
      die: 8
      bonus: 8
  - type: fire
    base:
      dice: 1
      die: 8
      bonus: 0
  type: utility
- name: "Fire Breath (Recharge 5\u20136)"
  type: save
  ability: dex
  dc: 21
  on_pass: half
  on_fail: full
  damage:
  - type: fire
    base:
      dice: 12
      die: 10
      bonus: 0
- name: Spellcasting
  description: 'The dragon casts one of the following spells, requiring no Material
    components and using Charisma as the spellcasting ability (spell save DC 21, +13
    to hit with spell attacks):'
- name: 'At Will:'
  description: Detect Magic, Guiding Bolt (level 2 version), Shapechange (Beast or
    Humanoid form only, no Temporary Hit Points gained from the spell, and no Concentration
    or Temporary Hit Points required to maintain the spell)
- name: '1/Day Each:'
  description: Flame Strike, Zone of Truth
- name: Weakening Breath
  type: save
  ability: str
  dc: 21
  on_pass: none
  on_fail: full
- name: Banish
  type: save
  ability: cha
  dc: 21
  on_pass: none
  on_fail: full
  damage:
  - type: force
    base:
      dice: 3
      die: 6
      bonus: 0
- name: Guiding Light
  description: The dragon uses Spellcasting to cast Guiding Bolt (level 2 version).
- name: Pounce
  description: The dragon moves up to half its Speed, and it makes one Rend attack.

---
# Adult Gold Dragon

*Huge Dragon (Metallic), Lawful Good*

### Actions

**Rend.** Melee Attack Roll: +14, reach 10 ft. Hit: 17 (2d8 + 8) Slashing damage plus 4 (1d8) Fire damage.

**Fire Breath (Recharge 5–6).** Dexterity Saving Throw: DC 21, each creature in a 60-foot Cone. Failure: 66 (12d10) Fire damage. Success: Half damage.

**Weakening Breath.** Strength Saving Throw: DC 21, each creature that isn’t currently affected by this breath in a 60-foot Cone. Failure: The target has Disadvantage on Strength-based D20 Tests and subtracts 3 (1d6) from its damage rolls. It repeats the save at the end of each of its turns, ending the effect on itself on a success. After 1 minute, it succeeds automatically.

**Banish.** Charisma Saving Throw: DC 21, one creature the dragon can see within 120 feet. Failure: 10 (3d6) Force damage, and the target has the Incapacitated condition and is transported to a harmless demiplane until the start of the dragon’s next turn, at which point it reappears in an unoccupied space of the dragon’s choice within 120 feet of the dragon. Failure or Success: The dragon can’t take this action again until the start of its next turn.

