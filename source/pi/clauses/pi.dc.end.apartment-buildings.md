---
id: pi.dc.end.apartment-buildings
type: endorsement
heading: Apartment Buildings Sub-limit
profession: design-construct
since: 1.0.0
status: draft
note: Class 2 buildings and buildings over three storeys refer (decision D9 of Linear PLT-1405), because the developer and builder owe the non-delegable statutory duty in s 37 of the Design and Building Practitioners Act 2020 (NSW) and cannot apportion it (Pafburn Pty Ltd v The Owners - Strata Plan No 84674 [2024] HCA 49).
trigger:
  questions:
    - qs.pi.dc.class2_pct
    - qs.pi.dc.max_storeys
  rules:
    - when: qs.pi.dc.class2_pct > 0 or qs.pi.dc.max_storeys > 3
      action: refer
  reason: Applies because {qs.pi.dc.class2_pct}% of your work with design responsibility is for Class 2 buildings, or the buildings you design are over three storeys.
  responses:
    - Attach
    - Attach with amended sub-limit
    - Attach with premium loading
    - Do not attach
    - Decline risk
---

For all claims arising from professional services for a Class 2 building under the National Construction Code, or for any building of more than three storeys, the most we will pay in total, including defence costs, is the sub-limit shown in the schedule for this endorsement. The sub-limit is part of, and not in addition to, the limit of liability.

[WP REVIEW: confirm whether this sub-limit may apply to a registered building practitioner once the insurance requirement under the Design and Building Practitioners Act 2020 (NSW) commences.]
