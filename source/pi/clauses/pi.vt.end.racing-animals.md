---
id: pi.vt.end.racing-animals
type: endorsement
heading: Racing Animals Excess
profession: veterinary
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.vt.racing_pct
  rules:
  - when: qs.pi.vt.racing_pct > 10
    action: apply
  reason: Applies because {qs.pi.vt.racing_pct}% of your work is with racing animals.
  responses:
  - Attach
  - Attach with special excess
  - Do not attach
---

For a claim arising from services to a thoroughbred, standardbred or greyhound in training or racing, or bred for racing, the excess is the amount shown in the schedule for this endorsement.
