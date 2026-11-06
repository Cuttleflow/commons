---
id: env.end.e01
type: endorsement
heading: E01 Pre-existing Conditions
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.env.site.pre_existing_requested
  rules:
  - when: qs.env.site.pre_existing_requested == true
    action: refer
  reason: Referred because you asked for cover for pollution that began at your site before the retroactive date.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

[[ref:env.cover.site-pollution-legal-liability]] also covers pollution conditions at the covered locations shown in the schedule for this endorsement that began before the retroactive date, as long as no member of your control group knew of them before the start of the policy period, other than conditions disclosed to us in writing and accepted in the schedule. The most we will pay under this endorsement is the sub-limit shown in the schedule for it, which is part of and not in addition to the limit of liability.

Schedule variables: the covered locations; the sub-limit; any disclosed conditions accepted.
