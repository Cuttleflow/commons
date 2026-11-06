---
id: peq.end.e12
type: endorsement
heading: E12 Remote and Autonomous Plant
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.peq.plant.autonomous
  rules:
  - when: qs.peq.plant.autonomous == yes
    action: refer
  reason: Referred because insured plant is operated remotely or autonomously.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

This endorsement applies to the items of specified plant named in the schedule for it that are operated by remote control, or by a guidance or autonomy system.

**Technology failure.** We pay for accidental loss or damage to a named item caused by the failure of its remote control, guidance, positioning or autonomy system, including loss of a satellite positioning or communications signal, or a software fault. [[ref:peq.excl.breakdown]] and [[ref:peq.excl.cyber]] do not apply to that loss or damage, except where it is caused by a deliberate and malicious cyber event.

**Operating conditions.** A named item must run only software and firmware approved by its manufacturer, within a geofenced work area where the system provides one, and under the supervision of a person able to stop it.

We do not pay for the cost of repairing or replacing the remote control, guidance or autonomy system itself, unless it is damaged by accidental loss or damage covered by [[ref:peq.cover.material-damage|heading]].

Schedule variables: items covered; technology failure excess (default twice the item's excess).
