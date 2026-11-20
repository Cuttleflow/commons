---
id: isr.end.accr
type: endorsement
heading: ACCR Accounts Receivable
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  rules:
  - when: '''ACCR'' in qs.isr.cover.options_requested'
    action: broker_option
  reason: Offered as an option for accounts receivable.
---

Where Damage covered by this Policy to your records means you cannot collect money owed to you by customers, we pay the outstanding balances you cannot recover because of that Damage, the reasonable extra cost of collecting the rest, interest on any loan you take to cover delayed collections, and the cost of reconstructing the records, up to the sub-limit shown in the Schedule. We calculate the amount from your average monthly outstanding balances in the 12 months before the Damage. We do not pay for bookkeeping errors, dishonesty, or loss caused by a cyber event (see CYBX).

Schedule variables: sub-limit.
