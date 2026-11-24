---
id: dli.end.e05
type: endorsement
heading: E05 Modular and Prefabricated Construction
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.dli.building.construction_type
  rules:
  - when: qs.dli.building.construction_type == modular
    action: refer
  reason: Referred because the building is built from volumetric modules or prefabricated panels, which need factory inspections and a review of the connections.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

Some building elements are manufactured off site as volumetric modules or prefabricated panels. The following conditions apply to the building work:

- the technical inspector inspects the manufacture of those building elements at the factory at the stages the technical inspection plan sets out;
- the manufacturer gives the technical inspector its quality records and its certificates of compliance with the Building Code of Australia for those building elements; and
- the technical inspector inspects the connections between modules or panels, and the waterproofing and fire separation at those connections, on site before they are closed in.

If a condition is not met, we may decline to issue the certificate of currency until the technical inspector is satisfied by other means. Once this policy has taken effect, [[ref:dli.cond.protection-of-the-owners-corporation]] applies.

Schedule variables: the building elements manufactured off site; the manufacturer.
