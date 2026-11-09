---
id: cpo.end.e10
type: endorsement
heading: E10 Residential Tenancies
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.cpo.occupancy.residential_pct
  rules:
  - when: qs.cpo.occupancy.residential_pct > 0
    action: refer
  reason: "{qs.cpo.occupancy.residential_pct}% of the floor area is residential; the issuer checks whether the client is a retail client."
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

Part of the building, shown in the schedule for this endorsement, is let for residential use. Those tenancies are covered as part of the building. Their contents, and the liability of their tenants, are not covered. Where a residential tenancy legislation requires you to repair the tenancy, this policy covers the cost of repair only where the damage is covered by [[ref:cpo.section.property]].

Schedule variables: residential tenancies and their share of the floor area.
