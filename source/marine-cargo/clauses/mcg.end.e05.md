---
id: mcg.end.e05
type: endorsement
heading: E05 Theft-Attractive Goods Excess
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.mcg.goods.theft_attractive_pct
  rules:
  - when: qs.mcg.goods.theft_attractive_pct > 25
    action: apply
  reason: Applies because theft-attractive goods are {qs.mcg.goods.theft_attractive_pct}% of your sendings.
---

The excess shown in the schedule for this endorsement replaces the excess shown in the schedule for each claim for theft, pilferage or non-delivery of theft-attractive goods.

Schedule variables: special excess (default $2,500 or 10% of the claim, whichever is greater).
