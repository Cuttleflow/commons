---
id: isr.end.secu
type: endorsement
heading: SECU Security and Intruder Alarm
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.cover.options_requested
  - qs.isr.cover.theft_sublimit_over_threshold
  rules:
  - when: '''THFT'' in qs.isr.cover.options_requested and qs.isr.cover.theft_sublimit_over_threshold == yes'
    action: apply
  reason: Applies because full theft cover is taken with a theft sub-limit above the agency's threshold.
---

Where the Schedule shows that a Situation has a monitored intruder alarm or other security protection:

- keep it in working order and set it whenever the Situation is closed;
- keep the monitoring contract in force; and
- tell us if it will be out of action for longer than the period shown in the Schedule.

This condition applies only to claims for theft and malicious damage.

Schedule variables: protected Situations and protections; out-of-action period (default 72 hours).
