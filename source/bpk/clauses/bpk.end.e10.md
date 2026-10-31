---
id: bpk.end.e10
type: endorsement
heading: E10 Hot Works
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.bpk.liability.hot_works_away
  rules:
  - when: qs.bpk.liability.hot_works_away == yes
    action: apply
  reason: Applies because you carry out hot works away from your premises.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

[[ref:bpk.liability.excl.hot-works]] does not apply where, for each hot works job away from your Premises, you hold any permit required, remove or protect combustible material within the distance shown in the Schedule, keep a fire extinguisher at hand, and keep watch for the time shown in the Schedule after the work ends. [[ref:bpk.cond.insurance-contracts-act]] applies to these requirements.

Schedule variables: clearance distance; fire watch time; special excess (optional).
