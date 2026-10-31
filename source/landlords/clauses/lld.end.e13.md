---
id: lld.end.e13
type: endorsement
heading: E13 Self-Managed Property
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.lld.tenancy.management
  rules:
  - when: qs.lld.tenancy.management == self
    action: apply
  reason: Applies because the property is self-managed.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

You manage the property yourself, without a property manager. For [[ref:lld.cover.tenant-default]], [[ref:lld.cover.death-of-tenant]] and [[ref:lld.section.tenant-damage]]:

- the tenant default excess is the amount shown in the schedule for this endorsement;
- with your claim, you must give us the records that show the checks in [[ref:lld.cond.tenant-selection]] were made, the condition reports and inspection records in [[ref:lld.obl.inspections]], the rent ledger, and copies of the notices you gave.

Schedule variables: tenant default excess (default two weeks' rent).
