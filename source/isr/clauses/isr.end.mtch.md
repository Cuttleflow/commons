---
id: isr.end.mtch
type: endorsement
heading: MTCH Matching and Undamaged Portions
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  rules:
  - when: '''MTCH'' in qs.isr.cover.options_requested'
    action: broker_option
  reason: Offered as an option for matching and undamaged parts.
---

When we pay to reinstate Damaged property, we also pay:

- the cost of replacing or altering undamaged parts that form one continuous area or set with the Damaged parts, where replacement materials cannot reasonably match them in appearance or function; and
- the value of undamaged parts of a Damaged building (including foundations) that cannot lawfully or practically be used in reinstating it, and the cost of removing them.

The most we pay under this endorsement at any one Situation is the sub-limit shown in the Schedule.

Schedule variables: sub-limit per Situation.
