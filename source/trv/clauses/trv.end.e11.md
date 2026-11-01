---
id: trv.end.e11
type: endorsement
heading: E11 Cancel for Any Reason
since: 1.0.0
changed: 1.1.0
status: draft
trigger:
  questions:
  - qs.trv.cover.cfar
  rules:
  - when: qs.trv.cover.cfar == yes
    action: refer
  reason: Offered because cancel for any reason cover was requested.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

If you cancel the trip more than 14 days before departure for any reason, including a reason not listed in [[ref:trv.cover.cancellation]], we will pay 75% of the non-refundable amounts you lose, up to 75% of the cancellation limit for your plan. The exclusion in that section for you changing your mind, or for your work or business commitments, does not apply to this payment. All the other terms of that section apply.

Schedule variables: none.
