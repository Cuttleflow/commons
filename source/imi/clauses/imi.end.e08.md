---
id: imi.end.e08
type: endorsement
heading: E08 Extended Reporting Period
since: 1.3.0
changed: 1.4.0
status: draft
trigger:
  questions:
  - qs.imi.cover.extended_reporting_months
  - qs.imi.cover.options_requested
  rules:
  - when: qs.imi.cover.extended_reporting_months != 'None'
    action: refer
  - when: '''E08 Extended Reporting Period'' in qs.imi.cover.options_requested'
    action: refer
  reason: Considered because you asked for a longer period to notify claims after the policy ends.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

The automatic period in [[ref:imi.cond.extended-reporting-period]] is replaced, for [[ref:imi.section.pl]] and [[ref:imi.section.do]], by the extended reporting period shown in the schedule for this endorsement, which must be 12, 24, 36 or 72 months. The period starts at the end of the policy period.

The extended reporting period applies only if this policy is not renewed for any reason other than replacement by another policy that gives equivalent cover, or is cancelled by you or by us, and the non-renewal or cancellation is not caused by non-payment of premium. You must ask for it, and pay the additional premium shown in the schedule, within 30 days of the end of the policy period.

During the extended reporting period we cover claims first made against an insured, and circumstances notified, in that period, but only for wrongful acts committed before the end of the policy period. The limits of liability that applied at the end of the policy period apply, and are not reinstated. The additional premium is fully earned when the endorsement is attached. [[ref:imi.section.crime]] is not affected. It continues to operate under [[ref:imi.cond.extended-discovery-period-crime]] and [[ref:imi.obl.notify-losses-crime]].

Schedule variables: extended reporting period (12, 24, 36 or 72 months); additional premium.
