---
id: isr.end.stkd
type: endorsement
heading: STKD Stock Declaration and Premium Adjustment
since: 1.1.0
status: draft
note: Contains 1 WP REVIEW tag for the Wording Partner.
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.risk.seasonal_stock
  rules:
  - when: '''STKD'' in qs.isr.cover.options_requested'
    action: broker_option
  - when: qs.isr.risk.seasonal_stock == yes
    action: suggest
  reason: Suggested because stock levels are seasonal.
---

- The Declared Value for stock at each Situation is the maximum value shown in the Schedule. Premium on stock is charged on that maximum as a deposit.
- Within 30 days after the end of each declaration period, declare the value of stock at each Situation on the last day of the period, or the highest value during the period if the Schedule says so.
- At the end of the Period of Insurance we calculate the stock premium on the average of the values declared. We refund any amount by which the deposit exceeds that premium, subject to the minimum premium shown, and charge additional premium if the average exceeds the maximum.
- If a declaration is not made, the maximum value is treated as declared for that period.
- If the last declaration before the Damage was less than the actual value of stock on its date, we pay the proportion of the stock loss that the declared value bears to the actual value. [WP REVIEW: check this reduction against section 54.]

Schedule variables: maximum stock value per Situation; declaration period (monthly or quarterly); basis (last day or highest); minimum premium.
