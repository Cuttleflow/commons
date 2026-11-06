---
id: hnw.end.e02
type: endorsement
heading: E02 High Hazard Zone
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.hnw.property.hazard_zone
  rules:
  - when: qs.hnw.property.hazard_zone == high
    action: refer
  reason: Referred because the address is in a high natural hazard zone for flood or storm; the underwriter sets the special excess.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The home is in a high natural hazard zone for flood or storm. For damage caused by flood or storm, the special excess shown in the schedule for this endorsement applies in place of the basic excess. Flood and storm remain covered.

Schedule variables: flood and storm excess (no default).
