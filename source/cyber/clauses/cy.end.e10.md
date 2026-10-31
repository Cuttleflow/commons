---
id: cy.end.e10
type: endorsement
heading: E10 Excess Layer
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.cy.cover.layer
  rules:
  - when: qs.cy.cover.layer == excess
    action: apply
  reason: Applies because this policy is written in excess of other cyber insurance.
  responses:
  - Attach
  - Decline risk
---

This policy applies as excess insurance above the underlying insurance listed in the schedule for this endorsement. Cover attaches only after the underlying limits have been exhausted by actual payment of covered loss.

This policy follows the terms, conditions, definitions and exclusions of the primary policy listed in the schedule, except as otherwise stated in this policy or the schedule, and except that this policy's limit of liability, premium and notice provisions always apply.

You must maintain the underlying insurance in full effect during the policy period and tell us of any change to it. If the underlying insurance is reduced or exhausted by covered loss, this policy drops down only to the extent of that reduction; it does not drop down where the underlying insurance is uncollectible for any other reason, including insurer insolvency. [[ref:cy.pay.excess]] does not apply; the underlying limits are the attachment point.

Schedule variables: underlying insurance; attachment point.
