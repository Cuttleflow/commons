---
id: mot.end.e15
type: endorsement
heading: E15 Automated Driving Systems
since: 3.0.0
status: draft
note: Contains a WP REVIEW tag for the Wording Partner.
trigger:
  questions:
  - qs.mot.vehicles.automated_count
  rules:
  - when: qs.mot.vehicles.automated_count > 0
    action: refer
  reason: Referred because {qs.mot.vehicles.automated_count} vehicle(s) have an automated driving system.
  responses:
  - Attach
  - Do not attach
  - Decline risk
---

For each Insured vehicle shown in the Schedule as equipped with an automated driving system, cover under this Policy applies while the system is engaged as though the person responsible for the vehicle were driving it, provided the system is used as its manufacturer instructs and its software updates have been installed when issued. [WP REVIEW: align with the Automated Vehicle Safety Law once enacted.]

Schedule variables: vehicles covered.
