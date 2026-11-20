---
id: mpc.end.e03
type: endorsement
heading: E03 Water-Skier and Tow-Sport Liability
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.mpc.cover.water_ski
  rules:
  - when: qs.mpc.cover.water_ski == yes
    action: apply
  reason: Applies because water-skier and tow-sport liability was chosen.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

[[ref:mpc.section.liability]] covers liability for personal injury to a person being towed by the boat on water skis, a wakeboard, a kneeboard, an inflatable or any similar thing, and the liability of that person for personal injury or property damage to others, while an observer is on board as the law of the place requires. Towing a person or object in the air remains excluded under [[ref:mpc.excl.liability-towing]].

Schedule variables: none.
