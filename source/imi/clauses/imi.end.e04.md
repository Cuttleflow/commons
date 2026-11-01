---
id: imi.end.e04
type: endorsement
heading: E04 Alternative Strategies
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.imi.exposure.alternatives_share_pct
  - qs.imi.exposure.strategy
  - qs.imi.governance.redemption_suspension_5yr
  rules:
  - when: qs.imi.exposure.alternatives_share_pct >= 30
    action: apply
  - when: qs.imi.exposure.strategy in ('Private credit', 'Property or real assets')
    action: apply
  reason: Applies because {qs.imi.exposure.alternatives_share_pct}% of your funds under management is in alternative or unlisted assets, or your main strategy is {qs.imi.exposure.strategy}.
  responses:
  - Attach
  - Do not attach
---

[[ref:imi.cover.financial-services-liability]] extends to any actual or alleged wrongful act in:

(a) calculating, charging, or recovering a performance fee, including a clawback of a performance fee;

(b) creating, valuing, or operating a side pocket;

(c) imposing a gate on redemptions, or suspending redemptions or applications, in a fund shown in the schedule for this endorsement; and

(d) valuing unlisted assets held by a fund shown in the schedule for this endorsement.

[[ref:imi.excl.fund-performance]] continues to apply, but a claim that alleges a wrongful act of the kind described in (a) to (d) is not a claim that only alleges inadequate performance or return. [[ref:imi.excl.fees-and-commissions]] continues to apply, except that it does not exclude defence costs.

Schedule variables: funds covered; sub-limit (optional).
