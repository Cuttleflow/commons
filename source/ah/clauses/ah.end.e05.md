---
id: ah.end.e05
type: endorsement
heading: E05 Extended Reporting Period
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.ah.cover.erp_purchased
  rules:
  - when: qs.ah.cover.erp_purchased == yes
    action: apply
  reason: Applies because you bought the 12-month extended reporting period.
---

Records the purchase of the 12-month extended reporting period described in [[ref:ah.ext.extended-reporting-period]], with the start and end dates stated in the schedule.

Schedule variables: extended reporting period start and end dates.
