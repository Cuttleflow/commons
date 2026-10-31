---
id: lld.end.e11
type: endorsement
heading: E11 Interested Party
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.lld.policy.interested_party
  rules:
  - when: qs.lld.policy.interested_party == yes
    action: apply
  reason: Applies because an interested party was named.
  responses:
  - Attach
  - Do not attach
---

The interest of the party named in the schedule for this endorsement is noted. Noting an interest does not make that party an insured and gives it no right to claim, but we will tell it if this policy is cancelled, if you agree that we may do so.

Schedule variables: interested party name and interest.
