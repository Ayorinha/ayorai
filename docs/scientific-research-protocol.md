# AYORAI Shield — Scientific Research Protocol

**Status:** Research proposal / engineering specification  
**Version:** 0.1  
**Author:** Anderson Leon Ayora — AYORAI · Applied Intelligence

## Abstract

AYORAI Shield proposes a defense architecture for agentic AI systems based on a separation between **semantic reasoning** and **security authorization**.

The central hypothesis is that an AI model should never be able to authorize a high-impact action merely by producing a plausible natural-language instruction or tool call. Instead, the action must cross an independent security channel that evaluates identity, capability, provenance, freshness, policy and reversibility.

The proposed mechanism is the **Ayorai Secure Action Envelope (ASAE)**: a structured, cryptographically authenticated envelope carrying an action request, scoped capability, provenance commitment, freshness nonce, policy version and transaction state. The envelope is intentionally designed so that knowledge of its public format is insufficient to authorize an action.

This is not security-through-obscurity. The protocol may be public. Security depends on protected keys, capability state, policy state, freshness and independently enforced authorization.

## 1. Research question

Can an agentic security layer reduce unauthorized high-impact actions by separating:

1. model-generated intent;
2. security authorization;
3. execution;
4. reversible state commitment?

### Primary hypothesis

**H1:** An independently enforced, capability-based security envelope with freshness, provenance and transactional commit controls will reduce unauthorized high-impact actions relative to a model-only or prompt-filter-only baseline.

### Secondary hypotheses

**H2:** Rotating capability state and nonces will reduce replay and static-payload effectiveness.

**H3:** Requiring a valid authorization artifact from an independent policy engine will prevent semantic imitation from becoming authority.

**H4:** Staged execution with rollback/quarantine will reduce irreversible impact even when an upstream agent is compromised.

## 2. Novelty boundary

The research claim is not that cryptographic authorization, capability systems, provenance, nonces or transactional rollback are individually new.

The proposed contribution is their **agent-native composition** into a security protocol specifically designed around the boundary between LLM reasoning and consequential execution.

Novelty must be established through a formal prior-art review and empirical comparison. Until that review is complete, this document uses the terms **proposed**, **hypothesis** and **research direction**, not "first", "unique" or "unbreakable".

## 3. Core architecture

```
LLM / Agent reasoning
        |
        | natural-language intent
        v
+-------------------------+
| Intent Normalizer       |
| no execution authority  |
+-------------------------+
        |
        v
+-------------------------+
| Policy Decision Point   |
| identity + capability   |
| provenance + risk       |
| freshness + context     |
+-------------------------+
        |
        | authorized envelope only
        v
+-------------------------+
| ASAE Security Channel   |
| authenticated + scoped  |
| nonce + policy version  |
+-------------------------+
        |
        v
+-------------------------+
| Transaction Sandbox     |
| prepare -> validate     |
| -> commit / rollback    |
+-------------------------+
        |
        v
Protected resource
```

## 4. Security invariant

A model output is **never** an authorization credential.

Formally:

```
ModelOutput != Authority
Authority = PDP(identity, capability, provenance, policy, freshness, context)
```

The executor must reject any request lacking a valid authorization artifact.

## 5. ASAE envelope

A conceptual envelope contains:

- protocol version;
- issuer identity;
- subject agent identity;
- delegated capability;
- resource scope;
- requested operation;
- bounded arguments;
- provenance commitment;
- risk class;
- policy version;
- nonce;
- expiration;
- parent delegation identifier;
- transaction identifier;
- authorization signature;
- optional human-approval reference.

Sensitive fields should not be exposed to the model unless required.

## 6. Why a new protocol can help

A new protocol does **not** become secure merely because an AI has not seen it during training.

A model can still infer, imitate or adapt to a public protocol.

The security advantage comes from making authorization depend on information and state that the model does not possess:

- private signing keys;
- short-lived capability tokens;
- unpredictable nonces;
- server-side authorization state;
- resource-bound scopes;
- policy-version checks;
- transaction state;
- independent approval.

This changes the problem from "Can the model understand the code?" to "Does the request carry independently verifiable authority?"

## 7. Moving-target component

Shield may optionally rotate:

- capability identifiers;
- nonce formats;
- session epochs;
- policy versions;
- authorization challenges.

Rotation is a **supplementary control**, not a replacement for cryptography.

The system must preserve backward-compatible verification windows where necessary and prevent rotation from becoming an availability attack.

## 8. Reversibility layer

High-impact operations should follow:

```
PREPARE -> VALIDATE -> STAGE -> VERIFY -> COMMIT
                                      |
                                  failure
                                      v
                                   ROLLBACK
```

The protected resource should remain unchanged until the commit condition is satisfied.

For resources that cannot support true transactions, Shield should use compensating actions, snapshots or quarantine where technically possible.

## 9. Threat model

The protocol is intended to address:

- prompt injection;
- indirect prompt injection;
- compromised agent;
- confused deputy;
- tool poisoning;
- MCP compromise;
- replay;
- stale authorization;
- cross-agent privilege propagation;
- malicious memory;
- unauthorized high-impact actions;
- output-to-tool laundering.

It does not by itself solve:

- compromised cryptographic keys;
- compromised trusted execution infrastructure;
- bugs in the protected application;
- denial of service;
- malicious authorized users;
- all model-level failures.

## 10. Experimental design

Compare at least four configurations:

| Configuration | Description |
|---|---|
| B0 | Agent without Shield controls |
| B1 | Agent + prompt/instruction guard |
| B2 | Agent + policy/tool authorization |
| B3 | Agent + ASAE + transactional controls |

Measure:

- unauthorized action rate;
- attack success rate;
- benign task success;
- false-positive rate;
- replay success rate;
- stale-token acceptance;
- privilege escalation rate;
- cross-agent propagation;
- sensitive-data exposure;
- rollback success;
- latency;
- availability impact;
- audit completeness.

## 11. Falsification criteria

The hypothesis should be considered unsupported if:

1. B3 does not materially reduce unauthorized high-impact actions compared with B2 under controlled experiments;
2. the protocol introduces unacceptable benign-task degradation;
3. replay or privilege-boundary tests routinely succeed;
4. the independent authorization layer can be bypassed through model-generated semantics;
5. rollback fails to contain tested high-impact scenarios.

## 12. Scientific standard

Every reported result must specify:

- model and version;
- benchmark/version;
- attack corpus;
- corpus hash;
- protocol version;
- policy version;
- tool configuration;
- random seed where applicable;
- hardware/runtime;
- denominator;
- confidence interval or uncertainty treatment where appropriate;
- limitations;
- reproducible artifact.

## 13. Relationship to existing research

The protocol should be evaluated against agent-security work such as AgentDojo and AgentDyn, NIST agent identity/authorization work, adversarial-ML guidance, and OWASP agent/MCP security guidance.

The objective is integration and measurable evidence, not replacement of those projects.

## 14. Research conclusion

The strongest version of the original idea is therefore not "invent a code that AI has never seen."

It is:

> **Create an authorization language that the model may understand but can never independently satisfy, because execution authority is established by an external cryptographic and stateful security plane.**

That is a testable cybersecurity research thesis.
