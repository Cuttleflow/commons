---
id: mot.end.e18
type: endorsement
heading: E18 Sole Operator
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.fleet.vehicle_count
  rules:
  - when: qs.mot.fleet.vehicle_count == 1
    action: suggest
  reason: Suggested because one vehicle is insured.
  responses:
  - Attach
  - Do not attach
---

Where one vehicle is insured and the Named insured is a sole trader or a company with one working director, the driver basis is the Named insured or that director and any driver shown in the Schedule, the declarations in [[ref:mot.fleet.declarations]] do not apply, and the premium is fixed for the Period of Insurance.

Schedule variables: drivers.
