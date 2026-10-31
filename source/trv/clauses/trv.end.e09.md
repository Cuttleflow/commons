---
id: trv.end.e09
type: endorsement
heading: E09 Pregnancy Extension
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.trv.medical.pregnant
  rules:
  - when: qs.trv.medical.pregnant == yes
    action: refer
  reason: Offered because a traveller will be pregnant during the trip.
  responses:
  - Attach
  - Do not attach
---

In [[ref:trv.excl.pregnancy]], the 26th week of pregnancy is replaced by the 36th week, for a single pregnancy with no complications before departure that a medical practitioner has confirmed in writing.

Schedule variables: insured person.
