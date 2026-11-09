---
id: trd.end.e14
type: endorsement
heading: E14 Lloyd's Underwriters
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trd.insured.lloyds_binder
  rules:
  - when: qs.trd.insured.lloyds_binder == yes
    action: apply
  reason: Applies because the policy is placed with Lloyd's underwriters.
  responses:
  - Attach
  - Do not attach
---

Where the insurer is one or more syndicates at Lloyd's, each syndicate is liable only for its own proportion of any claim, and not for another syndicate's proportion. You may serve proceedings on the Lloyd's General Representative in Australia shown in the schedule, who will accept service for the syndicates. Complaints may also be referred to Lloyd's Australia, and then to the Australian Financial Complaints Authority where its rules allow.

Schedule variables: the syndicates and their proportions; the Lloyd's General Representative in Australia.
