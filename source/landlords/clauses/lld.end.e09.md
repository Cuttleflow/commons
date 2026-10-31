---
id: lld.end.e09
type: endorsement
heading: E09 Unoccupied Property
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.lld.tenancy.vacant_over_60_days
  rules:
  - when: qs.lld.tenancy.vacant_over_60_days == yes
    action: refer
  reason: Referred because the property has been, or will be, unoccupied for more than 60 days.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

[[ref:lld.excl.unoccupied]] does not apply until the date shown in the schedule for this endorsement, provided you or your property manager inspect the property at least every 14 days and keep it secure.

Schedule variables: date cover for unoccupancy ends (no default).
