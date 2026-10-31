---
id: ml.end.e02
type: endorsement
heading: E02 Defence Costs in Addition to the Limit
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.ml.cover.options_requested
  rules:
  - when: '''E02'' in qs.ml.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for defence costs to be paid outside the limit of liability.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

[[ref:ml.pay.defence-costs]] is amended for the sections shown in the schedule for this endorsement. For those sections, defence costs are payable in addition to the section limit of liability and do not reduce it or the overall aggregate.

The most we will pay for defence costs in addition to the limits during the policy period, for all those sections combined, is the defence costs limit shown in the schedule for this endorsement. Once it is exhausted, further defence costs are payable within the section limit of liability as [[ref:ml.pay.defence-costs]] provides.

Where a claim is brought in the United States of America or Canada under [[ref:ml.end.e03]], defence costs for that claim are always within the limit of liability.

Schedule variables: sections to which it applies; defence costs limit.
