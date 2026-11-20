---
id: mcg.end.e11
type: endorsement
heading: E11 Delay Extra Expense
since: 1.2.0
status: draft
trigger:
  questions:
  - qs.mcg.cover.delay_extra_expense
  rules:
  - when: qs.mcg.cover.delay_extra_expense == yes
    action: apply
  reason: Applies because you asked for cover for extra expense caused by delay.
  responses:
  - Attach with premium loading
  - Attach with amended sub-limit
  - Do not attach
---

If loss of or damage to the goods that this policy insures delays the delivery of the goods, or of goods that replace them, we pay the reasonable extra expense you incur to reduce the effect of the delay on your business, such as:

- the extra cost of sending replacement goods by a faster means of transport;
- the extra cost of buying replacement goods from another supplier; and
- overtime and extra labour to repair, sort or process the goods.

We pay only the amount by which these costs exceed what you would have spent if the loss or damage had not happened. We pay extra expense incurred within the period shown in the schedule for this endorsement after the loss or damage. The most we pay is the limit for any one loss, and in total for the policy period the aggregate limit, shown in the schedule for this endorsement. The excess shown in the schedule for this endorsement applies once to each loss.

We deduct any amount paid for the same cost under [[ref:mcg.ext.transit-interruption-costs]] or under the Institute Clauses. [[ref:mcg.excl.delay-and-market]] does not apply to the extra expense this endorsement pays. It still applies to loss of market, loss of profit, and any penalty or liquidated damages you must pay under a contract.

Schedule variables: limit any one loss (default $25,000); aggregate limit for the policy period (default $100,000); period after the loss or damage (default 90 days); excess (default $1,000).
