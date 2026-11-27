---
id: nur.end.e07
type: endorsement
heading: E07 Retail Visitors
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.nur.business.retail_visitors
  rules:
  - when: qs.nur.business.retail_visitors == yes
    action: apply
  reason: Applies because retail customers visit the situation.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

This endorsement applies where retail customers or other members of the public visit the situation.

- Keep the areas open to customers, including walkways, car parks and display benches, in a reasonable condition, and inspect them each trading day for spills, trip hazards, unstable or overhanging plants and pots, and damaged trolleys.
- Keep a record of each incident that injures a customer or damages their property, and tell us about it as [[ref:nur.obl.tell-us-about-claims]] requires.

The special excess applies to each claim for personal injury to a customer. If a condition of this endorsement was not met, [[ref:nur.cond.insurance-contracts-act]] applies.

Schedule variables: special excess (default: the excess shown for [[ref:nur.section.liability|heading]]).
