---
id: do.end.e01
type: endorsement
heading: E01 United States / Canada Jurisdiction Extension
since: 1.3.0
status: draft
trigger:
  questions:
  - qs.do.exposure.us_subsidiary
  - qs.do.exposure.us_revenue_pct
  - qs.do.exposure.us_listed
  rules:
  - when: "qs.do.exposure.us_subsidiary == yes or qs.do.exposure.us_listed == yes or qs.do.exposure.us_revenue_pct >= 10"
    action: refer
  - when: "qs.do.exposure.us_revenue_pct > 0"
    action: suggest
  reason: Applies because the company has a subsidiary in, earns {qs.do.exposure.us_revenue_pct}% of its revenue from, or has securities traded in, the United States or Canada.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

**Amendment to [[ref:do.excl.us-canada-jurisdiction]]**

[[ref:do.excl.us-canada-jurisdiction]] is deleted and replaced with: “This policy covers claims brought or maintained in courts in the United States of America and Canada, including securities claims alleging violations of US federal or state securities laws (including sections 11, 12, and 15 of the US Securities Act of 1933, section 10(b) of the US Securities Exchange Act of 1934 and Rule 10b-5 thereunder, and any equivalent state ‘blue sky’ laws).”

**Additional Definitions**

US securities claim means a securities claim brought in the United States alleging violations of US federal or state securities laws.

**Additional Exclusion — ERISA**

We do not cover any claim arising from a violation of the Employee Retirement Income Security Act of 1974 (ERISA) or any similar US federal or state statute governing employee benefit plans.

**Additional Retention**

For a US securities claim under Side C, the retention is the amount shown in the schedule for US securities claims (which may be higher than the standard Side C retention).

**Service of Suit**

We agree that any legal proceedings arising under this endorsement may be brought in a court of competent jurisdiction within the United States, and we will accept the decision of that court, including on any appeal.

Schedule variables: US securities claim retention; USA and Canada sub-limit, if any.
