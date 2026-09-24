# AYORAI Shield Threat Model

## Scope

The threat model covers agentic systems in which an AI model can consume untrusted content, retrieve data, call tools, write memory, or coordinate with other agents.

## Assets

- credentials and secrets;
- personal, financial and institutional data;
- retrieved documents and knowledge bases;
- agent memory;
- tool permissions;
- execution plans;
- audit records and provenance;
- security policies and detection rules.

## Trust boundaries

1. User/input → agent.
2. Agent → retrieved content.
3. Agent → memory.
4. Agent → MCP/tool.
5. Tool → external system.
6. Threat intelligence → adaptive-defense pipeline.
7. Model output → policy engine.
8. Security telemetry → audit store.

Every boundary is treated as a potential injection or integrity boundary.

## Threat classes

- prompt injection and indirect prompt injection;
- goal hijacking;
- tool abuse;
- privilege escalation;
- unauthorized data access;
- data exfiltration;
- memory poisoning;
- retrieval poisoning;
- malicious tool metadata;
- cross-agent trust abuse;
- policy manipulation;
- telemetry/provenance tampering;
- compromised learning inputs;
- denial of service through resource exhaustion.

## Security principles

### Least privilege

Agents and tools should receive only the permissions required for the current task.

### Explicit authorization

Sensitive actions require deterministic policy checks. Model output is not authorization.

### Provenance

Security decisions should retain enough provenance to reconstruct what evidence and policy inputs contributed to the decision.

### Containment

A compromised agent should not automatically gain the authority of other agents or tools.

### Fail closed for high-impact actions

When authorization or integrity cannot be established for a high-impact operation, the system should prefer review or isolation over silent execution.

### Untrusted learning

External intelligence, retrieved content and telemetry may propose new knowledge or rules but must not silently modify active security policy.

## Risk treatment

| Threat | Primary control | Residual risk |
|---|---|---|
| Prompt injection | input normalization + policy checks + adversarial tests | New attack variants |
| Tool abuse | tool allowlists + authorization | Misconfigured deployment |
| Memory poisoning | trust boundaries + validation | Complex application-specific semantics |
| Data exfiltration | sensitive-data boundaries + action policy | Undetected sensitive content |
| Policy tampering | controlled promotion + auditability | Compromised deployment credentials |
| Multi-agent abuse | isolation + explicit routing | Complex emergent interactions |
| Learning poisoning | quarantine + validation gate | Malicious or biased evidence |
| Audit tampering | provenance/hash controls | Host or key compromise |

This table is a risk model, not proof that any threat is fully mitigated.
