---
id: ppl.end.e07
type: endorsement
heading: E07 Licensed Venues
since: 2.0.0
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

[[ref:ppl.excl.licensed-venues]] does not apply to the licensed venues shown in the schedule for this endorsement, if at the time of the occurrence:

- the venue held a current liquor licence and was trading within its licensed hours and conditions; and
- your staff serving liquor held current responsible service of alcohol accreditation required by the law of the state or territory.

These licence conditions are part of this endorsement and are not variables. If the schedule shows a sub-limit or special excess for this endorsement, it applies.

Schedule variables: venues and licence numbers; sub-limit (optional); special excess (optional).
