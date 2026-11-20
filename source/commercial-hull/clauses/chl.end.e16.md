---
id: chl.end.e16
type: endorsement
heading: E16 Condition Survey
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.chl.vessel.hull_material
  - qs.chl.vessel.age
  rules:
  - when: qs.chl.vessel.hull_material == TIMBER
    action: refer
  - when: qs.chl.vessel.age > 25
    action: refer
  reason: Applies because the vessel has a timber hull or is more than 25 years old.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

The vessel must have a condition and valuation survey by a marine surveyor we accept, at your cost, before cover starts or within 30 days after it, unless the schedule shows a survey completed in the last 12 months. You must carry out the survey's recommendations by the dates it sets. If the survey values the vessel differently from the agreed value, we may agree a new agreed value with you and adjust the premium.

[[ref:chl.cond.insurance-contracts-act]] applies to these conditions.

Schedule variables: survey date; recommendations and their dates.
