---
id: cpo.end.e08
type: endorsement
heading: E08 Interested Party
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.cpo.insured.interested_parties
  rules:
  - when: qs.cpo.insured.interested_parties == yes
    action: apply
  reason: A financier or other party has an interest in the building.
  responses:
  - Attach
  - Do not attach
---

The interest of the party named in the schedule for this endorsement in the building is noted. We pay a claim under [[ref:cpo.section.property]] to that party, or to you and that party jointly, as their interests appear. We will tell that party if we cancel this policy, at the same time as we tell you. An act or omission of yours does not reduce that party's interest, to the extent the law allows.

Schedule variables: name of the interested party; nature of the interest.
