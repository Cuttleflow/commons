---
id: fsl.end.e03
type: endorsement
heading: E03 Warehouse Security Conditions
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.fsl.operations.warehouse
  rules:
  - when: qs.fsl.operations.warehouse == true
    action: apply
  reason: Applies because you store goods for customers in a warehouse or depot you operate.
  responses:
  - Attach
  - Do not attach
---

For goods in a warehouse or depot you operate, [[ref:fsl.cover.cargo-liability|heading]] does not cover theft, or loss or damage by fire, unless at the time of the loss:

- the premises had an intruder alarm monitored by a security company, which was set whenever the premises were closed; and
- the fire detection, sprinklers and other fire protection installed in the premises were maintained and serviced as the law requires.

This endorsement does not apply to a loss that the failure did not cause or contribute to.

Schedule variables: the warehouses and depots it applies to; any agreed exception.
