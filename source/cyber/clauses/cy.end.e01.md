---
id: cy.end.e01
type: endorsement
heading: E01 Extended Reporting Period
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.cy.cover.options_requested
  rules:
  - when: '''E01'' in qs.cy.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for a longer period to notify claims after the policy ends.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

If this policy is cancelled or not renewed, and you do not obtain replacement cover, you may buy an extended reporting period of the duration shown in the schedule for this endorsement by giving us written notice and paying the additional premium within 30 days after the end of the policy period.

During the extended reporting period we will cover claims first made against you, and insured losses first discovered by you, arising solely from cyber events, dependent events, privacy breaches, or acts, errors or omissions that occurred before the end of the policy period.

The extended reporting period does not reinstate or increase the limit of liability, which applies in the aggregate across the policy period and the extended reporting period combined.

You may not buy the extended reporting period if the policy was cancelled for non-payment of premium or for fraud. The automatic 30-day period under [[ref:cy.cond.cancellation]] is part of, and does not extend, any period bought under this endorsement.

Schedule variables: duration (12, 24, 36 or 72 months); additional premium (a percentage of the expiring annual premium).
