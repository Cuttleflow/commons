---
id: lld.end.e06
type: endorsement
heading: E06 Specialist Disability or Supported Accommodation
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.lld.tenancy.tenancy_type
  rules:
  - when: qs.lld.tenancy.tenancy_type == supported
    action: refer
  reason: Referred because the property is specialist disability or supported accommodation.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

The property may be let as specialist disability accommodation or supported independent living accommodation, with the occupants' tenancies arranged under a residential tenancy agreement or a supported accommodation agreement under the law of the state or territory. Each occupant is treated as a tenant, and their agreement as a residential tenancy agreement.

Damage caused by an occupant because of their disability is covered under [[ref:lld.cover.accidental-tenant-damage]] and not [[ref:lld.cover.malicious-tenant-damage]].

Schedule variables: provider name; special excess (default the tenant damage excess).
