---
id: cy.end.e02
type: endorsement
heading: E02 Defence Costs in Addition to the Limit
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.cy.cover.options_requested
  rules:
  - when: '''E02'' in qs.cy.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for defence costs to be paid outside the limit of liability.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

[[ref:cy.pay.defence-costs]] is amended so that defence costs are payable in addition to, and do not reduce, the limit of liability.

The most we will pay for defence costs under this endorsement is the defence costs cap shown in the schedule for this endorsement or, if no amount is shown, an amount equal to the limit of liability. Once the cap is exhausted, further defence costs are payable within the limit of liability.

Where a claim is only partly covered, defence costs are allocated on a fair and reasonable basis between covered and uncovered matters. Where [[ref:cy.end.e11]] applies to a claim, defence costs for that claim are within the limit of liability.

Schedule variables: defence costs cap.
