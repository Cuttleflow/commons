---
id: me.end.e03
type: endorsement
heading: E03 Cosmetic Procedures Buy-back
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.me.ops.cosmetic_procedures
  rules:
  - when: qs.me.ops.cosmetic_procedures == discrete_unit
    action: refer
  - when: qs.me.ops.cosmetic_procedures == incidental
    action: refer
  reason: Referred because cosmetic procedures are performed at a facility.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:me.excl.cosmetic-procedures]] does not apply to the specific procedures listed in the schedule, subject to the practitioner-qualification, facility-accreditation and sub-limit conditions stated there.

Schedule variables: procedures; practitioner qualifications; facility accreditation; sub-limit.
