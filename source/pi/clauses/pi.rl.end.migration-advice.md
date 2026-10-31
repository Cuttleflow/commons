---
id: pi.rl.end.migration-advice
type: endorsement
heading: Migration Advice
profession: recruitment-labour-hire
since: 1.0.0
status: draft
note: Adds cover.
trigger:
  questions:
  - qs.pi.rl.migration_advice
  - qs.pi.rl.marn
  rules:
  - when: qs.pi.rl.migration_advice = yes
    action: broker_option
  reason: Offered because a registered migration agent advises your clients or candidates.
---

We will not apply [[ref:pi.rl.excl.migration-advice]] to immigration assistance given by a registered migration agent named in the schedule, while that agent is registered.
