---
id: pi.rs.end.expert-witness
type: endorsement
heading: Expert Witness
profession: risk-safety-claims
since: 1.0.0
status: draft
note: Adds cover.
trigger:
  questions:
  - qs.pi.rs.expert_witness
  rules:
  - when: qs.pi.rs.expert_witness = yes
    action: broker_option
  reason: Offered because you give expert evidence.
---

Preparing expert reports for legal proceedings and giving expert evidence are professional services under this policy.

We also pay, under [[ref:pi.ext.inquiry-costs]], your defence costs in responding to a complaint to a professional body arising from your expert evidence.
