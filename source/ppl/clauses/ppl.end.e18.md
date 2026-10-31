---
id: ppl.end.e18
type: endorsement
heading: E18 New Zealand Exemplary Damages
since: 2.0.0
status: draft
trigger:
  questions:
  - qs.ppl.exposure.nz_turnover_pct
  - qs.ppl.products.nz_pct
  rules:
  - when: qs.ppl.exposure.nz_turnover_pct > 0 or qs.ppl.products.nz_pct > 0
    action: apply
  reason: Applies because you work or sell in New Zealand.
  responses:
  - Attach
  - Attach with amended sub-limit
---

[[ref:ppl.excl.fines-and-penalties]] does not apply to exemplary or punitive damages awarded in New Zealand for personal injury that is covered by the Accident Compensation Act 2001 (NZ), where you are liable for them and they arise from an occurrence covered by this policy. We do not pay exemplary damages to the extent they are uninsurable by law, or where the conduct giving rise to them was deliberate or reckless conduct by a director or officer of the named insured. The most we will pay for all such damages in the policy period, including defence costs, is the aggregate sub-limit shown for this endorsement.

Schedule variables: aggregate sub-limit (NZD or AUD).
