---
id: bpk.end.e03
type: endorsement
heading: E03 Seasonal Stock Increase
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.bpk.situation.seasonal_stock_increase_pct
  rules:
  - when: qs.bpk.situation.seasonal_stock_increase_pct > 50
    action: refer
  - when: qs.bpk.situation.seasonal_stock_increase_pct > 0
    action: broker_option
  reason: Offered because your stock rises by {qs.bpk.situation.seasonal_stock_increase_pct}% in peak months.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

The Stock Sum insured at a Situation is increased by the percentage shown in the Schedule during the months shown in the Schedule.

Schedule variables: Situations; percentage increase; months.
