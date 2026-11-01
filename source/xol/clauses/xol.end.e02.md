---
id: xol.end.e02
type: endorsement
heading: E02 Reinstatement of the Limit of Liability
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.xol.endorsements.reinstatement_requested
  rules:
  - when: qs.xol.endorsements.reinstatement_requested == true
    action: refer
  reason: Referred because you asked for the limit of liability to be reinstated.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

Once the limit of liability has been paid in full, it is reinstated once, for the rest of the policy period, for loss arising from claims first made, or losses first occurring, after the date of the reinstatement. The reinstated limit is not available for any claim or loss that the followed policy treats as related to a claim or loss that exhausted the original limit.

You must pay the reinstatement premium shown in the schedule, calculated as the schedule states. [[ref:xol.pay.limit-of-liability]] is read as allowing two limits of liability in total for the policy period.

Schedule variables: the reinstatement premium, as an amount or as a percentage of the annual premium, and whether it is pro rata as to time.
