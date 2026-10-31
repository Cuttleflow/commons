---
id: mot.end.e03
type: endorsement
heading: E03 Hire, Fare or Reward
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.use.hire_or_reward
  rules:
  - when: qs.mot.use.hire_or_reward == true
    action: refer
  reason: Referred because you told us a vehicle is used for hire, fare or reward.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

[[ref:mot.excl.hire-fare-or-reward]] does not apply to the Insured vehicles shown in the Schedule for this Endorsement while they are used for the hire, fare or reward purposes shown, including rideshare or delivery for the platforms named. The vehicle must be registered for that use where the law requires it, and the driver must hold any authority the law requires for it.

Schedule variables: vehicles covered; purposes and platforms; additional excess.
