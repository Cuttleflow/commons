---
id: chl.end.e07
type: endorsement
heading: E07 Northern Waters in the Cyclone Season
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.chl.vessel.northern_waters
  rules:
  - when: qs.chl.vessel.northern_waters == true
    action: apply
  reason: Applies because the vessel is kept in northern waters during the cyclone season.
---

While the vessel is in northern waters during the cyclone season:

- you must keep and follow a written cyclone plan that says where and how the vessel will be secured, moved or hauled out when a named cyclone threatens; and
- the named cyclone excess applies, instead of the basic excess, to loss of or damage to the vessel caused by a named cyclone.

[[ref:chl.cond.insurance-contracts-act]] applies to the cyclone plan condition.

Schedule variables: named cyclone excess (default 5% of the agreed value, and not less than the basic excess).
