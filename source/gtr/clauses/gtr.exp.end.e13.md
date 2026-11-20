---
id: gtr.exp.end.e13
type: endorsement
heading: E13 USA Travel
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gtr.exp.usa_travel
  rules:
  - when: qs.gtr.exp.usa_travel == yes
    action: apply
  reason: Applied because assignees travel to the USA from a host country outside the worldwide area.
  responses:
  - Attach
  - Attach with premium loading
---

If the area of cover is not worldwide, treatment in the USA during a trip from the host country of up to the number of days shown in the schedule (default 30 days in each policy period) is covered, for an injury or sickness that first shows itself in the USA. Treatment an insured person travelled to the USA to obtain is not covered.

Schedule variables: days in the USA in each policy period.
