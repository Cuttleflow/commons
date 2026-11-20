---
id: ccl.end.e04
type: endorsement
heading: E04 Dangerous Goods
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.ccl.operations.dangerous_goods
  rules:
  - when: qs.ccl.operations.dangerous_goods == true
    action: refer
  reason: Applies because you carry dangerous goods in packages.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

You carry the dangerous goods in packages shown in the schedule. You must carry them as the Australian Code for the Transport of Dangerous Goods by Road and Rail requires, with drivers who hold any licence it requires. Bulk dangerous goods remain excluded goods. [[ref:ccl.cond.insurance-contracts-act]] applies to these conditions.

Schedule variables: the classes and quantities of dangerous goods carried.
