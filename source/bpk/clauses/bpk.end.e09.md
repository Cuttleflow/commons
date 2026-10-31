---
id: bpk.end.e09
type: endorsement
heading: E09 Interests of Lessors and Financiers
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.bpk.insured.interested_parties_count
  rules:
  - when: qs.bpk.insured.interested_parties_count > 0
    action: apply
  reason: Applies because you asked us to note a lessor or financier.
  responses:
  - Attach
  - Do not attach
---

The interest of each lessor or financier listed in the Schedule is noted as an Interested party under [[ref:bpk.cond.subrogation-and-interested-parties]].

Schedule variables: names of lessors and financiers; property in which each has an interest.
