---
id: pa.end.e02
type: endorsement
heading: E02 Business Expenses
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.cover.business_expenses
  rules:
  - when: qs.pa.cover.business_expenses > 0
    action: refer
  reason: Offered because cover was requested for {qs.pa.cover.business_expenses} a week of business expenses.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

If you are self-employed or a working director of your own company, and you are receiving weekly benefits for temporary total disablement, we will also reimburse the fixed expenses of your business that you continue to pay, up to the weekly business expenses amount shown in the schedule, for up to 26 weeks of any one disablement.

Fixed expenses are rent, electricity, gas, telephone and internet, equipment lease and loan repayments, insurance premiums, accounting fees, and the wages of employees who are not employed to generate income in your place. They do not include your own remuneration, the cost of stock, or the cost of a person employed to replace you.

Schedule variables: weekly business expenses amount; benefit period for this endorsement (default 26 weeks).
