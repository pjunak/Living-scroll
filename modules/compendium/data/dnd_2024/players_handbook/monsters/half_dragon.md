---name: Half-Dragon
size: Medium
type: Medium Monstrosity
alignment: Chaotic Evil
ac: '11'
hp: 38 (7d8 + 7)
speed: 20 ft., Fly 40 ft.
stats:
  str: 12
  dex: 13
  con: 12
  int: 7
  wis: 10
  cha: 13
cr: 1 (XP 200; PB +2)
traits: []
actions:
- name: Claw
  damage:
  - type: slashing
    base:
      dice: 2
      die: 4
      bonus: 1
  type: utility
- name: Luring Song
  type: save
  ability: wis
  dc: 11
  on_pass: none
  on_fail: full

---
# Half-Dragon

*Medium Monstrosity, Chaotic Evil*

### Actions

**Claw.** Melee Attack Roll: +3, reach 5 ft. Hit: 6 (2d4 + 1) Slashing damage.

**Luring Song.** The harpy sings a magical melody, which lasts until the harpy’s Concentration ends on it. Wisdom Saving Throw: DC 11, each Humanoid and Giant in a 300-foot Emanation originating from the harpy when the song starts. Failure: The target has the Charmed condition until the song ends and repeats the save at the end of each of its turns. While Charmed, the target has the Incapacitated condition and ignores the Luring Song of other harpies. If the target is more than 5 feet from the harpy, the target moves on its turn toward the harpy by the most direct route, trying to get within 5 feet of the harpy. It doesn’t avoid Opportunity Attacks; however, before moving into damaging terrain (such as lava or a pit) and whenever it takes damage from a source other than the harpy, the target repeats the save. Success: The target is immune to this harpy’s Luring Song for 24 hours.

