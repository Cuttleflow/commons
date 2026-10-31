---
id: pi.rl.end.payroll-administration
type: endorsement
heading: Payroll Administration
profession: recruitment-labour-hire
since: 1.0.0
status: draft
note: Adds cover. Payday super (from 1 July 2026) shortens the time to pay superannuation and is expected to increase errors.
trigger:
  questions:
  - qs.pi.rl.payroll_clients
  rules:
  - when: qs.pi.rl.payroll_clients > 0
    action: broker_option
  reason: Offered because you run payroll for {qs.pi.rl.payroll_clients} clients.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Do not attach
---

Payroll administration for clients, including calculating and paying wages, superannuation contributions and tax withholding on a client's behalf, is a professional service under this policy.

For all claims arising from payroll administration, the most we will pay in total, including defence costs, is the sub-limit shown in the schedule for this endorsement, which is part of the limit of liability. [[ref:pi.rl.excl.employer-payments]] continues to apply to amounts you owe as an employer of your own workers.
