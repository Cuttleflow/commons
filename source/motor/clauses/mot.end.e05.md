---
id: mot.end.e05
type: endorsement
heading: E05 Agreed Value
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.vehicles.agreed_value_count
  rules:
  - when: qs.mot.vehicles.agreed_value_count > 0
    action: apply
  reason: Applies because {qs.mot.vehicles.agreed_value_count} vehicle(s) are insured for an agreed value.
  responses:
  - Attach
  - Do not attach
---

Each Insured vehicle shown in the Schedule for this Endorsement is insured for its Agreed value, and [[ref:mot.pay.basis-of-settlement]] settles a Total loss on that basis. The Agreed value is fixed at inception or renewal and does not change because the Schedule is reissued for another reason.

Schedule variables: vehicles covered; Agreed value of each.
