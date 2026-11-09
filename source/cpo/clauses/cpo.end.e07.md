---
id: cpo.end.e07
type: endorsement
heading: E07 Heritage-Listed Building
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.cpo.building.heritage
  rules:
  - when: qs.cpo.building.heritage == yes
    action: apply
  reason: The building is heritage-listed.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

The building is heritage-listed. Where the heritage listing or a heritage authority requires damaged heritage features to be repaired or rebuilt with original or matching materials or methods, we pay the extra cost of doing so, up to the heritage limit shown in the schedule for this endorsement, in addition to the building sum insured.

Schedule variables: heritage limit (default: 10% of the building sum insured).
