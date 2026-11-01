---
id: car.end.e06
type: endorsement
heading: E06 Piling, Deep Excavation and Dewatering
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.car.risk.excavation_depth_m
  - qs.car.risk.piling
  - qs.car.risk.dewatering
  rules:
  - when: qs.car.risk.excavation_depth_m > 3 or qs.car.risk.piling == yes or qs.car.risk.dewatering == yes
    action: refer
  reason: Referred because the project includes piling, excavation deeper than 3 metres or dewatering.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

This endorsement applies to projects with piling, excavation deeper than 3 metres or dewatering. The following conditions apply:

- a geotechnical investigation is completed before work starts, and its recommendations are followed;
- excavations are supported as the design requires, and support is inspected daily while open; and
- dewatering systems have stand-by pumps and power available at all times.

We do not pay for the cost of additional support, grouting or dewatering needed because ground conditions differ from those expected, unless damage happens. [[ref:car.ext.vibration-and-support]] applies subject to the special excess shown for this endorsement.

Schedule variables: maximum excavation depth; special excess.
