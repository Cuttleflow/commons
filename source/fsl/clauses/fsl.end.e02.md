---
id: fsl.end.e02
type: endorsement
heading: E02 Special Cargo Conditions
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.fsl.operations.special_cargo_pct
  rules:
  - when: qs.fsl.operations.special_cargo_pct > 25
    action: refer
  - when: qs.fsl.operations.special_cargo_pct > 10
    action: apply
  reason: Applies because {qs.fsl.operations.special_cargo_pct}% of your gross receipts come from dangerous, temperature-controlled or high-value goods.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
---

In this endorsement, special cargo means:

- dangerous goods, as classified under the International Maritime Dangerous Goods Code, the IATA Dangerous Goods Regulations or the Australian Code for the Transport of Dangerous Goods by Road and Rail;
- goods that must be kept within a stated temperature range; and
- high-value goods, meaning computers, mobile phones and other portable electronic devices, pharmaceuticals, tobacco products and alcoholic beverages, and any consignment of other goods valued above $250,000 or the amount shown in the schedule for this endorsement.

For special cargo, [[ref:fsl.cover.cargo-liability|heading]] does not cover physical loss of or damage to goods, or delay in delivering them, caused by your failure, where it was your responsibility under the contract:

- to follow the customer's written instructions for handling, packing, storage and carriage;
- for dangerous goods, to comply with the code that applies to their carriage, including declaration, packing, marking, labelling and segregation;
- for temperature-controlled goods, to set, monitor and record the temperature as instructed, and to keep the record for each consignment; or
- for high-value goods, to keep them in locked premises, vehicles or containers whenever they are not being loaded, unloaded or moved.

This endorsement does not apply to a loss that the failure did not cause or contribute to.

Schedule variables: high-value consignment threshold (default $250,000, as shown in the schedule); any special excess.
