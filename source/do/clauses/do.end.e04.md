---
id: do.end.e04
type: endorsement
heading: E04 Environmental, Social, and Governance (ESG)
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.do.cover.options_requested
  - qs.do.insured.entity_type
  rules:
  - when: "'E04' in qs.do.cover.options_requested"
    action: broker_option
  - when: "qs.do.insured.entity_type == 'listed'"
    action: suggest
  reason: Offered because you asked for cover for greenwashing, climate disclosure and activist shareholder claims.
  responses:
  - Attach
  - Attach with premium loading
  - Do not attach
---

**Greenwashing Claims**

We will cover claims against an insured alleging misleading or deceptive conduct in connection with environmental, social, or governance disclosures, sustainability reports, or ESG-related representations made by the company — including claims under section 1041H of the Corporations Act 2001 (Cth) or the Australian Consumer Law. This includes enforcement action alleging greenwashing in relation to financial products, investment strategies, or corporate disclosures.

**Climate Disclosure**

We will cover claims arising from the company's climate-related disclosures, including disclosures required under the Australian Sustainability Reporting Standards (ASRS) or equivalent mandatory disclosure requirements, and voluntary disclosures made in accordance with the TCFD framework or its successors.

**Activist Shareholder Claims**

We will cover claims brought by shareholders or shareholder activist groups alleging that the company's directors and officers have failed to adequately address climate-related risks, transition risks, or sustainability-related risks in their governance and strategy.

Schedule variables: ESG sub-limit, if any.
