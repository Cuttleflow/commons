---
id: lld.end.e04
type: endorsement
heading: E04 Short-Stay Letting
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.lld.tenancy.agreement_type
  rules:
  - when: qs.lld.tenancy.agreement_type == short_stay
    action: refer
  reason: Referred because the property is let for short stays.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:lld.excl.short-stay-letting]] does not apply. While the property is used for short-stay letting:

- a guest is treated as a tenant, and their stay as a tenancy, for the Tenant Damage section, with the short-stay damage limit shown in the schedule for this endorsement;
- [[ref:lld.cover.tenant-default]] and [[ref:lld.cover.death-of-tenant]] do not apply;
- [[ref:lld.cover.rent-after-damage]] pays the average nightly booking income for the same months in the previous year, or the confirmed bookings you lose if the property was not let then, for up to 12 weeks.

Schedule variables: short-stay damage limit (default $20,000); special excess (default the tenant damage excess).
