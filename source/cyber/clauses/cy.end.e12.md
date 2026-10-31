---
id: cy.end.e12
type: endorsement
heading: E12 Aggregate Limit Reinstatement
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.cy.cover.options_requested
  rules:
  - when: '''E12'' in qs.cy.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for the limit to be reinstated after a large loss.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

If the limit of liability is exhausted by payment of covered loss, it is reinstated for the rest of the policy period, as many times as the schedule for this endorsement shows (once if no number is shown).

A reinstated limit applies only to claims and insured losses arising from cyber events, dependent events, privacy breaches, or acts, errors or omissions that are not related to those that exhausted the limit, and never increases the amount payable for any single claim, insured loss, or related series.

Each reinstatement attracts the additional premium shown in the schedule, payable when the reinstatement takes effect.

Schedule variables: number of reinstatements (default one); additional premium.
