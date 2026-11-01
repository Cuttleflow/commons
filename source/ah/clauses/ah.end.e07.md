---
id: ah.end.e07
type: endorsement
heading: E07 Cosmetic and Aesthetic Procedures
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.ah.practice.cosmetic_procedures
  rules:
  - when: qs.ah.practice.cosmetic_procedures == yes
    action: refer
  reason: Referred because you perform cosmetic or aesthetic procedures.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

Professional services are extended to include the non-surgical cosmetic or aesthetic procedures described in the schedule (for example, cosmetic injectables administered by a dentist for an aesthetic purpose), provided each procedure is within the insured's scope of practice, is performed in accordance with the relevant National Board's guidelines on cosmetic procedures, and, where a prescription-only substance is used, [[ref:ah.excl.prescription-medicines]] is satisfied.

Schedule variables: procedures named; special excess (optional); sub-limit (optional).
