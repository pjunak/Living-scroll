---name: Destructive Wave
type: spell
level: 5
school: Evocation
ritual: false
casting_time: Action
range: Self
components:
- V
material: ''
duration: Instantaneous
concentration: false
classes:
- Paladin
id: spell:destructive-wave
material_price: ''
actions:
- type: save
  ability: con
  on_pass: half
  on_fail: full
  damage:
  - type: thunder
    base:
      dice: 5
      die: 6
      bonus: 0
---
# Destructive Wave
*5th-Level Evocation (Paladin)*
**Casting Time:** Action
**Range:** Self
**Components:** V
**Duration:** Instantaneous

Destructive energy ripples outward from you in a 30-foot Emanation. Each creature you choose in the Emanation makes a Constitution saving throw. On a failed save, a target takes 5d6 Thunder damage and 5d6 Radiant or Necrotic damage (your choice) and has the Prone condition. On a successful save, a target takes half as much damage only.