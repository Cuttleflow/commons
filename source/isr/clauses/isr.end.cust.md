---
id: isr.end.cust
type: endorsement
heading: CUST Customers' and Third-Party Property
since: 1.1.0
status: draft
note: Contains 1 WP REVIEW tag for the Wording Partner.
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.risk.warehousing_others_goods
  rules:
  - when: qs.isr.risk.warehousing_others_goods == yes
    action: refer
  - when: '''CUST'' in qs.isr.cover.options_requested'
    action: broker_option
  reason: Offered because the business holds goods belonging to others.
---

The Material Damage cover includes property owned by others and in your care, custody or control at a Situation (including customers' goods, consigned stock, and employees' and visitors' personal effects and tools), where you are legally liable for it or have agreed in writing to insure it, up to the sub-limit shown in the Schedule for any one Situation. Payment to the owner discharges us to the extent of the payment. Where the owner has its own insurance for the property, we pay the amount by which the loss exceeds what that insurance pays. [WP REVIEW: check this excess provision against section 45.]

Schedule variables: sub-limit per Situation.
