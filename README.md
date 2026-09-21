# AYORAI — Agentic Intelligence & AI Safety

AYORAI is an applied AI engineering framework for modular agentic systems with explicit orchestration, safety controls, memory, RAG, MCP and tool governance.

## AYORAI Shield

AYORAI Shield is the project's runtime-security foundation for agentic AI. It is designed around deterministic authorization, least privilege, provenance, auditability, multi-agent containment and controlled adaptive defense.

### Security architecture

```
User / Untrusted Content
          ↓
     Safety Guard
          ↓
 Planner → Router → Specialized Agents
                     ├─ Research
                     ├─ Analyst
                     ├─ Security
                     └─ Reviewer
          ↓
     Memory / RAG / MCP / Tools
          ↓
   Deterministic Risk Engine
          ↓
       Policy Engine
      ┌────┼─────┐
    ALLOW REVIEW ISOLATE
          ↓
      Audit / Evidence
```

Model output is treated as evidence, not authorization. High-impact actions require deterministic policy controls and, where configured, explicit human approval.

## Adaptive defense

Threat intelligence and telemetry may propose new knowledge or rules, but they are treated as untrusted evidence. New rules must remain quarantined until validation and explicit promotion.

The defender must defend its own learning process.

## Security status

| Capability | Status |
|---|---|
| Agent contracts and orchestration | Implemented |
| Tool/MCP governance | Implemented |
| Deterministic safety/policy controls | Implemented |
| Audit and execution context | Implemented |
| Provenance/integrity controls | Implemented/expanding |
| Adversarial evaluation corpus | Implemented/expanding |
| Adaptive-defense quarantine model | Implemented/expanding |
| CodeQL + CI | Implemented |
| Local semantic runtime | Experimental plan |
| BitNet integration | Not yet integrated |
| Endpoint EDR/XDR | Out of current scope |
| Malware sandbox | Out of current scope |
| Independent security audit | Pending |

See [SECURITY-CLAIMS.md](SECURITY-CLAIMS.md), [SECURITY.md](SECURITY.md), [docs/THREAT-MODEL.md](docs/THREAT-MODEL.md), [docs/VALIDATION-GATES.md](docs/VALIDATION-GATES.md), [docs/EVALUATION.md](docs/EVALUATION.md), [docs/LOCAL-RUNTIME.md](docs/LOCAL-RUNTIME.md), and [docs/OPERATIONS.md](docs/OPERATIONS.md).

## Engineering goals

- deterministic agent contracts
- multi-agent orchestration
- prompt-injection and policy defenses
- auditable execution context
- retrieval and tool interfaces without vendor lock-in
- automated tests and CI
- reproducible adversarial evaluation
- explicit security claims and limitations
- local-first security components where evidence supports them

## Repository structure

- `src/ayorai/agents` — specialized agents
- `src/ayorai/core` — shared contracts
- `src/ayorai/orchestration` — planning and routing
- `src/ayorai/safety` — policy and risk controls
- `src/ayorai/memory` — state interfaces
- `src/ayorai/rag` — retrieval interfaces
- `src/ayorai/mcp` — tool/context adapters
- `src/ayorai/tools` — governed tools
- `tests` — automated tests
- `docs` — threat model, validation, evaluation and operations

## Validation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
ruff check .
pytest -q
```

Security-sensitive changes should follow the validation gates documented in `docs/VALIDATION-GATES.md`.

## Scope and limitations

AYORAI Shield is an engineering and research foundation for agentic AI security. It is not currently a complete antivirus, EDR/XDR, malware sandbox, SIEM/SOAR or enterprise identity platform. Production deployments require deployment-specific identity, secrets/key management, monitoring, network controls, incident response and adversarial validation.

No absolute-security claim is made.

## Author

Anderson Leon Ayora — AYORAI · Applied Intelligence
