---
id: car.end.e12
type: endorsement
heading: E12 Fitness-for-Purpose Design Warranty
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.car.s4.required
  - qs.car.s4.ffp_warranty
  rules:
  - when: qs.car.s4.required == yes and qs.car.s4.ffp_warranty == yes
    action: refer
  reason: Referred because the construction contract requires a fitness-for-purpose design warranty.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

This endorsement applies only while [[ref:car.section.design-pi|heading]] applies, and only to the construction contracts named in the schedule for this endorsement.

[[ref:car.excl.design-pi]] does not exclude liability under an express warranty in a named construction contract that the design will be fit for its purpose. The most we will pay for that liability is the sub-limit shown in the schedule, which is part of the limit of liability for [[ref:car.section.design-pi|heading]].

Schedule variables: construction contracts named; sub-limit.
