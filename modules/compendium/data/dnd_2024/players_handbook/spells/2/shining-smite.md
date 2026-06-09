---name: Shining Smite
type: spell
level: 2
school: Transmutation
ritual: false
casting_time: Bonus Action, which you take immediately after hitting a creature with
  a Melee weapon or an Unarmed Strike
range: Self
components:
- V
material: ''
duration: Concentration, up to 1 minute
concentration: true
classes:
- Paladin
id: spell:shining-smite
material_price: ''
actions:
- type: utility
  damage:
  - type: radiant
    base:
      dice: 2
      die: 6
      bonus: 0
    scaling:
      dice_per_slot: 1
      die: 6
      mode: spell_level
---
# Shining Smite
*2nd-Level Transmutation (Paladin)*
**Casting Time:** Bonus Action, which you take immediately after hitting a creature with a Melee weapon or an Unarmed Strike
**Range:** Self
**Components:** V
**Duration:** Concentration, up to 1 minute

The target hit by the strike takes an extra 2d6 Radiant damage from the attack. Until the spell ends, the target sheds Bright Light in a 5-foot radius, attack rolls against it have Advantage, and it can’t benefit from the Invisible condition.

**Using a Higher-Level Spell Slot.** The damage increases by 1d6 for each spell slot level above 2.