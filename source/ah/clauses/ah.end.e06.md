---
id: ah.end.e06
type: endorsement
heading: E06 Extended Run-off Cover
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.ah.cover.extended_runoff_required
  rules:
  - when: qs.ah.cover.extended_runoff_required == yes
    action: broker_option
  reason: Offered because your registration standard or association requires run-off longer than 72 months.
---

The 72-month automatic run-off period in [[ref:ah.ext.run-off]] is extended to the longer period stated in the schedule (including an unlimited run-off period where stated), to meet the run-off requirements of the insured's National Board registration standard or professional association. The other terms of that extension continue to apply.

Schedule variables: run-off period.
