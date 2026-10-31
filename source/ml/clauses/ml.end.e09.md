---
id: ml.end.e09
type: endorsement
heading: E09 Not-for-Profit and Association
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.ml.insured.entity_type
  rules:
  - when: qs.ml.insured.entity_type in ['not_for_profit', 'association']
    action: apply
  reason: Applies because the named insured is a not-for-profit organisation or an incorporated association.
  responses:
  - Attach
  - Do not attach
---

This endorsement applies where the named insured is a not-for-profit organisation, an incorporated association, a company limited by guarantee or a charitable trust.

For this policy:

- the definition of [[ref:ml.def.insured-person|heading]] includes any trustee, honorary office holder, committee member, and any volunteer while acting at the direction of the board or committee of management;
- [[ref:ml.excl.insured-versus-insured]] does not apply to a claim brought by a member of the company in their capacity as a member, unless an insured person brings, assists or participates in it other than as a witness;
- [[ref:ml.excl.major-transactions]] does not apply to a merger with, or acquisition of, another not-for-profit entity; and
- the Company Liability section covers claims brought by a grant provider or funding body alleging misuse of grant or donated funds, but not repayment of the grant or donation itself.

Schedule variables: none.
