---
id: car.end.e03
type: endorsement
heading: E03 Delay in Start-Up Extensions
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.car.s3.required
  rules:
  - when: qs.car.s3.required == yes
    action: refer
  reason: Referred because delay in start-up cover was asked for; the extensions are considered with it.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

This endorsement applies only while [[ref:car.section.delay|heading]] applies. [[ref:car.cover.delay]] also covers delay to practical completion caused by:

- damage at the premises of a supplier named in the schedule to materials or equipment being made for the project;
- interruption to the supply of electricity, gas, water or telecommunications to the project site, caused by damage to the supplier's property; and
- prevention of access to the project site by a public authority because of damage to property within the distance shown in the schedule.

The sub-limit for each item is shown in the schedule and is part of the sum insured for [[ref:car.section.delay|heading]].

Schedule variables: named suppliers; sub-limit for each item; access distance (default 1 km).
