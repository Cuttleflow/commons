---
id: trv.amt.end.e18
type: endorsement
heading: E18 Conditions Not Accepted After Screening
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trv.amt.screening_outcome
  rules:
  - when: qs.trv.amt.screening_outcome == exclude
    action: refer
  reason: Referred because medical screening did not accept a declared condition; the underwriter confirms the condition is excluded.
  responses:
  - Attach
  - Do not attach
  - Decline risk
---

We do not pay any claim arising from the conditions shown in the schedule for this endorsement, for the insured persons named, including a claim for cancelling or cutting short a trip because of them. This applies whether or not the condition is a pre-existing condition. It does not affect cover for any other condition, or for the other insured persons.

Schedule variables: insured persons; conditions not accepted.
