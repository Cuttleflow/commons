---
id: car.end.e07
type: endorsement
heading: E07 Wet Works
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.car.risk.marine_tidal
  rules:
  - when: qs.car.risk.marine_tidal == yes
    action: refer
  restrictions:
  - when: qs.car.risk.marine_tidal == yes and this endorsement is not attached
    action: refer
    note: Works in water are excluded without this endorsement, so the underwriter must decide.
  reason: Referred because the project includes work in or next to water.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:car.excl.property-excluded]] does not exclude the works in or next to water named in the schedule for this endorsement. The following conditions apply:

- work is planned around tide and weather forecasts, and stopped when a warning for the site is issued;
- materials and plant are secured above the highest astronomical tide when not in use; and
- the separate excess for wet works shown in the schedule applies.

This endorsement does not cover marine risks to vessels or cargo, which need a marine policy.

Schedule variables: wet works described; special excess.
