---
id: prc.end.e06
type: endorsement
heading: E06 Untraceable Products
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.prc.controls.batch_coding
  rules:
  - when: qs.prc.controls.batch_coding == false
    action: refer
  reason: Referred because the insured products are not coded so that a batch can be identified and traced.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

Where the insured products affected by an insured event cannot be identified by production batch, we pay recall costs and replacement costs only for insured products made or supplied in the period before the insured event was discovered that is shown in the schedule for this endorsement. If no period is shown, it is 90 days.

Schedule variables: the period (default 90 days).
