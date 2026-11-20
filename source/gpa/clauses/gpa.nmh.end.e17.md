---
id: gpa.nmh.end.e17
type: endorsement
heading: E17 Ambulance at Full Cost
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.nmh.ambulance
  rules:
  - when: qs.gpa.nmh.ambulance == yes
    action: apply
  reason: Applied because the policyholder buys ambulance cover at full cost.
  responses:
  - Attach
  - Do not attach
---

The excess and the percentage in [[ref:gpa.xmed.cover.medical-expenses]] do not apply to the cost of emergency transport by a licensed ambulance service for an injury covered under this policy, to the extent that cost is a non-Medicare medical expense. We pay it in full, up to the limit for each injury.

Schedule variables: none.
