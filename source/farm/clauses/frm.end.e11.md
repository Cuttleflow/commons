---
id: frm.end.e11
type: endorsement
heading: E11 Bushfire Special Excess
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.location.bushfire_band
  rules:
  - when: qs.frm.location.bushfire_band == EXTREME
    action: refer
  - when: qs.frm.location.bushfire_band == HIGH
    action: apply
  reason: Applies because the farm location has a high bushfire exposure. An extreme exposure is referred to an underwriter.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

The bushfire excess applies to each event of damage or death caused by bushfire, under every section, instead of the section's excess. [[ref:frm.pay.excess]] still applies, so one bushfire event bears one bushfire excess.

Schedule variables: bushfire excess (default: $5,000).
