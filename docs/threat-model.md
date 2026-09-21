# AYORAI Shield Threat Model

## Scope

Shield protects agentic systems at the boundary between model reasoning and consequential execution.

## Assets

- system/developer instructions;
- user and tenant data;
- credentials and delegated authority;
- retrieved documents and web content;
- memory and persistent state;
- tool/MCP configuration;
- model outputs;
- agent-to-agent messages;
- authorization artifacts;
- transaction state;
- audit evidence;
- application state.

## Adversaries

- malicious end user;
- malicious web/document content;
- compromised MCP/tool server;
- poisoned memory source;
- compromised agent;
- malicious delegated agent;
- supply-chain dependency;
- attacker attempting replay, privilege escalation, data exfiltration or irreversible state change.

## Attack classes

| Surface | Threat | Required control |
|---|---|---|
| Input | direct/indirect prompt injection | contextual boundary |
| Retrieval | poisoned document/web content | provenance + data/instruction separation |
| Tool | abuse / privilege escalation | capability authorization |
| MCP | malicious server / confused deputy | server identity + allowlist + scoped credentials |
| Memory | poisoning / persistence | provenance + integrity + quarantine |
| Multi-agent | instruction laundering / privilege propagation | independent identity and policy checks |
| Identity | impersonation / stale authority | authenticated agent identity + short-lived credentials |
| Authorization | scope expansion | least privilege + delegation confinement |
| Replay | reused authorization | nonce + expiry + session epoch |
| Output | exfiltration / unsafe tool transition | destination and action policy |
| Autonomy | irreversible high-impact action | explicit approval + transaction boundary |
| Supply chain | compromised dependency/model/tool | pinning + scanning + provenance |
| Cost | loops / denial-of-wallet | budgets + rate limits + circuit breakers |
| Availability | tool/model exhaustion | timeouts + isolation + recovery |
| Audit | evidence tampering | chained evidence + external durable storage in production |

## Security properties

1. **Confidentiality** — unauthorized data is not exposed.
2. **Integrity** — unauthorized state changes are blocked.
3. **Authorization** — actions remain within delegated capability.
4. **Containment** — compromise of one agent does not automatically compromise another.
5. **Freshness** — stale/replayed authorization is rejected.
6. **Provenance** — security decisions can be traced to source and authority.
7. **Recoverability** — suspicious state can be quarantined or rolled back where technically possible.
8. **Auditability** — security events can be reconstructed.

## Security invariant

**Model output is not authority.**

A natural-language request, tool-call proposal or generated protocol message cannot authorize itself. The executor requires an independently verifiable authorization artifact.

## Residual risk

No architecture can guarantee protection against every attack. Remaining risks include compromised trusted infrastructure, stolen signing material, application vulnerabilities, malicious authorized users, denial of service and unknown attack classes. These are explicit research targets rather than hidden assumptions.
