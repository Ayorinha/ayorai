# AYORAI Shield Benchmark Matrix

This is a capability comparison, not a ranking.

| System | Primary emphasis | Dynamic attacks | Tool/MCP | Memory | Multi-agent | Provenance | Runtime authorization | Evidence |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| AgentDojo | agent prompt-injection evaluation | Yes | Yes | Limited | Limited | Partial | Evaluation | Yes |
| garak | LLM security probing | Yes | Not primary | Not primary | Not primary | Not primary | Not primary | Yes |
| AgentDyn | open-ended agent security benchmark | Yes | Yes | Limited | Limited | Partial | Evaluation | Yes |
| OWASP Agent Security | practical agent controls | Guidance | Yes | Yes | Yes | Yes | Yes | Yes |
| OWASP MCP | MCP attack surface | Guidance | Yes | Limited | Partial | Yes | Yes | Yes |
| NIST AML | adversarial ML taxonomy | N/A | N/A | N/A | N/A | N/A | N/A | Risk |
| CMU AISIRT | incident response | Incident | Yes | Yes | Yes | Yes | Response | Strong |
| CMU Cyber Autonomy | autonomous cyber defense | Research | Research | Research | Research | Research | Research | Research |
| Stanford agent identity | identity/delegation | Not primary | Yes | Not primary | Yes | Yes | Yes | Yes |
| Berkeley AISI | agentic risk management | Scenario | Yes | Yes | Yes | Yes | Governance | Yes |
| Tsinghua secure AI | secure/robust AI + privacy | Research | Research | Research | Research | Research | Research | Research |
| NJU SecLab | AI/system security | Research | Research | Research | Research | Research | Research | Research |
| **AYORAI Shield** | integrated runtime security | Target | Target | Target | Target | Target | Target | Target |

## Required Shield measurements
Attack success rate, benign-task success, false positives/over-defense, unauthorized tool calls, sensitive-data exfiltration, memory-poisoning persistence, cross-agent propagation, latency, audit completeness, recovery success and adversarial cost amplification.

"Target" means an engineering objective, not a completed feature.
