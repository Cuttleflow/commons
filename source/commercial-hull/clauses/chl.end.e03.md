---
id: chl.end.e03
type: endorsement
heading: E03 Passenger Vessels
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.chl.vessel.use_category
  rules:
  - when: qs.chl.vessel.use_category == 1
    action: apply
  reason: Applies because the vessel is a Class 1 passenger vessel.
---

For a Class 1 vessel:

- you must count the passengers boarding and leaving on each voyage, and record the count;
- every passenger must receive the safety briefing that the vessel's safety management system requires before the vessel leaves; and
- for each claim under [[ref:chl.section.pi|heading]] for the death of, or injury or illness to, a passenger, the passenger excess applies instead of the protection and indemnity excess.

[[ref:chl.cond.insurance-contracts-act]] applies to these conditions.

Schedule variables: passenger excess (default $5,000).
