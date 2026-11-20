---
id: pa.lol.end.e17
type: endorsement
heading: E17 Cabin Crew Fitness to Fly
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pa.lol.licence_type
  rules:
  - when: qs.pa.lol.licence_type == cabin_crew
    action: refer
  reason: Referred because cabin crew fitness to fly cover needs an underwriter's terms.
  responses:
  - Attach
  - Attach with premium loading
  - Decline risk
---

This policy applies to the cabin crew member named in the schedule as if they held a licence. Permanent loss of licence and temporary loss of licence mean a decision by their employer's aviation medical adviser, because of an injury or sickness, that they are permanently, or for the time being, not fit to work as cabin crew under the employer's fitness to fly standard shown in the schedule.

Schedule variables: employer; fitness to fly standard; capital sum and monthly benefit.
