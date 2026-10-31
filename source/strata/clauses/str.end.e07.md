---
id: str.end.e07
type: endorsement
heading: E07 Heritage-Listed Building
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.str.building.heritage
  rules:
  - when: qs.str.building.heritage == yes
    action: refer
  reason: Referred because the building is heritage-listed.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

Where the heritage listing requires damaged parts of the building to be repaired with original or matching materials or methods, the cost of repairing or rebuilding includes that extra cost, within the building sum insured. The building sum insured must allow for it.

Schedule variables: heritage register and listing number.
