---
id: peq.end.e01
type: endorsement
heading: E01 Underground, Tunnelling and Deep Excavation Plant
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.peq.ops.underground
  rules:
  - when: qs.peq.ops.underground == yes
    action: refer
  reason: Referred because plant will work underground, in tunnels or in excavations deeper than 3 metres.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:peq.excl.underground]] does not apply to the items of specified plant named in the schedule for this endorsement, while they work underground, in a tunnel or in an excavation, if:

- the work has a ground support, ventilation and gas monitoring plan prepared by a competent person, as the work health and safety laws that apply require; and
- the plant is fitted with the fire suppression and protective structures that those laws, or the site operator, require for underground work.

We do not pay for loss or damage caused by the collapse of an excavation or tunnel where the ground support in the plan was not in place.

The underground excess shown in the schedule applies to loss or damage that happens underground, in a tunnel or in an excavation, instead of the item's excess, where it is higher. The recovery costs limit in [[ref:peq.ext.recovery-costs]] is increased to the amount shown in the schedule for this endorsement for plant recovered from underground or from a tunnel.

Schedule variables: items covered; underground excess (default 10% of the loss, minimum $10,000); underground recovery costs limit (default $100,000 for any one event).
