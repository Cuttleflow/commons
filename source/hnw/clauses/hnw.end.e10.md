---
id: hnw.end.e10
type: endorsement
heading: E10 Vault Storage
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.hnw.valuables.jewellery_vault_sum_insured
  rules:
  - when: qs.hnw.valuables.jewellery_vault_sum_insured > 0
    action: apply
  reason: Applies because jewellery and watches in a vault are insured.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

Jewellery and watches in a vault are covered while in the vault named in the schedule for this endorsement. They are also covered anywhere in the world while out of the vault for up to the number of days in each policy period shown in the schedule for this endorsement. Outside those days, an item out of the vault is covered as jewellery and watches only if that category is insured, and within its category sum insured.

Schedule variables: name and address of the vault; days out of the vault (default 30).
