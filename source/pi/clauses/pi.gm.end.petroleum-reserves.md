---
id: pi.gm.end.petroleum-reserves
type: endorsement
heading: Petroleum Reserves Estimation
profession: geoscience-mineral
since: 1.0.0
status: draft
note: Adds cover.
trigger:
  questions:
  - qs.pi.gm.petroleum_pct
  rules:
  - when: qs.pi.gm.petroleum_pct > 0
    action: broker_option
  reason: Offered because you estimate petroleum reserves.
---

Paragraph (b) of [[ref:pi.gm.excl.excluded-activities]] does not apply to the estimation and evaluation of petroleum reserves and resources, if the work is carried out under the Petroleum Resources Management System or an equivalent standard shown in the schedule.
