---
id: isr.end.noav
type: endorsement
heading: NOAV Co-insurance Waived
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.values.missing_valuation
  rules:
  - when: '''NOAV'' in qs.isr.cover.options_requested'
    action: broker_option
  restrictions:
  - when: qs.isr.values.missing_valuation == yes
    action: refer
    note: A Situation has no valuation date, and the waiver depends on recorded valuations.
  reason: Offered because the broker asked for co-insurance to be waived.
---

The co-insurance provisions of the Base Wording and of COIS do not apply to the Material Damage cover at any Situation for which the Schedule shows a valuation date. If the Schedule says so, they also do not apply to the Business Interruption cover. COIS continues to apply at any Situation with no valuation date shown. This endorsement does not increase the Limit of Liability or any sub-limit and does not change the basis of settlement.

Schedule variables: valuation date per Situation; whether the waiver extends to Business Interruption.
