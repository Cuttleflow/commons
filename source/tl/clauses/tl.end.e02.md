---
id: tl.end.e02
type: endorsement
heading: E02 Defence Costs in Addition to the Limit
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.tl.cover.options_requested
  rules:
  - when: '''E02'' in qs.tl.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for defence costs to be paid outside the limit of liability.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

For the [[ref:tl.section.professional-liability|heading]] section and the [[ref:tl.section.cyber|heading]] section, [[ref:tl.pay.limits-of-liability]] is amended so that defence costs are payable in addition to, and do not reduce, the limit of liability.

The most we will pay for defence costs under this endorsement is the defence costs cap shown in the schedule for this endorsement or, if no amount is shown, an amount equal to the limit of liability. Once the cap is exhausted, further defence costs are payable within the limit of liability.

Where a claim is only partly covered, defence costs are allocated on a fair and reasonable basis between covered and uncovered matters, as set out in [[ref:tl.pay.allocation]]. Where [[ref:tl.end.e01]] applies to a claim, defence costs for that claim are within the limit of liability.

Defence costs under the [[ref:tl.section.liability|heading]] section are already payable in addition to the limit and are not changed by this endorsement.

Schedule variables: defence costs cap.
