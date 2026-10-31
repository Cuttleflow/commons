---
id: bpk.end.e05
type: endorsement
heading: E05 Increased Tenants' Liability
since: 2.1.0
status: draft
trigger:
  questions:
  - qs.bpk.liability.lease_tenants_liability_required
  rules:
  - when: qs.bpk.liability.lease_tenants_liability_required > 2000000
    action: refer
  - when: qs.bpk.liability.lease_tenants_liability_required > 500000
    action: suggest
  reason: Considered because your lease requires tenants' liability cover of ${qs.bpk.liability.lease_tenants_liability_required}.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

The tenants' liability sub-limit in [[ref:bpk.liability.additional-benefits]] is increased to the amount shown in the Schedule.

Schedule variables: tenants' liability sub-limit.
