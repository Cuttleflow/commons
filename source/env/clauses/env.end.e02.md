---
id: env.end.e02
type: endorsement
heading: E02 Transported Cargo
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.env.ops.transports_dangerous_goods
  - qs.env.ops.bulk_fuel_or_chemicals
  rules:
  - when: qs.env.ops.bulk_fuel_or_chemicals == true
    action: refer
  - when: qs.env.ops.transports_dangerous_goods == true
    action: suggest
  reason: Applies because you transport dangerous goods or pollutants by road for your work.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

[[ref:env.excl.transport]] does not apply to a pollution condition arising from cargo transported by you or on your behalf by road in connection with covered operations, including loading and unloading, beyond the boundary of a job site, within Australia. The most we will pay under this endorsement is the sub-limit shown in the schedule for it, which is part of and not in addition to the limit of liability.

Schedule variables: the sub-limit; whether bulk fuel or chemicals are covered.
