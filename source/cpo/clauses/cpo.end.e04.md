---
id: cpo.end.e04
type: endorsement
heading: E04 Combustible Cladding
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.cpo.building.combustible_cladding
  rules:
  - when: qs.cpo.building.combustible_cladding == yes
    action: refer
  - when: qs.cpo.building.combustible_cladding == unknown
    action: refer
  reason: The building has, or may have, combustible external cladding.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The building has the combustible cladding described in the schedule for this endorsement. Damage caused by or spreading through that cladding is covered, subject to the special excess shown. The cost of removing or replacing the cladding, whether or not it is damaged, is not covered. You agree to carry out the remediation plan shown in the schedule, if any, by the date shown.

Schedule variables: description and extent of the cladding; remediation plan and completion date (default: none); special excess (default: the basic excess).
