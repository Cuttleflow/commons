---
id: env.end.e06
type: endorsement
heading: E06 Prior Acts
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.env.history.prior_cpl_continuous
  rules:
  - when: qs.env.history.prior_cpl_continuous == true
    action: broker_option
  reason: Offered because you have held continuous contractors pollution cover before this policy.
---

The retroactive date for [[ref:env.cover.contractors-pollution-liability]] is the date shown in the schedule for this endorsement, which is the start of your continuous prior contractors pollution cover. [[ref:env.excl.known-conditions]] and [[ref:env.excl.prior-claims-and-circumstances]] still apply.

Schedule variables: the retroactive date; the prior insurer.
