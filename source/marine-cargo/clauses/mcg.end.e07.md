---
id: mcg.end.e07
type: endorsement
heading: E07 Import Duty and Taxes
since: 1.0.0
status: draft
trigger:
  questions:
  - qs.mcg.cover.duty_requested
  rules:
  - when: qs.mcg.cover.duty_requested == yes
    action: broker_option
  reason: Offered because you asked to insure import duty and taxes.
---

For import transits, the value of the goods in [[ref:mcg.pay.basis-of-valuation]] includes the import duty, GST and other taxes payable on their entry into Australia, where you pay them and cannot recover them after the loss.

We pay that part of the value only where the duty or tax has been paid or is payable and is not refunded or remitted because of the loss.

Schedule variables: none.
