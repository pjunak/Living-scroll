---name: Arms of Hadar
type: spell
level: 1
school: Conjuration
ritual: false
casting_time: Action
range: Self
components:
- V
- S
material: ''
duration: Instantaneous
concentration: false
classes:
- Warlock
id: spell:arms-of-hadar
material_price: ''
actions:
- type: save
  ability: str
  on_pass: half
  on_fail: full
  damage:
  - type: necrotic
    base:
      dice: 2
      die: 6
      bonus: 0
    scaling:
      dice_per_slot: 1
      die: 6
      mode: spell_level
---
# Arms of Hadar
*1st-Level Conjuration (Warlock)*
**Casting Time:** Action
**Range:** Self
**Components:** V, S
**Duration:** Instantaneous

Invoking Hadar, you cause tendrils to erupt from yourself. Each creature in a 10-foot Emanation originating from you makes a Strength saving throw. On a failed save, a target takes 2d6 Necrotic damage and can’t take Reactions until the start of its next turn. On a successful save, a target takes half as much damage only.

**Using a Higher-Level Spell Slot.** The damage increases by 1d6 for each spell slot level above 1.