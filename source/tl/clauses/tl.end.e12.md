---
id: tl.end.e12
type: endorsement
heading: E12 Customer Business Interruption
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.tl.cover.options_requested
  rules:
  - when: '''E12'' in qs.tl.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for cover for lost income when a major customer suffers a cyber event.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

[[ref:tl.cover.business-interruption]] extends to your lost income resulting from a reduction in purchases by a customer named in the schedule for this endorsement, where that reduction results directly from a **cyber security breach** affecting the named customer's computer systems.

Loss is measured over the indemnity period, after the waiting period shown for this endorsement on a threshold basis, and only to the extent the reduction in the named customer's purchases exceeds normal variation in their purchasing pattern over the preceding 12 months.

This endorsement does not cover reductions attributable to market conditions, the customer's financial position, or any cause other than the **cyber security breach**.

Schedule variables: named customers; sub-limit; waiting period.
