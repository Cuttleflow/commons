---
id: tl.end.e11
type: endorsement
heading: E11 Non-IT Dependent Business Interruption
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.tl.cover.options_requested
  rules:
  - when: '''E11'' in qs.tl.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for cover for outages at suppliers you depend on.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

[[ref:tl.cover.business-interruption]] extends to business interruption loss resulting from a **cyber security breach** affecting the computer systems of a supplier named in the schedule for this endorsement, even though that supplier is not a **technology provider**. For this endorsement, a **cyber security breach** at a named supplier is treated as a dependent security breach.

The waiting period shown for this endorsement applies on a threshold basis: once the interruption exceeds it, business interruption loss is measured from the start of the interruption.

This endorsement does not cover interruption arising from physical damage to the supplier's premises or plant, insolvency of the supplier, industrial action, or the supplier's commercial decision to stop supplying.

Schedule variables: named suppliers; sub-limit; waiting period.
