---
id: dli.end.e04
type: endorsement
heading: E04 Mixed-Use Buildings
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.dli.building.commercial_lots
  rules:
  - when: qs.dli.building.commercial_lots > 0
    action: apply
  reason: Applies because the building has {qs.dli.building.commercial_lots} non-residential lots.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

The building contains lots that are not used for residential purposes. This policy covers relevant defects in the building elements of the common property of the whole building, including the parts that serve those lots.

We do not pay to rectify a defect in the fit-out of a non-residential lot, or for a non-residential lot owner's or occupier's loss of income, loss of rent or business interruption.

Schedule variables: the number of non-residential lots and their use.
