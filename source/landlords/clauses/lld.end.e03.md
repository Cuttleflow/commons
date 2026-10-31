---
id: lld.end.e03
type: endorsement
heading: E03 Pet Damage
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.lld.tenancy.pets_permitted
  rules:
  - when: qs.lld.tenancy.pets_permitted == yes
    action: apply
  reason: Applies because the tenancy allows pets.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

[[ref:lld.cover.malicious-tenant-damage]] and [[ref:lld.cover.accidental-tenant-damage]] also cover damage to the building and the contents by an animal kept at the property by a tenant, where the residential tenancy agreement or the tenancy legislation allows the tenant to keep it. The most we pay for damage by animals during one tenancy is the pet damage limit shown in the schedule for this endorsement, within the tenant damage limits.

We do not pay for damage by an animal that is gradual, such as scratching or chewing over a period, or for cleaning, fumigation or odour removal.

Schedule variables: pet damage limit (default $5,000).
