---
id: hom.end.e02
type: endorsement
heading: E02 Flood Excess
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.hom.property.hazard_zone
  rules:
  - when: qs.hom.property.hazard_zone == high
    action: refer
  reason: Referred because the address is in a high natural hazard zone; the underwriter sets any flood excess.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

For damage caused by flood, the flood excess shown in the schedule for this endorsement applies in place of the basic excess. Flood remains covered.

Schedule variables: flood excess (no default).
