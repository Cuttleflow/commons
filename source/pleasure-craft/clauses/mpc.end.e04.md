---
id: mpc.end.e04
type: endorsement
heading: E04 Named Cyclone Excess
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.mpc.storage.zone
  rules:
  - when: qs.mpc.storage.zone == northern
    action: apply
  reason: Applies because the boat is kept or used in northern waters during the cyclone season.
  responses:
  - Attach
  - Attach with special excess
  - Do not attach
---

For damage caused by a named cyclone to the boat while it is afloat, or in a marina berth, in northern waters, the named cyclone excess shown in the schedule for this endorsement applies in place of every other excess: the higher of the amount and the percentage of the claim shown (default $5,000 or 10% of the claim, whichever is higher). Damage by a named cyclone remains covered, subject to [[ref:mpc.excl.moorings-and-rigging]].

Schedule variables: named cyclone excess amount (default $5,000); named cyclone excess percentage (default 10%).
