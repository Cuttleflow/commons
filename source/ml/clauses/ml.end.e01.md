---
id: ml.end.e01
type: endorsement
heading: E01 Extended Reporting and Discovery Period
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.ml.cover.options_requested
  rules:
  - when: '''E01'' in qs.ml.cover.options_requested'
    action: broker_option
  reason: Offered because you asked for a longer period to notify claims and discover crime losses after the policy ends.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

The Extended Reporting Period under [[ref:ml.cond.extended-reporting-period]] and the Extended Discovery Period under [[ref:ml.cond.extended-discovery-period]] are each extended to the number of months shown in the schedule for this endorsement, which must be 12, 24 or 36 months. The period starts at the end of the policy period and replaces the automatic period in those conditions.

This endorsement does not extend the policy period, cover any wrongful act or dishonest act that first occurs after the end of the policy period, or reinstate any limit of liability. All claims and Crime Losses notified during the extended period are subject to the limits of liability that applied at the end of the policy period.

The additional premium shown in the schedule for this endorsement is fully earned when the endorsement is attached. You may not cancel the endorsement once the extended period has started.

Schedule variables: period (12, 24 or 36 months); additional premium.
