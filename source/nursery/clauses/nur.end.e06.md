---
id: nur.end.e06
type: endorsement
heading: E06 Potting Mix and Soil Products
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.nur.business.sells_potting_mix
  - qs.nur.business.own_brand_mix
  rules:
  - when: qs.nur.business.own_brand_mix == yes
    action: refer
  - when: qs.nur.business.sells_potting_mix == yes
    action: apply
  reason: Applies because you sell potting mix or soil products. Referred if you make, blend or bag them under your own brand.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

This endorsement applies to potting mix, soil, compost, mulch and other growing media that you sell.

- Each bag or container of potting mix you sell must carry the health warning that the law or the Australian Standard for potting mixes (AS 3743) requires. Bulk potting mix must be sold with that warning displayed where it is sold and printed on the invoice or docket.
- Keep a record of each batch you buy or make, and of its supplier.

Growing media you make, blend or bag for sale under your own name or brand are covered only if the schedule shows own-brand products as covered. If a condition of this endorsement was not met, [[ref:nur.cond.insurance-contracts-act]] applies.

[WP REVIEW: confirm the current edition of AS 3743 and which states or territories make its warning label mandatory by law.]

Schedule variables: own-brand products covered (default: no).
