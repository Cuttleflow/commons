---
id: car.end.e05
type: endorsement
heading: E05 Residential Multi-Storey
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.car.project.type
  - qs.car.project.storeys
  - qs.car.risk.combustible_cladding
  rules:
  - when: qs.car.project.type == res_multi_unit and (qs.car.project.storeys > 3 or qs.car.risk.combustible_cladding != no)
    action: refer
  - when: qs.car.project.type == res_multi_unit
    action: apply
  reason: Applies because the project is residential with more than one dwelling; referred if it is above 3 storeys or combustible cladding is declared.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

This endorsement applies to residential projects of more than one dwelling. The following conditions apply:

- the insured holds the builder's licence and any home building compensation cover required in the state or territory of the project site;
- no combustible external cladding is installed unless it complies with the building code in force and a fire engineer has certified it; and
- fire protection systems for the completed building are installed and commissioned before occupation.

We do not pay for the cost of removing or replacing external cladding because it does not comply with building law, whether or not damage has happened.

Schedule variables: number of storeys covered; special excess, if any.
