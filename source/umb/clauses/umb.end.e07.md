---
id: umb.end.e07
type: endorsement
heading: E07 Excess of Underlying Sub-limits
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.umb.underlying.sublimits_extension_requested
  rules:
  - when: qs.umb.underlying.sublimits_extension_requested == true
    action: refer
  reason: Referred because you asked for this policy to sit above sub-limits in your underlying insurance.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

For each sub-limit of the underlying insurance shown in the schedule for this endorsement, [[ref:umb.cover.coverage-a]] applies above that sub-limit, as if it were the underlying limit for that liability, up to the sub-limit shown for it in the schedule for this endorsement, which is part of and not in addition to the limit of liability.

Schedule variables: each underlying sub-limit; the sub-limit of this policy above it.
