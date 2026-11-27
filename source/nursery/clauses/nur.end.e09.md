---
id: nur.end.e09
type: endorsement
heading: E09 Incidental Landscaping and Installation
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.nur.business.landscaping_pct
  rules:
  - when: qs.nur.business.landscaping_pct > 20
    action: refer
  - when: qs.nur.business.landscaping_pct > 0
    action: apply
  reason: Applies because {qs.nur.business.landscaping_pct}% of your turnover comes from landscaping or installation work.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

[[ref:nur.li.excl-contracting]] is changed so that [[ref:nur.section.liability|heading]] covers your liability arising from planting, laying turf, building garden beds, landscaping and installing irrigation at customers' premises, where the income from it is no more than the share of turnover shown in the schedule.

This endorsement does not cover:

- building a structure that needs a building permit or a licensed builder, or a retaining wall more than 1 metre high;
- excavation deeper than 1 metre, or work within 3 metres of an overhead power line;
- felling, removing or pruning a tree more than 3 metres high; or
- connecting irrigation to a mains water supply, or other plumbing or electrical work that the law requires a licensed person to do.

Before you dig, you must obtain the information about underground services that the Before You Dig Australia service provides, and follow it. [[ref:nur.li.care-custody-control]] is changed so that it also covers property damage to the part of a customer's property you are working on, up to $25,000 for one occurrence. The special excess applies to each claim arising from this work. If a condition of this endorsement was not met, [[ref:nur.cond.insurance-contracts-act]] applies.

Schedule variables: share of turnover (default: 20%); special excess (default: $1,000).
