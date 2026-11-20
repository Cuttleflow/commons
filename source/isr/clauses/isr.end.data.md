---
id: isr.end.data
type: endorsement
heading: DATA Data and Software Reinstatement
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  rules:
  - when: '''DATA'' in qs.isr.cover.options_requested'
    action: broker_option
  reason: Offered as an option to raise the data restoration limit.
---

Where computer equipment or data storage media are Damaged by a cause covered by this Policy (including a cause written back under CYBX), we pay the reasonable cost of restoring data and software from back-ups or source documents, including technicians' labour, up to the sub-limit shown in the Schedule. We do not pay for the value of the data itself; the cost of recreating data that was not backed up, beyond the amount shown; licence fees; or anything caused by a cyber event that CYBX does not write back.

Schedule variables: sub-limit; limit for recreating data that was not backed up.
