---
id: car.end.e04
type: endorsement
heading: E04 Demolition and Asbestos Removal
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.car.risk.demolition
  - qs.car.risk.asbestos_known
  rules:
  - when: qs.car.risk.demolition == yes or qs.car.risk.asbestos_known == yes
    action: refer
  restrictions:
  - when: qs.car.risk.demolition == yes and this endorsement is not attached
    action: refer
    note: Demolition projects are written only with the conditions in this endorsement.
  reason: Referred because the project includes demolition or the removal of known asbestos.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

This endorsement applies to projects that include demolition or the planned removal of asbestos. The following conditions apply to those projects:

- demolition is carried out by a contractor licensed for that class of demolition in the state or territory of the project site, under a written safe work method statement;
- asbestos is removed only by a licensed asbestos removalist, under an asbestos removal control plan, with clearance certificates obtained; and
- adjoining property is surveyed before demolition starts.

[[ref:car.excl.asbestos]] does not apply to damage to the contract works caused by an accident during the planned removal, up to the asbestos sub-limit shown in the schedule for this endorsement. We do not pay the planned cost of the removal itself.

Schedule variables: projects or demolition scope; asbestos sub-limit; special excess.
