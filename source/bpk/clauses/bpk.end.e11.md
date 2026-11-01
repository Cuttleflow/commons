---
id: bpk.end.e11
type: endorsement
heading: E11 Voluntary Workers' Personal Accident
since: 2.1.0
changed: 2.2.0
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

A **voluntary worker** is a person who does voluntary work for the Business and who is not paid for it, other than reimbursement of expenses. **Voluntary work** is work the Business asks the person to do, or agrees to the person doing, in the ordinary activities of the Business, including travelling directly to or from it. **Disablement** means a permanent injury of a kind listed as a disablement covered in the Schedule, confirmed by a registered medical practitioner.

We pay the benefits shown in the Schedule if a voluntary worker suffers accidental bodily injury while doing voluntary work for the Business during the Period of Insurance, resulting in death or a Disablement.

A voluntary worker may also be within the definition of Employee, which includes volunteers. This Endorsement applies to that person as a voluntary worker, and its benefits are not liability cover. It does not change [[ref:bpk.liability.excl.injury-to-employees]], which continues to apply to a claim made against you by that person. We do not pay a benefit under this Endorsement for an injury for which workers' compensation is payable.

Schedule variables: benefits; disablements covered; number of voluntary workers.
