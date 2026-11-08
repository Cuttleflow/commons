---
id: fsl.end.e01
type: endorsement
heading: E01 Scheduled Customer Contracts
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.fsl.operations.onerous_contracts
  rules:
  - when: qs.fsl.operations.onerous_contracts == true
    action: refer
  reason: Referred because you have signed customer contracts that accept more liability than your standard trading conditions.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

For each customer contract named in the schedule for this endorsement, [[ref:fsl.pay.trading-conditions]] measures your liability under that contract instead of under your standard trading conditions, and [[ref:fsl.excl.contractual-liability]] does not apply to it.

If the schedule shows a contract sub-limit, the part of your liability under the contract that is greater than your liability under your standard trading conditions is covered only up to that sub-limit, for any one occurrence or claim. The sub-limit is part of the limit of the section concerned.

This endorsement does not cover:

- an agreed or liquidated damages amount, or a service credit, unless the schedule says so;
- loss of profit or loss of market beyond what your standard trading conditions allow, unless the schedule says so; or
- liability under a contract that has been changed after we named it, unless we agree in writing to the change.

Schedule variables: each contract (customer, contract title and date); contract sub-limit; any special excess.
