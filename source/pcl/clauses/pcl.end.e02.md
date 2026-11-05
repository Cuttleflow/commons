---
id: pcl.end.e02
type: endorsement
heading: E02 Vault Storage
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pcl.collection.vault_storage
  rules:
  - when: qs.pcl.collection.vault_storage == yes
    action: apply
  reason: Applies because jewellery or watches are kept in a vault.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

Jewellery and watches in a vault are covered while they are in the vault named in the schedule.

They are also covered anywhere in the world while they are out of the vault, for up to the number of consecutive days shown in the schedule for this endorsement on each occasion. While they are out of the vault, the premium is based on them being kept in the vault. If they are to be out of the vault for longer, tell us before the time ends: we may charge an additional premium to continue cover.

Schedule variables: vault name and address; days out of the vault on each occasion (default 30).
