---
id: ah.end.e01
type: endorsement
heading: E01 Facility-based Intrapartum Midwifery Care
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.ah.practice.profession
  - qs.ah.practice.facility_intrapartum
  rules:
  - when: qs.ah.practice.profession == midwifery and qs.ah.practice.facility_intrapartum == yes
    action: refer
  reason: Referred because you are a midwife providing intrapartum care in a licensed facility.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

Available to registered midwives. [[ref:ah.excl.obstetrics]] does not apply to intrapartum care (active labour, delivery, and the 24-hour post-partum period) provided by the insured midwife within a licensed healthcare facility, within the midwife's scope of practice and any collaborative arrangements required by law. Intrapartum care at homebirths and in all other non-facility settings remains excluded and cannot be endorsed under this product.

The midwife must hold the current endorsement or credentialing required by the facility. Privately practising midwives requiring intrapartum homebirth cover should seek cover under the Commonwealth-supported midwife professional indemnity arrangements.

Schedule variables: facilities; special excess (optional); sub-limit (optional).
