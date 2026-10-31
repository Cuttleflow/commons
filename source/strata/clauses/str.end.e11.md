---
id: str.end.e11
type: endorsement
heading: E11 Commercial Occupancy
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.str.occupancy.hazardous_tenancy
  rules:
  - when: qs.str.occupancy.hazardous_tenancy == yes
    action: refer
  reason: Referred because a lot is used for a higher-hazard commercial occupancy, such as cooking with deep fryers, a gym or a workshop.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The schedule names the lots and the occupancy. Where the occupancy uses cooking equipment, the kitchen exhaust system serving it must be cleaned by a professional at least every six months; where it uses other hazardous processes, the precautions named in the schedule apply. [[ref:str.cond.insurance-contracts-act]] applies to these steps.

Schedule variables: lots and occupancy; precautions; special excess.
