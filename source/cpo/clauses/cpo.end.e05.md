---
id: cpo.end.e05
type: endorsement
heading: E05 Higher-Hazard Tenancy
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.cpo.tenancy.cooking_deep_frying
  - qs.cpo.tenancy.spray_painting
  - qs.cpo.tenancy.hot_work
  - qs.cpo.tenancy.flammable_storage
  - qs.cpo.tenancy.late_licensed
  rules:
  - when: qs.cpo.tenancy.cooking_deep_frying == yes
    action: refer
  - when: qs.cpo.tenancy.spray_painting == yes
    action: refer
  - when: qs.cpo.tenancy.hot_work == yes
    action: refer
  - when: qs.cpo.tenancy.flammable_storage == yes
    action: refer
  - when: qs.cpo.tenancy.late_licensed == yes
    action: refer
  reason: A tenancy is used for a higher-hazard activity.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The tenancy described in the schedule for this endorsement is used for the higher-hazard activity shown. Cover continues on these conditions, which apply to that tenancy only:

- commercial cooking equipment with deep fryers must have an automatic fire suppression system over the cooking surfaces, and the exhaust hoods, filters and ducts must be cleaned by a professional cleaner at least every 6 months, or as the schedule shows;
- spray painting must be done only in a spray booth that complies with AS/NZS 4114;
- hot work must be done under a written hot work permit system;
- flammable liquids and gases must be stored as the relevant Australian Standard requires.

If you can show that a breach of a condition did not cause or contribute to the damage, we pay the claim as if the condition had been met. Otherwise, [[ref:cpo.cond.insurance-contracts-act]] applies. The special excess shown applies to damage that starts in that tenancy.

Schedule variables: tenancy and activity; cleaning interval (default: 6 months); special excess (default: the basic excess).
