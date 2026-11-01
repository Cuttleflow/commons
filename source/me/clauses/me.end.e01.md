---
id: me.end.e01
type: endorsement
heading: E01 Obstetrics Buy-back
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.me.ops.obstetrics
  rules:
  - when: qs.me.ops.obstetrics == yes
    action: refer
  reason: Referred because a facility provides obstetrics services.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:me.excl.obstetrics]] is deleted, in whole or in part, for the obstetrics services and facilities described in the schedule, subject to the sub-limit, additional excess and clinical governance conditions stated there. For a private hospital, Endorsement E15 states further conditions that apply.

Schedule variables: obstetrics services and facilities; sub-limit; additional excess; clinical governance conditions.
