---
id: pi.acct.end.crypto-assets
type: endorsement
heading: Crypto-assets Exclusion
profession: accountants
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.ac.crypto_clients_pct
  rules:
  - when: qs.pi.ac.crypto_clients_pct > 10
    action: suggest
  reason: Applies because {qs.pi.ac.crypto_clients_pct}% of your clients hold crypto-assets.
---

We do not cover any claim, loss or liability arising from the custody, transfer or loss of access to a crypto-asset, or from any advice about the value of a crypto-asset.

This endorsement does not apply to a claim arising from your preparation of a tax return or financial statements that record crypto-assets.
