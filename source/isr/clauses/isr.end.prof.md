---
id: isr.end.prof
type: endorsement
heading: 'PROF Professional and Government Fees: Increased Limit'
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  rules:
  - when: '''PROF'' in qs.isr.cover.options_requested'
    action: broker_option
  reason: Offered as an option to raise the professional fees limit.
---

The sub-limit for professional fees is increased to the amount shown in the Schedule. It covers the fees of architects, surveyors, engineers, quantity surveyors, project managers and lawyers necessarily incurred in reinstating Damaged property, and fees and contributions payable to a government or local authority for approvals needed to reinstate it. Fees for preparing a claim are paid only under CPRC.

Schedule variables: sub-limit.
