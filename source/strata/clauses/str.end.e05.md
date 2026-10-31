---
id: str.end.e05
type: endorsement
heading: E05 Water Damage Excess
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.str.claims.water_damage_count
  rules:
  - when: qs.str.claims.water_damage_count >= 2
    action: refer
  reason: Referred because the scheme has had {qs.str.claims.water_damage_count} water damage claims in the last three years.
  responses:
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

For damage caused by liquid escaping from a pipe, tank, appliance, shower, bath or other fixture, the excess shown in the schedule for this endorsement applies in place of the basic excess.

Schedule variables: water damage excess.
