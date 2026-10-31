---
id: mot.end.e11
type: endorsement
heading: E11 Registered Mobile Plant
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.vehicles.plant_count
  rules:
  - when: qs.mot.vehicles.plant_count > 0
    action: refer
  reason: Referred because {qs.mot.vehicles.plant_count} item(s) of registered mobile plant are listed.
  responses:
  - Attach
  - Attach with special excess
  - Do not attach
  - Decline risk
---

Registered mobile plant shown in the Schedule is an Insured vehicle while it is driven on a public road, at the cover level shown. Loss, damage and liability while it is operated as a Tool of trade are not covered by this Policy and should be insured under a plant and equipment or liability policy.

Schedule variables: plant covered; cover level; Sum insured.
