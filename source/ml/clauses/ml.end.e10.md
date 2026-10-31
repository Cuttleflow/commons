---
id: ml.end.e10
type: endorsement
heading: E10 Excess Layer
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.ml.cover.layer
  rules:
  - when: qs.ml.cover.layer == excess
    action: apply
  reason: Applies because this policy is written in excess of other management liability insurance.
  responses:
  - Attach
  - Decline risk
---

This policy applies only in excess of the underlying insurance shown in the schedule for this endorsement, and only after the underlying limits have been exhausted by payment of covered loss. Except as this endorsement states, this policy follows the terms of the primary underlying policy for the sections shown in the schedule.

Where the underlying limits are reduced or exhausted by payment, this policy drops down to apply in excess of the reduced limits, or in place of the exhausted limits. This policy does not drop down because an underlying insurer becomes insolvent or fails to pay for any other reason. The excess under [[ref:ml.pay.excess]] does not apply; the underlying limits are the attachment point.

We are not obliged to defend any claim. We may join the defence or settlement of any claim that is likely to involve this policy.

Schedule variables: underlying insurance (insurer, policy, limits, sections).
