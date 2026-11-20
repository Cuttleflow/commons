---
id: mpc.end.e07
type: endorsement
heading: E07 Standing Rigging
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.mpc.boat.rigging_age
  rules:
  - when: "qs.mpc.boat.rigging_age > 10"
    action: refer
  reason: "Referred because the standing rigging is {qs.mpc.boat.rigging_age} years old."
  responses:
  - Attach
  - Attach with special excess
  - Do not attach
---

The exclusion in [[ref:mpc.excl.moorings-and-rigging]] of damage caused by the failure of standing rigging more than 10 years old does not apply, provided a qualified rigger inspected the standing rigging within the period shown in the schedule for this endorsement before the damage, and any work the rigger recommended was done.

Schedule variables: rigging inspection period (default 12 months).
