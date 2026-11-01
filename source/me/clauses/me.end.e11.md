---
id: me.end.e11
type: endorsement
heading: E11 Excess Layer
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.me.cover.excess_layer
  rules:
  - when: qs.me.cover.excess_layer == yes
    action: refer
  reason: Referred because this cover sits above underlying insurance.
---

This wording applies in excess of the underlying insurance stated in the schedule, and follows its terms only as the schedule states. Our liability attaches only after the underlying limits have been exhausted by payment of covered claims.

Schedule variables: underlying insurer, policy and limit.
