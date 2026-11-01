---
id: gpa.end.e03
type: endorsement
heading: E03 Sports Teams
since: 1.0.0
changed: 1.1.0
status: draft
trigger:
  questions:
  - qs.gpa.pertype.players
  rules:
  - when: qs.gpa.pertype.players > 0
    action: apply
  reason: Applied because the policyholder covers {qs.gpa.pertype.players} registered players and officials.
  responses:
  - Attach
  - Do not attach
---

The category named in the schedule for this endorsement covers registered players, coaches, umpires and officials of the policyholder. For them:

- the scope of cover is while taking part in, training for, or officiating at an activity organised by the policyholder, and while travelling directly to and from it;
- weekly sickness benefits do not apply;
- the weekly benefit is the lower of the amount shown for this endorsement and 85% of income, after a waiting period of 14 days unless the schedule shows otherwise, for up to 52 weeks;
- the capital sum for a player under 18 is the reduced amount shown for this endorsement; and
- [[ref:gpa.excl.professional-sport]] applies to anyone who is paid more than 15% of their income, or more than $10,000 a year, from sport.

The premium for this category is a rate per registered player or official.

Schedule variables: the sport; number of registered participants (or the declaration basis); capital sum; weekly benefit; reduced capital sum for those under 18 (default 20% of the capital sum).
