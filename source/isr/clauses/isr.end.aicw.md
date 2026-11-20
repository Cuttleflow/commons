---
id: isr.end.aicw
type: endorsement
heading: 'AICW Additional Increased Cost of Working: Separate Limit'
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.policy.base_wording
  - qs.isr.bi.insured
  rules:
  - when: qs.isr.policy.base_wording != 'meridian' and qs.isr.bi.insured == yes
    action: apply
  reason: Applies because the base wording does not give additional increased cost of working its own limit.
---

Additional increased cost of working is reasonable extra expenditure you incur to keep the business running or to reduce the interruption, beyond the amount that would be justified by the loss it avoids. We pay it up to the separate amount shown in the Schedule. That amount is in addition to the sum insured for gross profit, gross revenue or gross rentals, and within the Limit of Liability.

Schedule variables: additional increased cost of working sum insured.
