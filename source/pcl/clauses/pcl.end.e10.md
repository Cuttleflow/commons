---
id: pcl.end.e10
type: endorsement
heading: E10 Interested Party
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pcl.policy.interested_party
  rules:
  - when: qs.pcl.policy.interested_party == yes
    action: apply
  reason: Applies because an interested party was named.
  responses:
  - Attach
  - Do not attach
---

The interest of the party named in the schedule for this endorsement is noted. Noting an interest does not make that party an insured and gives it no right to claim. Where the schedule says so, we pay a claim for an item in which that party has an interest to that party and you jointly. We will tell it if this policy is cancelled, if you agree that we may do so.

Schedule variables: interested party name, interest and items affected.
