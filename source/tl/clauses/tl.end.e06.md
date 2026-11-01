---
id: tl.end.e06
type: endorsement
heading: E06 AI Governance and Model Liability
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.tl.cover.options_requested
  - qs.tl.ops.uses_ai_systems
  rules:
  - when: '''E06'' in qs.tl.cover.options_requested'
    action: broker_option
  - when: qs.tl.ops.uses_ai_systems == yes
    action: suggest
  reason: Suggested because you build, train or operate AI models or systems in your business.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

**technology services** includes the design, training, fine-tuning, testing, hosting and deployment of artificial intelligence models or systems for others, and **technology product** includes those models and systems.

The [[ref:tl.section.professional-liability|heading]] section covers a claim alleging that a model or system you supplied failed to perform as your contract or your documented specification required, or that you were negligent in its design, training, testing or monitoring, and that your client suffered a financial loss as a result. The [[ref:tl.section.cyber|heading]] section covers a cyber loss that results from data poisoning, meaning deliberate corruption of training data or model weights by a person without authority, or from adversarial inputs, including prompt injection, that result in **unauthorised** access to or disclosure of data.

[[ref:tl.ext.regulatory-penalties]] extends to the defence costs of a regulatory proceeding that arises from your governance of an AI system you supplied to a client. We do not pay a fine or penalty.

This endorsement does not cover: (a) a claim alleging infringement of intellectual property rights in training data or model outputs; (b) loss from the inherent inaccuracy, bias or unreliability of model outputs where you met the contract or specification; or (c) a claim alleging deliberate discrimination.

The most we will pay under this endorsement is the sub-limit shown in the schedule for it, which is part of the limit of liability. [WP REVIEW: confirm the regulatory defence costs paragraph against the statutory limits on insuring penalties and against the adopting insurer's regulatory-proceedings position.]

Schedule variables: covered AI systems; sub-limit.
