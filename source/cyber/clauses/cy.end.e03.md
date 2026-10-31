---
id: cy.end.e03
type: endorsement
heading: E03 End-of-Life Software
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.cy.security.eol_software
  rules:
  - when: qs.cy.security.eol_software == yes
    action: refer
  reason: Applies because you run software or an operating system that the vendor no longer supports with security patches.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:cy.excl.unsupported-software]] does not apply to the systems and software listed in the schedule for this endorsement.

For any insured loss or claim arising from a cyber event that exploits a vulnerability in listed end-of-life software, you bear the co-insurance percentage shown in the schedule of each amount otherwise payable, in addition to the excess.

You must maintain the compensating controls described in the schedule (such as network segmentation, virtual patching, or endpoint monitoring) for each listed system. If you do not, we may reduce our liability to the extent that the failure caused or contributed to the loss or prejudiced us, as s.54 of the Insurance Contracts Act 1984 (Cth) allows.

Schedule variables: listed systems and software; co-insurance percentage (default 20%); compensating controls.
