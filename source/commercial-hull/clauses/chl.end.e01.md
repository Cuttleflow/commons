---
id: chl.end.e01
type: endorsement
heading: E01 Operational Area B
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.chl.vessel.operational_area
  rules:
  - when: qs.chl.vessel.operational_area == B
    action: refer
  reason: Applies because the vessel operates in operational area B.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

Cover extends to operational area B where the vessel's certificate of operation allows it. While the vessel is in operational area B:

- it must carry the safety and communication equipment the national law requires for that area, including a registered emergency position-indicating radio beacon;
- the master must hold the certificate of competency the national law requires for that area; and
- the special excess shown in the schedule applies to each claim under [[ref:chl.section.hull|heading]] arising there.

[[ref:chl.cond.insurance-contracts-act]] applies to these conditions.

Schedule variables: special excess (default twice the basic excess).
