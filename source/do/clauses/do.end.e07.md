---
id: do.end.e07
type: endorsement
heading: E07 Defence Costs in Addition to Limit
since: 1.3.0
changed: 1.4.0
status: draft
trigger:
  questions:
  - qs.do.cover.options_requested
  rules:
  - when: "'E07' in qs.do.cover.options_requested"
    action: broker_option
  reason: Offered because you asked for defence costs to be paid in addition to the limit of liability.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

[[ref:do.pay.defence-costs]] is deleted and replaced with: “Defence costs are payable in addition to the limit of liability. This means that the cost of defending a claim does not reduce the amount available to pay compensatory damages.”

Additional sub-limit for defence costs: as shown in the schedule. If the schedule shows no sub-limit, the sub-limit is 25% of the Overall Aggregate shown in Item 3(g) of the schedule.

Schedule variables: Defence costs sub-limit, if any (25% of the Overall Aggregate applies if none is shown).
