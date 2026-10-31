---
id: mot.end.e04
type: endorsement
heading: E04 Increased Tools of Trade
since: 3.0.0
status: draft
trigger:
  questions:
  - qs.mot.cover.tools_of_trade_si
  rules:
  - when: qs.mot.cover.tools_of_trade_si > 5000
    action: apply
  reason: Applies because you asked for tools of trade cover of {qs.mot.cover.tools_of_trade_si}.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

The tools of trade benefit in [[ref:mot.ext.additional-benefits]] is increased to the amount shown in the Schedule for each vehicle. Tools of trade must be kept in a locked vehicle or a locked toolbox fixed to it when unattended; we do not pay for theft from an unattended vehicle without signs of forced entry.

Schedule variables: tools of trade limit for each vehicle.
