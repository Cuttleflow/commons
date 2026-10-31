---
id: bpk.end.e11
type: endorsement
heading: E11 Voluntary Workers' Personal Accident
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.bpk.insured.voluntary_workers
  rules:
  - when: qs.bpk.insured.voluntary_workers > 0
    action: broker_option
  reason: Offered because {qs.bpk.insured.voluntary_workers} voluntary workers help the Business.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

We pay the benefits shown in the Schedule if a voluntary worker suffers accidental bodily injury while doing voluntary work for the Business during the Period of Insurance, resulting in death or the disablement shown in the Schedule.

Schedule variables: benefits; disablements covered; number of voluntary workers.
