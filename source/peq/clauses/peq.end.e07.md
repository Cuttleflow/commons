---
id: peq.end.e07
type: endorsement
heading: 'E07 Road Risk: Registered Mobile Plant'
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.peq.plant.registered_count
  rules:
  - when: qs.peq.plant.registered_count > 0
    action: suggest
  reason: Suggested because {qs.peq.plant.registered_count} item(s) of insured plant are registered for road use.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

This endorsement applies to the items of registered plant named in the schedule for it, and only if [[ref:peq.section.liability|heading]] applies.

[[ref:peq.excl.liability-road-use]] does not apply to property damage caused while a named item is driven on a public road between the named insured's premises and a work site, or between work sites. The most we pay for any one occurrence under this endorsement is the road risk limit shown in the schedule, which is part of the limit for [[ref:peq.section.liability|heading]].

[[ref:peq.excl.liability-workers]] still applies. Where a commercial motor policy also covers the same liability, [[ref:peq.pay.other-insurance]] applies. This endorsement is the companion to endorsement E11 of the Meridian Commercial Motor wording (2026/CMV/0001).

Schedule variables: registered items covered; road risk limit (default $20,000,000 for any one occurrence).
