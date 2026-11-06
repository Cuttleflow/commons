---
id: peq.end.e11
type: endorsement
heading: E11 Wet Works
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.peq.ops.wet_works
  rules:
  - when: qs.peq.ops.wet_works == yes
    action: refer
  reason: Referred because insured plant will work on pontoons or barges, in tidal zones, or from the bank of a waterway.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:peq.excl.waterborne-airborne]] does not apply to the items of specified plant named in the schedule for this endorsement while they work on a pontoon or barge, in a tidal zone, or from the bank of a waterway, if:

- the pontoon or barge has a current survey for the load it carries, and the plant is secured to it as the survey or a competent person requires; and
- the work follows a written plan for tides, weather and water levels, and work stops when they exceed the plan's limits.

We do not pay for loss or damage caused by the plant falling into the water where it was not secured as this endorsement requires, or for loss or damage to the pontoon or barge itself.

The wet works excess shown in the schedule applies to loss or damage that happens on or over water, instead of the item's excess, where it is higher.

Schedule variables: items covered; wet works excess (default 10% of the loss, minimum $10,000).
