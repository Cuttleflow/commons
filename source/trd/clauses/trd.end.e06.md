---
id: trd.end.e06
type: endorsement
heading: E06 Roof Work Conditions
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trd.business.trade
  - qs.trd.ops.roof_work
  rules:
  - when: qs.trd.business.trade == 3223
    action: refer
  - when: qs.trd.ops.roof_work == yes
    action: apply
  reason: Applies because you open roofs or replace roof coverings. A roofing business is referred to an underwriter.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

When you open a roof, or remove or replace roof sheeting, tiles or flashing, you must cover the opening with a secured weatherproof temporary covering:

- at the end of each working day; and
- before you leave the site at any time when rain or strong wind is forecast for the area by the Bureau of Meteorology.

The special excess shown for this endorsement applies to each occurrence of property damage caused by water or wind entering through a roof opening you made or left. If you did not cover the opening as this endorsement requires, [[ref:trd.cond.insurance-contracts-act]] applies.

Schedule variables: special excess (default: $2,500).
