---
id: do.end.e06
type: endorsement
heading: E06 Extended Discovery Period
since: 1.3.0
changed: 1.4.0
status: draft
trigger:
  questions:
  - qs.do.cover.options_requested
  rules:
  - when: "'E06' in qs.do.cover.options_requested"
    action: broker_option
  reason: Offered because you asked for a longer discovery period after the policy ends.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

The discovery period under [[ref:do.cond.discovery-period]] is extended to the period shown in the schedule (12, 24, 36, 72 or 84 months, or lifetime) after the end of the policy period.

During the extended discovery period, claims first made against an insured for wrongful acts that occurred during or before the policy period are covered, subject to all other terms, conditions, exclusions, and limits of this policy.

The extended discovery period is not cancellable by us once purchased. Additional premium: as shown in the schedule.

Schedule variables: Extended discovery period (12, 24, 36, 72 or 84 months, or lifetime); additional premium.
