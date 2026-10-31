---
id: pi.et.end.vet-student-loans
type: endorsement
heading: VET Student Loans Exclusion
profession: education-training
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.et.vsl_approved
  rules:
  - when: qs.pi.et.vsl_approved = yes
    action: refer
  reason: Applies because you are an approved VET Student Loans provider.
---

We do not cover any claim, loss or liability arising from your participation in the VET Student Loans program, including any requirement to repay or re-credit loan amounts.
