---
id: pi.mm.end.usa-audience
type: endorsement
heading: United States Audience Exclusion
profession: marketing-media
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.pi.mm.us_audience_pct
  rules:
  - when: qs.pi.mm.us_audience_pct > 10
    action: refer
  reason: Applies because {qs.pi.mm.us_audience_pct}% of your audience is in the United States.
---

We do not cover any claim brought in a court of the United States of America or Canada, or under its law, arising from material that you created or published.
