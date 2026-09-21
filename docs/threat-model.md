# AYORAI Shield Threat Model

## Threat model scope

Shield protects agentic systems rather than only the underlying LLM.

### Assets

- system and developer instructions;
- user data;
- credentials and delegated authority;
- retrieved documents;
- memory;
- tool parameters;
- model outputs;
- agent-to-agent messages;
- audit evidence;
- application state.

### Adversaries

- malicious end user;
- malicious document/web page;
- compromised tool/MCP server;
- poisoned memory source;
- malicious or compromised agent;
- supply-chain dependency;
- attacker attempting to induce costly or irreversible behavior.

## Attack classes

| Attack surface | Example | Required defense |
|---|---|---|
| Input | direct prompt injection | contextual analysis |
| Retrieval | indirect injection in document | provenance + content isolation |
| Web | malicious webpage | untrusted-content boundary |
| Tool | tool abuse / privilege escalation | capability authorization |
| MCP | malicious server/configuration | server identity + allowlist |
| Memory | memory poisoning | integrity + provenance + quarantine |
| Multi-agent | confused deputy / instruction laundering | independent policy checks |
| Output | data exfiltration | output and destination policy |
| Autonomy | excessive/irreversible action | risk-adaptive approval |
| Supply chain | compromised dependency | dependency pinning + scanning |
| Cost | denial-of-wallet / loops | budgets + rate limits |
| Availability | tool/model exhaustion | timeouts + circuit breakers |

## Security properties

Shield should demonstrate:

1. **Confidentiality** — unauthorized data is not exposed.
2. **Integrity** — unauthorized state changes are blocked.
3. **Authorization** — actions stay within delegated capability.
4. **Containment** — compromise of one agent does not automatically compromise others.
5. **Provenance** — security-relevant decisions can be traced to sources and authority.
6. **Recoverability** — suspicious state can be quarantined and rolled back.
7. **Auditability** — security events are reconstructable.

## Residual risk

No prompt filter can guarantee protection against all attacks. The threat model therefore assumes defense in depth: contextual controls, authorization, isolation, monitoring, evaluation and human oversight for high-impact actions.
