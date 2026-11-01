---
id: ah.end.e02
type: endorsement
heading: E02 Clinical Trials and Approved Research
since: 1.3.0
changed: 1.4.0
status: draft
trigger:
  questions:
  - qs.ah.practice.clinical_trials
  rules:
  - when: qs.ah.practice.clinical_trials == yes
    action: refer
  reason: Referred because you take part in a clinical trial or research project.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

[[ref:ah.excl.clinical-trials]] does not apply to the insured's participation as an investigator or study clinician in a clinical trial or research project named in the schedule, provided the trial or project has current approval from a human research ethics committee constituted under NHMRC guidelines and, where required, complies with the Therapeutic Goods Administration's CTN or CTA scheme. Cover applies in excess of the indemnity given by the trial sponsor that is stated in the schedule.

Schedule variables: trials or projects named; sponsor indemnity; sub-limit (optional).
