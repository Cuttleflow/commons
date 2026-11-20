---
id: chl.end.e12
type: endorsement
heading: E12 Queensland Marine Pollution and Wreck Removal
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.chl.vessel.state
  - qs.chl.vessel.length
  rules:
  - when: qs.chl.vessel.state == QLD and qs.chl.vessel.length > 15
    action: apply
  reason: Applies because the vessel is more than 15 metres long and based in Queensland.
---

For a vessel to which s.67A of the Transport Operations (Marine Pollution) Act 1995 (Qld) applies:

- the pollution sub-limit in [[ref:chl.cover.pi-limits]] is not less than the amount that section and its regulations require for pollution, whatever the schedule shows;
- the protection and indemnity limit for wreck removal and salvage under paragraph (d) of [[ref:chl.cover.pi]] is not less than the amount they require; and
- we issue a certificate of insurance for the vessel to carry on board.

This endorsement applies only while [[ref:chl.section.pi|heading]] applies.

[WP REVIEW: confirm the amounts s.67A and the regulations require, and the lengths of vessel to which they apply, before each release.]
