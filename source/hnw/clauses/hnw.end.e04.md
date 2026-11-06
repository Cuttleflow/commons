---
id: hnw.end.e04
type: endorsement
heading: E04 Northern Australia
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.hnw.property.north_of_26th
  - qs.hnw.property.state
  rules:
  - when: qs.hnw.property.north_of_26th == yes or qs.hnw.property.state == NT
    action: refer
  reason: Referred because the home is north of the 26th parallel or in the Northern Territory, where the cyclone reinsurance pool applies.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The home is north of the 26th parallel of latitude, or in the Northern Territory. For damage caused by a cyclone, or by storm, flood or action of the sea within 48 hours after a cyclone, the cyclone excess shown in the schedule for this endorsement applies in place of the basic excess. Action of the sea following a cyclone is covered.

Schedule variables: cyclone excess (no default).
