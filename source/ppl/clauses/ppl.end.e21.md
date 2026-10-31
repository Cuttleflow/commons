---
id: ppl.end.e21
type: endorsement
heading: E21 Worker-to-worker Excess
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.exposure.subcontractor_pct
  - qs.ppl.exposure.labour_hire_pct
  rules:
  - when: qs.ppl.exposure.subcontractor_pct > 50 or qs.ppl.exposure.labour_hire_pct > 50
    action: refer
  - when: qs.ppl.exposure.subcontractor_pct > 25 or qs.ppl.exposure.labour_hire_pct > 25
    action: suggest
  reason: Considered because subcontractors or labour hire workers do a large part of your work.
  responses:
  - Attach with special excess
  - Do not attach
---

The excess for each worker-to-worker claim is the worker-to-worker excess shown in the schedule for this endorsement, instead of the standard excess. It applies to compensation and defence costs.

Schedule variables: worker-to-worker excess.
