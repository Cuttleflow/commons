---
id: mot.hmv.end.e18
type: endorsement
heading: E18 Owner-Driver
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.hmv.vehicles.powered_count
  rules:
  - when: qs.hmv.vehicles.powered_count == 1
    action: suggest
  reason: Suggested because one Powered vehicle is insured.
  responses:
  - Attach
  - Do not attach
---

Where one Powered vehicle is insured and the Named insured is a sole trader, or a company with one working director, who drives it, the driver basis is the Named insured or that director and the relief drivers shown in the Schedule. The unlisted driver excess in [[ref:mot.hmv.cond.excess]] applies when anyone else drives the vehicle.

Schedule variables: relief drivers.
