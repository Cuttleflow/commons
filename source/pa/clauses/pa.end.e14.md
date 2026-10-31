---
id: pa.end.e14
type: endorsement
heading: E14 Confirmation of Cover for a Principal
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.cover.site_confirmation
  rules:
  - when: qs.pa.cover.site_confirmation == yes
    action: apply
  reason: Applied because a contract or site requires confirmation of personal accident cover.
  responses:
  - Attach
  - Do not attach
---

We will give the principal named in the schedule for this endorsement a written confirmation that this policy is in force, showing the capital sum and weekly benefit. The confirmation does not change this policy, and gives the principal no right to claim under it or to receive any benefit.

We will tell the principal if this policy is cancelled before the end of the policy period, if you agree that we may do so.

Schedule variables: principal name and contract or site reference.
