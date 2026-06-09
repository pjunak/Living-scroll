---name: Thunderous Smite
type: spell
level: 1
school: Evocation
ritual: false
casting_time: Bonus Action, which you take immediately after hitting a target with
  a Melee weapon or an Unarmed Strike
range: Self
components:
- V
material: ''
duration: Instantaneous
concentration: false
classes:
- Paladin
id: spell:thunderous-smite
material_price: ''
actions:
- type: save
  ability: str
  on_pass: none
  on_fail: full
  damage:
  - type: thunder
    base:
      dice: 2
      die: 6
      bonus: 0
    scaling:
      dice_per_slot: 1
      die: 6
      mode: spell_level
---
# Thunderous Smite
*1st-Level Evocation (Paladin)*
**Casting Time:** Bonus Action, which you take immediately after hitting a target with a Melee weapon or an Unarmed Strike
**Range:** Self
**Components:** V
**Duration:** Instantaneous

Your strike rings with thunder that is audible within 300 feet of you, and the target takes an extra 2d6 Thunder damage from the attack. Additionally, if the target is a creature, it must succeed on a Strength saving throw or be pushed 10 feet away from you and have the Prone condition.

**Using a Higher-Level Spell Slot.** The damage increases by 1d6 for each spell slot level above 1.