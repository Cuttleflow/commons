---
id: cpo.end.e03
type: endorsement
heading: E03 Building Works
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.cpo.condition.building_works
  rules:
  - when: qs.cpo.condition.building_works == yes
    action: refer
  reason: Building works are planned or under way.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
---

[[ref:cpo.excl.building-works]] does not apply to the building works described in the schedule for this endorsement. Damage to the rest of the building during those works is covered. Damage to the works themselves is covered only up to the works limit shown, and only if the works contractor's own contract works insurance does not respond. You must make sure the contractor holds contract works and public liability insurance for the works.

Schedule variables: description and contract value of the works; works period; works limit (default: nil).
