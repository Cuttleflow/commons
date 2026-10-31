---
id: mot.end.e12
type: endorsement
heading: E12 Dangerous Goods Transport
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.use.dangerous_goods
  rules:
  - when: qs.mot.use.dangerous_goods == true
    action: refer
  reason: Referred because you told us vehicles carry Dangerous goods.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Decline risk
---

The Dangerous goods sub-limit in [[ref:mot.ext.dangerous-goods]] is increased to the amount shown in the Schedule. You must comply with the law that applies to the carriage of the classes of Dangerous goods shown, including placarding, driver licensing and vehicle approval, and we cover the reasonable cost of clean-up and removal of Dangerous goods spilled from an Insured vehicle that a public authority requires, within that sub-limit.

Schedule variables: Dangerous goods sub-limit; classes carried.
