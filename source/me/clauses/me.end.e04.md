---
id: me.end.e04
type: endorsement
heading: E04 Clinical Trials
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.me.ops.clinical_trials
  rules:
  - when: qs.me.ops.clinical_trials == yes
    action: refer
  reason: Referred because the company conducts clinical trials or studies.
---

[[ref:me.excl.clinical-trials]] does not apply to the company's liability arising from the specific trials or studies listed in the schedule, provided each has current human research ethics committee approval and the sponsor indemnity stated in the schedule is in place.

Schedule variables: trials or studies; sponsor indemnity; sub-limit (optional).
