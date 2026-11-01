---
id: me.end.e05
type: endorsement
heading: E05 Additional Extended Reporting Period
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.me.cover.additional_erp
  rules:
  - when: qs.me.cover.additional_erp == yes
    action: broker_option
  reason: Offered because you asked for a longer extended reporting period.
---

The reporting period under [[ref:me.ext.extended-reporting-period]] is extended beyond 365 days for the further period and premium stated in the schedule.

Schedule variables: further period; premium.
