---
id: cy.end.e06
type: endorsement
heading: E06 Digital Asset Theft
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.cy.insured.holds_crypto
  rules:
  - when: qs.cy.insured.holds_crypto == yes
    action: refer
  reason: Considered because you hold cryptocurrency or other digital assets.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Do not attach
---

For [[ref:cy.cover.funds-transfer-fraud]], funds include cryptocurrency and other digital assets owned by you and held in wallets under your control, and a fraudulent transfer includes the theft of those assets by a third party who gains **unauthorised** access to your computer system or wallet.

We will pay the lesser of the market value of the stolen assets at the time of discovery and their market value at the time of the theft, determined by reference to a reputable exchange.

You must: (a) hold the private keys for holdings above the hot-wallet threshold shown in the schedule in cold storage; and (b) protect all wallet access with multi-factor authentication. If you do not, we may reduce our liability to the extent that the failure caused or contributed to the loss or prejudiced us, as s.54 of the Insurance Contracts Act 1984 (Cth) allows.

This endorsement does not cover assets you hold on trust for, or on behalf of, any third party, or any fall in the market value of assets that are not stolen.

Schedule variables: sub-limit; hot-wallet threshold.
