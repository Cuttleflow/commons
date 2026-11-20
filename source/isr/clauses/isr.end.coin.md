---
id: isr.end.coin
type: endorsement
heading: 'COIN Coinsurance: Several Liability and Participations'
since: 1.1.0
status: draft
trigger:
  questions:
  - qs.isr.placement.participant_count
  rules:
  - when: qs.isr.placement.participant_count > 1
    action: apply
  reason: Applies because more than one insurer subscribes to the policy.
---

- This Policy is subscribed by the insurers named in the Schedule, each for the share shown against its name. Each insurer is liable only for its own share. No insurer is liable for the share of another insurer, including one that does not pay.
- Each insurer's share applies to the Limit of Liability, every sub-limit, the premium and every claim payment.
- Where the Schedule shows a signed share that differs from the written share, the signed share applies.
- The Schedule and other documents may be issued by the leading insurer or the broker for all insurers.
- Where the Schedule notes a term that applies only to one insurer, it applies only to that insurer's share.

Schedule variables: insurers; written and signed shares; insurer-specific terms.
