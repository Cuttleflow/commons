---
id: isr.pay.waiting-period
type: payment
heading: Waiting Period
since: 1.1.0
status: draft
---

Where the schedule shows a waiting period for this section or an extension, it is a threshold, not a deduction. If the interruption lasts longer than the waiting period, we measure the loss from the start of the interruption. If it does not, we pay nothing for that interruption. The schedule may instead apply [[ref:isr.end.txsd]], under which the first part of the loss is deducted.

**Worked example.** The waiting period is 3 days and a fire interrupts the Business for 20 days. Because the interruption lasted more than 3 days, we measure the loss for all 20 days.
