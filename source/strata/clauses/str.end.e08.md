---
id: str.end.e08
type: endorsement
heading: E08 Interested Party
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.str.interested_parties
  rules:
  - when: qs.str.interested_parties == yes
    action: apply
  reason: Applied because the body corporate has asked us to note an interested party.
  responses:
  - Attach
  - Do not attach
---

The interest of the party named in the schedule for this endorsement is noted. Noting an interest does not make that party an insured and gives it no right to claim, but we will tell it if this policy is cancelled, if you agree that we may do so.

Schedule variables: interested party name and interest.
