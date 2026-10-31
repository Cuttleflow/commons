---
id: hom.end.e10
type: endorsement
heading: E10 Building Works
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.hom.property.renovation
  rules:
  - when: qs.hom.property.renovation == yes
    action: refer
  reason: Referred because building works are under way or planned.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

Building works described in the schedule for this endorsement may be carried out at the home. [[ref:hom.excl.unoccupied]] does not apply while the works are under way and a builder licensed for them is responsible for the site. We do not pay for damage to the works themselves, to materials not yet fixed to the building, or for damage that results from the works.

Schedule variables: description and contract value of the works; expected completion date.
