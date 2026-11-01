---
id: mcg.end.e04
type: endorsement
heading: E04 Dangerous Goods
since: 1.0.0
changed: 1.1.0
status: draft
trigger:
  questions:
  - qs.mcg.goods.dangerous_goods
  rules:
  - when: qs.mcg.goods.dangerous_goods == yes
    action: refer
  reason: Referred because the goods include dangerous goods; the underwriter confirms the classes and the terms.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The goods include dangerous goods of the classes described in the schedule for this endorsement.

The cover for those goods applies on the condition that they are classified, packed, marked, labelled, documented and carried as the Australian Code for the Transport of Dangerous Goods by Road and Rail requires for inland transits, the International Maritime Dangerous Goods Code requires for transits by sea, and the IATA Dangerous Goods Regulations require for transits by air.

This condition is not a warranty. If you do not meet it, we may refuse only the part of the claim that the failure caused or contributed to, as [[ref:mcg.cond.insurance-contracts-act]] sets out.

We do not cover liability of any kind, including for pollution or contamination, or the cost of clean-up, under this endorsement.

Schedule variables: dangerous goods classes; special excess.
