---
id: frm.end.e14
type: endorsement
heading: E14 Northern Australia Cyclone
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.location.north_of_26
  rules:
  - when: qs.frm.location.north_of_26 == yes
    action: refer
  reason: Referred because the farm location is north of the 26th parallel, where the underwriter sets cyclone terms.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

For a farm location north of the 26th parallel of south latitude, damage and death caused by a cyclone, and by storm surge or flood caused by a cyclone, is subject to the cyclone excess instead of the section's excess. We do not pay for damage by a cyclone that is caused during the first 72 hours after this policy is first entered into, if a cyclone watch or warning that includes the farm location was in force when it was, unless this policy replaces, without a break, cover for the same property.

Flood caused by a cyclone is covered only if the schedule shows [[ref:frm.end.e01]].

Schedule variables: cyclone excess (default: $10,000).

[WP REVIEW: confirm whether this policy is an eligible contract for the cyclone reinsurance pool under the Terrorism and Cyclone Insurance Act 2003 (Cth), and the notice that Act requires if it is.]
