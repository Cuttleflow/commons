---
id: pi.rl.end.on-hired-workers
type: endorsement
heading: On-hired Workers
profession: recruitment-labour-hire
since: 1.0.0
changed: 1.1.0
status: draft
note: Adds cover. Rebuilt from the June optional extension OPT-ONHIRE, which was descriptive only.
trigger:
  questions:
  - qs.pi.rl.onhire_pct
  - qs.pi.rl.written_onhire_agreements
  rules:
  - when: qs.pi.rl.onhire_pct > 0 and qs.pi.rl.written_onhire_agreements = yes
    action: broker_option
  - when: qs.pi.rl.onhire_pct > 0 and qs.pi.rl.written_onhire_agreements = no
    action: refer
  reason: Offered because you supply workers to hosts under written on-hire agreements.
---

We will not apply [[ref:pi.rl.excl.on-hired-work]] where the worker was supplied under a written agreement with the host that places the supervision and direction of the worker's day-to-day work with the host. For a claim arising from that work, we cover your liability to the host or a third party for the worker's acts, errors or omissions in performing professional or technical work, except to the extent the host's own supervision caused or contributed to the loss.

For all claims under this endorsement, the most we will pay in total, including defence costs, is the sub-limit shown in the schedule for this endorsement, or 25% of the limit of liability if no sub-limit is shown. The sub-limit is part of, and not in addition to, the limit of liability.

This endorsement does not affect [[ref:pi.excl.bodily-injury-and-property-damage]] or [[ref:pi.excl.employers-liability]].
