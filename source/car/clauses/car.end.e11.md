---
id: car.end.e11
type: endorsement
heading: E11 Construction Plant
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.car.s1.plant_si
  - qs.car.s1.hired_plant
  rules:
  - when: qs.car.s1.plant_si > 0 or qs.car.s1.hired_plant == yes
    action: broker_option
  reason: Offered because construction plant is used at the project site.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

Construction plant owned by the insured, and construction plant hired in by it for which it is responsible, is covered under [[ref:car.section.material-damage|heading]] while at the project site or in transit to or from it within Australia, up to the sums insured shown in the schedule for this endorsement.

[[ref:car.excl.breakdown]] applies. The Meridian Plant and Equipment wording (2026/PEQ/0001) is available for plant cover away from the project site.

Schedule variables: owned plant sum insured; hired-in plant sum insured; plant excess.
