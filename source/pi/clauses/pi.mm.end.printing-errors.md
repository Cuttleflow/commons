---
id: pi.mm.end.printing-errors
type: endorsement
heading: Printing Errors
profession: marketing-media
since: 1.0.0
status: draft
note: Adds cover.
trigger:
  questions:
  - qs.pi.mm.printing
  - qs.pi.mm.proof_signoff
  rules:
  - when: qs.pi.mm.printing = yes and qs.pi.mm.proof_signoff = yes
    action: broker_option
  reason: Offered because you arrange printing with client-signed proofs.
---

We cover you for the cost of reprinting, or of compensating a client for, printed material that contains an error you introduced after the client signed off the final proof.

The most we will pay for all claims under this endorsement is the sub-limit shown in the schedule for this endorsement, which is part of the limit of liability.
