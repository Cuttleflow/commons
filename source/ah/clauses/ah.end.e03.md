---
id: ah.end.e03
type: endorsement
heading: E03 Practice Entity as Named Insured
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.ah.practice.entity_insured
  rules:
  - when: qs.ah.practice.entity_insured == yes
    action: apply
  reason: Applies because you practise through a company, partnership or trust that you asked us to name.
---

The definition of you, your and insured person is extended to include the company, partnership or trust named in the schedule through which the insured conducts the practice, but only for civil liability arising from professional services provided by insured persons and covered by this policy, and never for the entity's trading debts, employment practices, or directors' and officers' liability. The limit of liability is not increased.

Schedule variables: practice entity name and ABN.
