---
id: gpa.gig.end.e20
type: endorsement
heading: E20 Hospital Admission Benefit
since: 1.0.0
status: draft
note: Contains a WP REVIEW tag for the Wording Partner.
trigger:
  questions:
  - qs.gpa.gig.hospital_benefit
  rules:
  - when: qs.gpa.gig.hospital_benefit == yes
    action: refer
  reason: Referred for legal sign-off before a hospital admission benefit is attached.
  responses:
  - Attach
  - Do not attach
---

If an injury covered under this policy results in you being admitted to a hospital as an inpatient within 30 days after the accident, we will pay a lump sum of the amount shown in the schedule (default $1,000), once for each accident. The lump sum is a fixed amount: it does not depend on how long you stay in hospital or on the treatment you receive.

[WP REVIEW: confirm that a fixed lump sum paid on admission is not "calculated by reference to, or contingent on, the time a person is a hospital patient" under rule 13 of the Private Health Insurance (Health Insurance Business) Rules 2018 (Cth). Until confirmed this endorsement refers for legal sign-off.]

Schedule variables: lump sum amount.
