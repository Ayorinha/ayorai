# AYORAI Shield — Agentic AI Security & Resilience

AYORAI Shield is an open-source research and engineering framework for defending **agentic AI systems**: LLM agents, RAG pipelines, MCP/tool ecosystems, memory, multi-agent orchestration and autonomous workflows.

The project is designed around a simple principle:

> **Do not trust the model, the prompt, the retrieved data, the tool, the memory, or the agent chain by default. Verify each transition.**

## What Shield is building

AYORAI Shield is not positioned as a conventional prompt filter. Its target architecture is a **runtime security control plane for AI agents**, combining:

- contextual prompt-injection detection;
- least-privilege tool and MCP authorization;
- provenance-aware retrieval;
- memory integrity and isolation;
- risk-adaptive action gating;
- multi-agent trust boundaries;
- tamper-evident audit trails;
- adversarial evaluation and regression testing;
- human approval for high-impact actions;
- continuous threat-intelligence and benchmark updates.

### Security pipeline

```
Untrusted Input / Web / RAG / MCP / Memory
                 |
                 v
        +-------------------+
        |  PROVENANCE LAYER |
        +-------------------+
                 |
                 v
        +-------------------+
        | CONTEXTUAL GUARD  |
        | injection / goal  |
        | hijack / leakage  |
        +-------------------+
                 |
                 v
        +-------------------+
        | POLICY + RISK     |
        | identity / scope  |
        | tool / action     |
        +-------------------+
                 |
                 v
        +-------------------+
        | AGENT ORCHESTRATOR|
        +-------------------+
          |       |       |
       planner  analyst  researcher
          |       |       |
          +-------+-------+
                  |
                  v
        +-------------------+
        | TOOL/MCP GATEWAY  |
        | allowlist/schema  |
        | capability scope  |
        +-------------------+
                  |
                  v
        +-------------------+
        | OUTPUT + ACTION   |
        | validation / HITL |
        +-------------------+
                  |
                  v
        +-------------------+
        | AUDIT / TELEMETRY |
        | tamper-evident    |
        +-------------------+
```

## Research basis

Shield tracks the current security landscape across NIST adversarial ML guidance, OWASP agent/MCP security guidance, MIT/CMU autonomous cyber-defense research, Stanford agent identity and authorization research, Berkeley agentic-AI risk management, ETH Zürich AgentDojo, Oxford AI cybersecurity research, and Chinese research on secure/robust AI and agent security.

See:
- `docs/research-landscape.md`
- `docs/benchmark-matrix.md`
- `docs/security-architecture.md`
- `docs/threat-model.md`
- `docs/evaluation-plan.md`
- `docs/community-roadmap.md`

## Repository structure

- `src/ayorai/agents` — specialized agents
- `src/ayorai/core` — shared contracts
- `src/ayorai/orchestration` — planning and routing
- `src/ayorai/safety` — policy, guard and audit controls
- `src/ayorai/memory` — memory interfaces
- `src/ayorai/rag` — retrieval interfaces
- `src/ayorai/mcp` — MCP/tool adapters
- `src/ayorai/tools` — governed tools
- `tests` — automated regression suite

## Current maturity

The repository contains a working engineering foundation with multi-agent contracts, orchestration, safety gates, memory, RAG, MCP and tool governance. It is **not yet a production security appliance**. Production-grade claims require authenticated identity, stronger policy enforcement, durable tamper-evident telemetry, sandboxing, adversarial benchmarks and independent evaluation.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Design differentiators

Shield's research direction is deliberately broader than a static jailbreak detector:

1. **Contextual trust** — security decisions incorporate source, provenance, identity, action, tool and session context.
2. **Capability-bounded agents** — an agent receives explicit capabilities instead of broad implicit authority.
3. **Memory defense** — persistent memory is treated as an attack surface, not a trusted database.
4. **Multi-agent containment** — trust does not automatically propagate from one agent to another.
5. **Risk-adaptive autonomy** — autonomy can contract when uncertainty, impact or attack evidence increases.
6. **Tamper-evident evidence** — security decisions are recorded so incidents can be reconstructed.
7. **Continuous adversarial evaluation** — every new defense should be tested against adaptive attacks and regression cases.

These are research goals and engineering properties to be demonstrated experimentally, not claims of superiority over all existing systems.

## Author

Anderson Leon Ayora — AYORAI · Applied Intelligence
