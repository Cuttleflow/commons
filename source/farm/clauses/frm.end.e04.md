---
id: frm.end.e04
type: endorsement
heading: E04 Horse Riding and Equestrian Activities
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.frm.ops.horse_riding_visitors
  rules:
  - when: qs.frm.ops.horse_riding_visitors == yes
    action: refer
  reason: Referred because visitors ride horses at the farm, which the underwriter assesses before cover is given.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:frm.li.excl-guests]] does not apply to liability arising from horse riding by visitors at the farm location under your supervision, or from the equestrian events named in the schedule that you organise there.

Riding must be supervised by a person who holds a recognised qualification for instructing or guiding riders. Each rider must wear an approved helmet, and each rider or their parent or guardian must sign an acknowledgement of the risks of riding before riding. The most we pay for all claims arising from riding and equestrian events in the policy period is the riding sub-limit, which is part of, and not in addition to, the liability limit.

Schedule variables: riding sub-limit (default: $10,000,000); equestrian events (default: none).
