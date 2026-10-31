---
id: str.end.e04
type: endorsement
heading: E04 Combustible Cladding
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.str.building.combustible_cladding
  rules:
  - when: qs.str.building.combustible_cladding == yes
    action: refer
  - when: qs.str.building.combustible_cladding == unknown
    action: refer
  reason: Referred because the building has, or may have, combustible external cladding.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The schedule records that external cladding of the type named is on the building, the share of the facade it covers, and any remediation order and its status.

Cover for damage by fire to the building is subject to the special fire excess shown in the schedule for this endorsement. The cost of removing or replacing the cladding is not covered, except where fire or another insured cause damages it, and then only to replace it with non-combustible cladding of the same function.

Schedule variables: cladding type and share of facade; remediation order and status; special fire excess.
