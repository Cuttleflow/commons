---
id: pi.bsc.end.apartment-buildings
type: endorsement
heading: Apartment Buildings Sub-limit
profession: building-surveyors-certifiers
since: 1.0.0
changed: 1.1.0
status: draft
trigger:
  questions:
  - qs.pi.bsc.class2_pct
  - qs.pi.bsc.max_storeys
  rules:
  - when: qs.pi.bsc.class2_pct > 25 or qs.pi.bsc.max_storeys > 3
    action: refer
  restrictions:
  - when: sub-limit < statutory minimum limit for the practice state
    action: refer
    note: A sub-limit cannot reduce cover below the minimum limit that a certifier insurance law requires.
  reason: Applies because {qs.pi.bsc.class2_pct}% of your certificates are for apartment buildings, or you certify buildings over three storeys.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

For all claims arising from services for a Class 2 building under the National Construction Code, or for any building of more than three storeys, the most we will pay in total, including defence costs, is the sub-limit shown in the schedule for this endorsement. The sub-limit is part of, and not in addition to, the limit of liability.

[WP REVIEW: confirm whether the NSW minimum limit for certifiers applies to claims for Class 2 buildings, and so whether this sub-limit can lawfully apply.]
