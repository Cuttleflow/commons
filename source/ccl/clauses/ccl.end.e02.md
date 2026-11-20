---
id: ccl.end.e02
type: endorsement
heading: E02 Refrigerated Goods
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.ccl.operations.refrigerated_goods
  rules:
  - when: qs.ccl.operations.refrigerated_goods == true
    action: apply
  reason: Applies because you carry refrigerated goods.
---

For refrigerated goods:

- you must pre-cool the load space before loading, and record the temperature of the goods at loading;
- the refrigeration unit must be fitted with a temperature recorder or remote monitoring, and its records kept for the policy period; and
- the special excess shown in the schedule applies to each claim for deterioration.

[[ref:ccl.cond.insurance-contracts-act]] applies to these conditions.

Schedule variables: special excess for deterioration (default $2,500).
