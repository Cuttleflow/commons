---
id: hom.end.e07
type: endorsement
heading: E07 Strata Lot Owner
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.hom.property.dwelling_type
  rules:
  - when: qs.hom.property.dwelling_type == strata_lot
    action: apply
  reason: Applies because the home is a lot in a strata scheme.
  responses:
  - Attach
  - Do not attach
---

The home is a lot in a strata scheme. Fixtures and improvements in the lot that you own and that the body corporate does not insure, such as floor coverings, internal paint and built-in fittings you added, are contents. If the body corporate recovers from you the excess under its building policy for damage to the lot that this policy would have covered, we pay that excess, up to the limit shown in the schedule for this endorsement.

Schedule variables: body corporate excess limit (default $5,000).
