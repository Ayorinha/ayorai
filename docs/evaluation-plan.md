# AYORAI Shield Evaluation Plan

## Principle

A security system is credible when defenses are measured against adaptive attacks while preserving legitimate task utility.

## Evaluation layers

1. **Unit security tests** — injection variants, Unicode/obfuscation, multilingual inputs, instruction/data boundaries, tool authorization, malformed arguments, memory poisoning, output exfiltration, replay and scope.
2. **Protocol tests** — signature integrity, nonce uniqueness, expiration, session epochs, policy-version mismatch, delegation confinement and resource-scope boundaries.
3. **Scenario tests** — malicious web page, poisoned RAG document, compromised MCP tool, compromised agent, malicious memory and high-impact action.
4. **Harness tests** — tool discovery, credential isolation, timeouts, budgets, circuit breakers, logging and fail-closed behavior.
5. **Public benchmarks** — AgentDojo, AgentDyn and applicable garak probes.
6. **Adaptive attacker** — payload mutation, indirect injection, tool-description abuse, memory manipulation, authorization probing and cross-agent propagation.
7. **Regression** — every discovered failure becomes a permanent test with a corpus hash and reproducible fixture.
8. **Multilingual evaluation** — at minimum English, Portuguese, Spanish, French, Mandarin, Japanese, Korean and Hindi; expand based on deployment.

## Metrics

- ASR — attack success rate
- BTS — benign task success
- FPR — false-positive rate
- UCR — unauthorized call rate
- DER — data-exfiltration rate
- RPA — replay acceptance rate
- SEA — scope-escalation acceptance
- APR — attack propagation rate
- ACR — audit completeness
- RRS — recovery success
- L95 — 95th percentile latency
- CPA — cost amplification

Security evaluation must not optimize blocking alone; legitimate task completion and over-defense must be reported.

## Reproducibility

Record model/version, policy version, protocol version, tools, benchmark version, attack corpus hash, configuration, seeds where applicable, runtime, date, raw results and limitations.

## Publication standard

No security percentage without a defined denominator, corpus, configuration and reproducible artifact.

## Safety of the evaluation environment

Adversarial testing must remain inside synthetic or explicitly authorized environments. The research harness should never turn a benchmark into uncontrolled exploitation of external systems.
