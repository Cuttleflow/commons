---
id: isr.end.natd
type: endorsement
heading: NATD Natural Perils Deductibles
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.peril.cat_zone_high
  rules:
  - when: qs.isr.peril.cat_zone_high == yes
    action: apply
  reason: Applies because a Situation scores above the agency's threshold for cyclone, bushfire or hail.
---

For Damage at a Situation caused by a peril listed in the Schedule for this endorsement, the natural perils deductible shown for that peril applies instead of the standard Deductible. It may be a fixed amount, a percentage of the Declared Value of the Situation with a minimum and a maximum, or, for Business Interruption loss, a time excess. All Damage caused by the same peril within any 72 consecutive hours is one Event.

- **Named cyclone** means a tropical cyclone named by the Bureau of Meteorology. Damage caused by a named cyclone includes Damage by wind, rain or hail from it. Flood remains subject to FLOD.
- **Bushfire** means a fire in bush or grassland, including fire that spreads from it to buildings or other property.
- If the Schedule says so, a deductible for a peril applies only to Situations north of latitude 26 degrees south.

Schedule variables: perils (named cyclone, bushfire, hail, storm); deductible for each; whether a deductible applies only north of 26 degrees south.
