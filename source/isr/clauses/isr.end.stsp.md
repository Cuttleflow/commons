---
id: isr.end.stsp
type: endorsement
heading: STSP Stock at Selling Price
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.risk.anzsic_division
  rules:
  - when: '''STSP'' in qs.isr.cover.options_requested'
    action: broker_option
  - when: qs.isr.risk.anzsic_division == 'C'
    action: suggest
  reason: Suggested because the business is a manufacturer.
---

Finished stock that you manufactured, and that has been sold but not delivered, is valued at its selling price less any costs you save because of the Damage (such as delivery costs, commission and discounts not incurred). All other stock is valued as the Base Wording provides. We do not pay twice for the same loss under the Material Damage and Business Interruption covers.

Schedule variables: none.
