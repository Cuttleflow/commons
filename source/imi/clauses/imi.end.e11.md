---
id: imi.end.e11
type: endorsement
heading: E11 Excess Layer
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.imi.cover.options_requested
  rules:
  - when: '''E11 Excess Layer'' in qs.imi.cover.options_requested'
    action: refer
  reason: Considered because you asked for cover excess of other insurance.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

We pay covered loss under this policy only after the underlying limit shown in the schedule for this endorsement has been exhausted by the payment of covered loss. The underlying limit is exhausted only by payment of loss by the underlying insurers or by you. This policy does not drop down if an underlying insurer is unable or refuses to pay, and you bear that part of the loss.

Our limit of liability under this endorsement is the amount shown in the schedule, excess of the underlying limit. Subject to this endorsement, this policy applies to the layer on its own terms. [[ref:imi.pay.other-insurance]] does not apply to the underlying insurance. [WP REVIEW: whether the layer should follow the terms of the underlying policy, as is usual for an excess layer, rather than apply this policy's own terms]

Schedule variables: underlying insurer and policy; underlying limit; limit of liability of the layer.
