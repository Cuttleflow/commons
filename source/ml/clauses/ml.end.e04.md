---
id: ml.end.e04
type: endorsement
heading: E04 Increased WHS Defence Costs Sub-limit
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.ml.cover.options_requested
  - qs.ml.ops.high_risk_workplace
  rules:
  - when: '''E04'' in qs.ml.cover.options_requested'
    action: broker_option
  - when: qs.ml.ops.high_risk_workplace == yes
    action: suggest
  reason: Suggested because your workers carry out work with a higher risk of a WHS prosecution.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

The WHS defence costs sub-limit in [[ref:ml.cover.whs-defence-costs]] is replaced by the increased sub-limit shown in the schedule for this endorsement. The increased sub-limit is part of the Statutory Liability section limit of liability, unless the schedule states that it is in addition to it.

This endorsement increases the amount we pay for defence costs only. It does not cover any fine or penalty that [[ref:ml.excl.uninsurable-penalties]] excludes.

Schedule variables: increased sub-limit; whether in addition to the section limit.
