---
id: lld.end.e05
type: endorsement
heading: E05 Rooming House or Student Accommodation
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.lld.tenancy.tenancy_type
  rules:
  - when: qs.lld.tenancy.tenancy_type == rooming
    action: refer
  - when: qs.lld.tenancy.tenancy_type == student
    action: refer
  reason: Referred because the property is let as a rooming house or student accommodation.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The property may be let by the room, under a separate agreement for each room, as a rooming house or as student accommodation. Each occupant is treated as a tenant. The tenant damage excess applies once for each room in which damage happens, and the rent cover limit applies to all rooms together.

Schedule variables: number of rooms let; special excess (default the tenant damage excess).
