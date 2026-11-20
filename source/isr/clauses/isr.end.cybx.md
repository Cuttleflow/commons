---
id: isr.end.cybx
type: endorsement
heading: CYBX Cyber Exclusion and Physical Damage Write-back
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.policy.base_wording
  - qs.isr.binder.lloyds
  rules:
  - when: qs.isr.binder.lloyds == yes
    action: apply
  - when: qs.isr.policy.base_wording != 'meridian'
    action: apply
  reason: Applies because the capacity provider requires cyber to be dealt with expressly.
---

In this endorsement:

- a **computer system** is any computer, device, network, software, cloud service, industrial or process control system, and the data stored in or processed by any of them, whether owned by you or anyone else; and
- a **cyber event** is an unauthorised, malicious or criminal act involving a computer system, or an error, omission, failure or malfunction of a computer system.

We do not pay for loss of, damage to, or loss of use or function of data or software, however caused, except as DATA provides. We do not pay for Damage or Business Interruption loss caused by a cyber event, except as set out in the option shown in the Schedule:

- **Option A — fire and explosion.** Damage by fire or explosion that results from a cyber event is covered, and so is Business Interruption loss resulting from that Damage.
- **Option B — physical damage.** Physical Damage to property other than data or software that results from a cyber event is covered, and so is Business Interruption loss resulting from that Damage.

Schedule variables: Option A or Option B.
