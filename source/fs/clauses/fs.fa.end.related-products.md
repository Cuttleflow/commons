---
id: fs.fa.end.related-products
type: endorsement
heading: Related Products Exclusion
profession: financial-advisers
since: 1.0.0
status: draft
note: Conflicted product recommendations are central to recent adviser claims. Because this exclusion can remove cover ASIC expects, it is never applied automatically.
trigger:
  questions:
  - qs.fs.fa.related_products
  rules:
  - when: qs.fs.fa.related_products = yes
    action: refer
  reason: Applies because you recommend products issued or promoted by you or a related party.
  responses:
  - Attach
  - Attach with special excess
  - Attach with premium loading
  - Do not attach
  - Decline risk
---

We do not cover any claim, loss or liability arising from advice to acquire a financial product that is issued, operated or promoted by you, a representative, or a related party, or from which you or a related party receive a benefit other than advice fees paid by the client.
