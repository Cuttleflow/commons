---
id: lld.end.e02
type: endorsement
heading: E02 Higher Weekly Rent
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.lld.tenancy.weekly_rent
  rules:
  - when: qs.lld.tenancy.weekly_rent > 1500
    action: refer
  reason: Referred because the weekly rent is ${qs.lld.tenancy.weekly_rent}, above the standard limit.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

The weekly rent limit is the amount shown in the schedule for this endorsement, in place of the limit in [[ref:lld.def.rent]].

Schedule variables: weekly rent limit (no default).
