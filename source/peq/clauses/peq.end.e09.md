---
id: peq.end.e09
type: endorsement
heading: E09 Extended Hire Costs
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.peq.cover.hire_costs_weekly
  rules:
  - when: qs.peq.cover.hire_costs_weekly > 5000
    action: broker_option
  reason: Offered because a hire costs benefit of {qs.peq.cover.hire_costs_weekly} a week was asked for.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

[[ref:peq.ext.hire-costs]] applies to every item of specified plant named in the schedule for this endorsement, with the weekly limit and the most weeks shown in the schedule for this endorsement, instead of the defaults in that extension.

Schedule variables: items covered; weekly limit (default $10,000 a week for each item); most weeks (default 52 weeks).
