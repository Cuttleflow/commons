---
id: pi.gm.end.public-report-excess
type: endorsement
heading: Public Report Excess
profession: geoscience-mineral
since: 1.0.0
status: draft
note: Replaces the deductible in MERIDIAN-PI-GEOL-v1.0.0, which was the lesser of 0.25% or $10,000 with a maximum of $250,000. A lesser-of excess can never exceed $10,000, so the maximum had no effect.
  Counsel to confirm the base for the percentage.
trigger:
  questions:
  - qs.pi.gm.public_report_pct
  rules:
  - when: qs.pi.gm.public_report_pct > 0
    action: apply
  reason: Applies because you sign or contribute to public reports about mineral assets.
  responses:
  - Attach
  - Attach with special excess
  - Do not attach
---

For each claim arising from a public report, the excess is the amount shown in the schedule for this endorsement. If no amount is shown, the excess is the greater of $10,000 and 0.25% of the amount raised in, or the value of the transaction connected with, the capital raising or transaction for which the public report was prepared, but not more than $250,000.
