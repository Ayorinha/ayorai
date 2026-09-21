# ASAE — Ayorai Secure Action Envelope

**Status:** Experimental protocol specification  
**Version:** 0.1  
**Scope:** Agent-to-security-plane communication

## 1. Purpose

ASAE defines a security boundary between an AI agent and a protected executor.

The agent can request an action. The agent cannot grant itself authority to perform that action.

## 2. Design principles

1. **Public protocol, private authority.**
2. **Least privilege.**
3. **Short-lived authorization.**
4. **Freshness against replay.**
5. **Resource-bound capabilities.**
6. **Independent policy decision.**
7. **Explicit transaction state.**
8. **Fail closed on missing security evidence.**
9. **Auditable authorization.**
10. **No reliance on model secrecy.**

## 3. Conceptual message flow

```
Agent
  |
  | REQUEST(intent, context)
  v
Policy Decision Point
  |
  | CHALLENGE(nonce, epoch, policy)
  v
Agent / Adapter
  |
  | AUTH_REQUEST(capability, nonce, bounded_args)
  v
Authorization Verifier
  |
  | SIGNED_ENVELOPE
  v
Transaction Executor
  |
  +--> PREPARE
  +--> VERIFY
  +--> COMMIT
  +--> AUDIT
```

## 4. Authorization object

Conceptually:

```text
protocol_version
issuer
subject
capability
resource_scope
operation
bounded_arguments
provenance_hash
risk_class
policy_version
session_epoch
nonce
issued_at
expires_at
parent_delegation
transaction_id
signature
```

This is a protocol model, not a final wire format.

## 5. Cryptographic requirement

The final implementation must use a reviewed cryptographic construction and a vetted library.

Do not invent cryptography.

The proposed novelty is in **protocol composition and security semantics**, not a new cipher or signature algorithm.

## 6. Replay resistance

An authorization artifact must be rejected when:

- nonce was already consumed;
- expiration has passed;
- session epoch is invalid;
- policy version is incompatible;
- resource scope changed;
- transaction identifier is already committed.

## 7. Delegation

Delegation must narrow authority rather than expand it.

Example:

```
Parent:
  capability = payment
  scope = account:A
  max_value = 1000

Child:
  capability = payment
  scope = account:A
  max_value = 100
  expires = 60s
```

The child cannot create a child with a broader capability.

## 8. Fail-closed behavior

Invalid or ambiguous authorization results in:

```
DENY
```

High-impact operations without sufficient evidence become:

```
REVIEW
```

Suspicious persistent state becomes:

```
QUARANTINE
```

## 9. Model boundary

The LLM should receive a semantic representation of permitted capabilities, not private credentials.

Private authorization material must remain outside the model context.

## 10. Security properties to test

- authenticity;
- integrity;
- authorization;
- freshness;
- non-replay;
- scope confinement;
- delegation confinement;
- transaction integrity;
- audit linkage;
- cross-agent isolation.

## 11. Implementation maturity

Version 0.1 is a research specification.

A production implementation requires:

- formal protocol review;
- cryptographic review;
- threat modeling;
- interoperability testing;
- fuzzing;
- property-based testing;
- replay testing;
- fault injection;
- independent security assessment.
