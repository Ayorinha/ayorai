# AYORAI Shield

AYORAI Shield is the runtime security control plane for AYORAI agentic systems.

## Security model

Shield treats agent inputs, retrieved content, tool metadata, tool calls and persistent memory as distinct trust boundaries. Decisions are deterministic and explicit; model-assisted detection can be added behind the same enforcement interface without making the model itself the final authority.

## Initial controls

| Control | Purpose | Reference |
|---|---|---|
| Goal-hijacking detection | Detect configured instruction-hierarchy manipulation patterns | OWASP Agentic ASI01 |
| Tool authorization | Enforce explicit tool allowlists | OWASP Agentic ASI02 |
| Tool metadata integrity | Detect changes to a trusted tool-definition fingerprint | OWASP Agentic ASI04 |
| Memory-write gate | Require an explicit trust decision before persistence | OWASP Agentic ASI06 |
| Sensitive-data boundary | Detect configured credential-like material | Data-loss prevention |

## Design principles

- **Default deny at high-impact boundaries.**
- **Explicit trust:** untrusted memory is not silently persisted.
- **Integrity before execution:** tool metadata can be baselined and checked for drift.
- **Deterministic enforcement:** policy decisions are inspectable and testable.
- **Auditability:** every decision should be representable as a structured security event.
- **No absolute-security claims:** the project documents its coverage and residual risk.

## Roadmap

1. Structured security events and tamper-evident audit chaining.
2. MCP-aware tool-call inspection and parameter policy.
3. Provenance tracking for RAG and memory content.
4. Adversarial evaluation corpus mapped to OWASP Agentic risks.
5. Human approval gates for high-impact actions.
6. Deployment adapters for identity, secrets and policy providers.

This project is an engineering and research foundation. It is not a certified security product and should be evaluated against the deployment's own threat model.
