---
id: mot.end.e10
type: endorsement
heading: E10 Extended Hire Vehicle
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.cover.hire_extended
  rules:
  - when: qs.mot.cover.hire_extended == true
    action: broker_option
  reason: Offered as an option to extend the hire vehicle benefit.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

The hire vehicle additional benefits are increased to the daily amount and period shown in the Schedule, and the benefit for hire after an accident applies whoever was at fault.

Schedule variables: daily amount; period.
