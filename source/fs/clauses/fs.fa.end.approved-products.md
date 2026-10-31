---
id: fs.fa.end.approved-products
type: endorsement
heading: Approved Product List Condition
profession: financial-advisers
since: 1.0.0
status: draft
note: Market wordings commonly limit cover to approved products. This version keeps the switching and holding advice that ASIC RG 126.42 expects to be covered.
trigger:
  questions:
  - qs.fs.fa.approved_product_list
  - qs.fs.fa.off_apl_pct
  rules:
  - when: qs.fs.fa.approved_product_list = no
    action: refer
  - when: qs.fs.fa.off_apl_pct > 10
    action: suggest
  reason: Applies because {qs.fs.fa.off_apl_pct}% of your advice recommends products outside your approved product list.
---

For advice to acquire a financial product, we cover you only if the product was on your approved product list when the advice was given, or you had completed and recorded your own review of the product before the advice was given.

This endorsement does not apply to advice to switch from a product to one on your approved product list, or to continue holding a product, or to advice on a product the client already held.
