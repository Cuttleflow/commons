---
id: ppl.end.e11
type: endorsement
heading: E11 Excess Layer
since: 2.0.0
status: draft
note: Contains a WP REVIEW tag for the Wording Partner.
trigger:
  questions:
  - qs.ppl.cover.layer
  rules:
  - when: qs.ppl.cover.layer == excess
    action: refer
  reason: Referred because you asked for cover in excess of other insurance.
  responses:
  - Attach
  - Decline risk
---

This policy applies only in excess of the underlying insurance shown in the schedule for this endorsement. We will pay only after the underlying insurer, you or both have paid the full underlying limit. This policy follows the terms of the underlying insurance, except for the limit of liability, the premium, the policy period, and any term of this policy that is narrower. If the underlying aggregate limit is reduced or exhausted by payment of claims covered by this policy, this policy continues in excess of the reduced limit or, if exhausted, as underlying insurance, subject to the excess shown for this endorsement. We do not pay any amount the underlying insurer does not pay because of its insolvency or because the underlying insurance is void or cancelled. [WP REVIEW: check this drop-down and insolvency provision against ICA s45, which preserves true excess-layer other-insurance provisions.]

Schedule variables: underlying insurer, policy number and limits; excess (if the underlying is exhausted).
