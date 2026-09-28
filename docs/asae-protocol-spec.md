# ASAE — Ayorai Secure Action Envelope

**Status:** Experimental protocol specification  
**Version:** 0.1

ASAE defines a security boundary between an AI agent and a protected executor. The agent can request an action, but cannot grant itself authority.

## Design principles

1. Public protocol, private authority.
2. Least privilege.
3. Short-lived authorization.
4. Replay resistance.
5. Resource-bound capabilities.
6. Independent policy decision.
7. Explicit transaction state.
8. Fail closed on missing evidence.
9. Auditable authorization.
10. No reliance on model secrecy.

## Security boundary

```text
Agent intent
    ↓
Policy decision
    ↓
Scoped authorization envelope
    ↓
Independent verifier
    ↓
Protected executor
```

The protocol is public. Security depends on protected keys, capability state, freshness, policy state and independently enforced authorization.

Version 0.1 is research-only and requires formal review, cryptographic review, fuzzing, property-based testing and independent security assessment before production use.
