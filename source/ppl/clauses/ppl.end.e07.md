---
id: ppl.end.e07
type: endorsement
heading: E07 Licensed Venues
since: 2.0.0
changed: 2.1.0
status: draft
trigger:
  questions:
  - qs.ppl.ops.liquor_supplied
  - qs.ppl.ops.trading_after_midnight
  rules:
  - when: qs.ppl.ops.liquor_supplied == licensed_venue and qs.ppl.ops.trading_after_midnight == yes
    action: refer
  - when: qs.ppl.ops.liquor_supplied == licensed_venue
    action: apply
  reason: Applies because you sell or supply alcohol at a licensed venue.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Decline risk
---

[[ref:ppl.excl.licensed-venues]] does not apply to the licensed venues shown in the schedule for this endorsement.

For each venue you must make sure that:

- the venue holds a current liquor licence and trades within its licensed hours and conditions; and
- your staff serving liquor hold current responsible service of alcohol accreditation required by the law of the state or territory.

If you do not, we may reduce our liability for an occurrence arising from the sale or supply of liquor at the venue to the extent that the failure caused or contributed to the loss, as s.54 of the Insurance Contracts Act 1984 (Cth) allows.

These licence conditions are part of this endorsement and are not variables. If the schedule shows a sub-limit or special excess for this endorsement, it applies.

Schedule variables: venues and licence numbers; sub-limit (optional); special excess (optional).
