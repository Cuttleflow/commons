---
id: cy.end.e08
type: endorsement
heading: E08 Invoice Manipulation Fraud
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.cy.cover.options_requested
  rules:
  - when: '''E08'' in qs.cy.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for cover for customer payments diverted by fraudulent invoices.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
---

[[ref:cy.section.first-party]] is extended to cover your direct financial loss where a third party, having gained **unauthorised** access to your computer system or email, fraudulently alters or issues invoices or payment instructions in your name, causing amounts properly payable to you to be paid to the fraudster instead.

We will pay the invoiced amounts you are unable to recover from your customer or the receiving institution, provided you make reasonable efforts to recover them and notify affected customers promptly on discovery. You must discover the loss during the policy period and notify us within 30 days of discovery.

This endorsement does not cover amounts lost where the fraudulent instruction did not involve **unauthorised** access to your computer system or email.

Schedule variables: sub-limit.
