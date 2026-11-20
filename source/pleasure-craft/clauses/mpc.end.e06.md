---
id: mpc.end.e06
type: endorsement
heading: E06 Older Boat
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.mpc.boat.hull_age
  rules:
  - when: "qs.mpc.boat.hull_age > 20"
    action: refer
  reason: "Referred because the hull is {qs.mpc.boat.hull_age} years old."
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The boat is insured for its market value, even where the schedule shows an agreed value, unless the schedule shows that the agreed value was set by a condition and valuation survey that we accepted, and the date of that survey.

We do not pay for damage that results from a defect noted in that survey until the defect has been repaired and you have given us evidence of the repair.

Schedule variables: survey date; whether the agreed value was set by the survey.
