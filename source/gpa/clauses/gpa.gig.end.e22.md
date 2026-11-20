---
id: gpa.gig.end.e22
type: endorsement
heading: E22 Workers Aged 16 and 17
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.gig.under_18
  rules:
  - when: qs.gpa.gig.under_18 == yes
    action: refer
  reason: Referred because the platform allows workers under 18.
  responses:
  - Attach
  - Do not attach
  - Decline risk
---

In the definition of Covered Person, "at least 18 years old" is replaced by "at least 16 years old", for platform work that the law of the state or territory where it is performed allows a person of that age to do. Weekly benefits for a covered person under 18 are measured against their actual earnings from platform work.

Schedule variables: none.
