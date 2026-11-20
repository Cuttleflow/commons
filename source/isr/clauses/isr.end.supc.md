---
id: isr.end.supc
type: endorsement
heading: SUPC Suppliers and Customers
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.bi.named_dependency_overseas
  rules:
  - when: '''SUPC'' in qs.isr.cover.options_requested'
    action: broker_option
  restrictions:
  - when: qs.isr.bi.named_dependency_overseas == yes
    action: refer
    note: A named supplier or customer is outside Australia and cannot be assessed from the Situation data.
  reason: Offered as an option for named suppliers and customers.
---

We cover Business Interruption loss resulting from Damage, of a kind this Policy would cover, at the premises of:

- the suppliers and customers named in the Schedule, up to the named sub-limit and within the territory shown for each; and
- your other direct suppliers and customers in Australia, up to the unnamed sub-limit.

Unnamed suppliers and customers means those you deal with directly, not their own suppliers or customers. We do not cover loss arising from a supplier's or customer's insolvency, industrial action or decision to stop dealing with you, or from a cyber event or communicable disease.

Schedule variables: named suppliers and customers, with territory; named sub-limit; unnamed sub-limit; waiting period.
