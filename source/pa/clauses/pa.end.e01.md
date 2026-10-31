---
id: pa.end.e01
type: endorsement
heading: E01 Agreed Value Weekly Benefit
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.cover.agreed_value
  rules:
  - when: qs.pa.cover.agreed_value == yes
    action: refer
  reason: Offered because an agreed weekly benefit was requested; it needs evidence of income before cover starts.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

The second limit in [[ref:pa.pay.weekly-benefit-amount]], the percentage of your income, does not apply. We pay the weekly benefit as an agreed amount, subject to [[ref:pa.pay.offsets]].

You confirm that the weekly benefit was no more than the percentage of income shown in the schedule for this endorsement when this policy started or was last renewed, and you must give us evidence of your income for the 12 months before then if we ask.

Schedule variables: agreed weekly benefit; percentage of income at inception (default 85%).
