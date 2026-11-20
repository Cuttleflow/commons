---
id: chl.end.e10
type: endorsement
heading: E10 Loss of Hire
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.chl.cover.loss_of_hire
  rules:
  - when: qs.chl.cover.loss_of_hire == true
    action: refer
  reason: Applies because you asked for loss of hire cover.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

If the vessel is damaged by a peril insured under [[ref:chl.section.hull|heading]] on full conditions, and we pay the claim or would pay it but for the excess, we pay the agreed daily amount for each day the vessel cannot operate in your business because of the damage, after the waiting period, up to the maximum number of days.

We do not pay for days lost to lay-up, to work done at the same time that is not needed to repair the damage, or to delay in starting repairs that you could reasonably have avoided.

Schedule variables: agreed daily amount; waiting period (default 7 days); maximum days (default 30).
