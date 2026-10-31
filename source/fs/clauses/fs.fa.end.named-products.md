---
id: fs.fa.end.named-products
type: endorsement
heading: Named Products Exclusion
profession: financial-advisers
since: 1.0.0
status: draft
note: For products subject to known mass claims, such as the Shield Master Fund and the First Guardian Master Fund. Because this exclusion removes advice cover, it is never applied automatically, and the
  licensee must consider how it will otherwise meet claims (RG 126.44 to RG 126.45).
trigger:
  questions:
  - qs.fs.fa.named_products_exposure
  rules:
  - when: qs.fs.fa.named_products_exposure = yes
    action: refer
  reason: Applies because you advised clients on a product subject to known mass claims.
  responses:
  - Attach
  - Attach with special excess
  - Do not attach
  - Decline risk
---

We do not cover any claim, loss or liability arising from advice to acquire, switch to or continue to hold a financial product named in the schedule for this endorsement.
