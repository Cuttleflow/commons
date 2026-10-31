---
id: gpa.end.e01
type: endorsement
heading: E01 Voluntary Workers
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.gpa.pertype.volunteers
  rules:
  - when: qs.gpa.pertype.volunteers > 0
    action: apply
  reason: Applied because the policyholder covers {qs.gpa.pertype.volunteers} voluntary workers.
  responses:
  - Attach
  - Do not attach
---

The category named in the schedule for this endorsement covers voluntary workers: people doing unpaid work authorised and controlled by the policyholder. For them:

- the scope of cover is occupational: while doing that work, and while travelling directly to and from it;
- weekly sickness benefits do not apply;
- a voluntary worker who earns an income receives weekly benefits as [[ref:gpa.pay.weekly-benefit-amount]] says, up to the weekly benefit shown for this endorsement;
- a voluntary worker who does not earn an income and cannot carry out their usual domestic duties because of an injury receives 80% of the reasonable cost of domestic help, up to the weekly amount shown for this endorsement, for up to 26 weeks, after the waiting period; and
- the capital sum for a voluntary worker under 18 or aged 80 or over is the reduced amount shown for this endorsement.

The premium for this category is a rate per voluntary worker.

Schedule variables: number of voluntary workers (or the declaration basis); capital sum; weekly benefit for income earners; domestic help weekly amount (default $500); reduced capital sum for those under 18 and 80 or over (default 25% of the capital sum).
