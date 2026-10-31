---
id: cy.end.e15
type: endorsement
heading: E15 Generative AI Systems
since: 1.4.0
status: draft
trigger:
  questions:
  - qs.cy.cover.options_requested
  - qs.cy.ops.uses_ai_systems
  rules:
  - when: '''E15'' in qs.cy.cover.options_requested'
    action: broker_option
  - when: qs.cy.ops.uses_ai_systems == yes
    action: suggest
  reason: Suggested because you build or operate AI models or systems in your business.
  responses:
  - Attach
  - Attach with amended sub-limit
  - Attach with premium loading
  - Do not attach
---

For this policy:

- your computer system includes artificial intelligence systems you operate, or that are operated on your behalf, including models, model weights, training data, vector databases, and orchestration infrastructure, and data includes training data, fine-tuning data, and model weights;
- a cyber event includes: (a) data poisoning, meaning the deliberate corruption or manipulation of your training data or model weights by a person without authority; and (b) manipulation of an AI system's behaviour through adversarial inputs, including prompt injection, that results in **unauthorised** access to or disclosure of data;
- [[ref:cy.cover.data-restoration]] includes the reasonable costs of restoring, retraining, or fine-tuning an affected model to substantially its pre-event state, up to the model restoration sub-limit shown in the schedule; and
- a third party providing AI model hosting or inference services to you under written contract is a service provider for [[ref:cy.ext.dependent-business-interruption]].

This endorsement does not cover: (a) claims alleging infringement of intellectual property rights in training data or model outputs; (b) loss arising from the inherent inaccuracy, bias, or unreliability of model outputs without a cyber event; or (c) regulatory proceedings arising solely from your governance of AI systems.

Schedule variables: model restoration sub-limit; covered AI systems.
