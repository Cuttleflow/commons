---
id: fs.ii.end.strata-remuneration
type: endorsement
heading: Strata Insurance Remuneration Exclusion
profession: insurance-intermediaries
since: 1.0.0
status: draft
note: ASIC has reviewed remuneration in strata insurance distribution since 2023. This endorsement removes remuneration disputes only; claims for negligent placement remain covered.
trigger:
  questions:
  - qs.fs.ii.strata_gwp_pct
  rules:
  - when: qs.fs.ii.strata_gwp_pct > 20
    action: refer
  reason: Applies because {qs.fs.ii.strata_gwp_pct}% of your premium comes from strata insurance.
---

We do not cover any claim for the repayment or refund of commission, fees or other remuneration that you or a related party received for arranging strata insurance, or any claim alleging that such remuneration was not disclosed or was excessive.
