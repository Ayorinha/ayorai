# AYORAI — Agentic Intelligence & AI Safety

AYORAI is an applied AI engineering framework for modular agentic systems with explicit orchestration, safety controls, memory, RAG, MCP and tool governance.

## Engineering goals
- deterministic agent contracts
- multi-agent orchestration
- prompt-injection and policy defenses
- auditable execution context
- retrieval and tool interfaces without vendor lock-in
- automated tests and CI

## Architecture
```
User → Safety Guard → Planner → Router → Specialized Agents
                                      ├─ Research
                                      ├─ Analyst
                                      ├─ Security
                                      └─ Reviewer
                 → Memory / RAG / MCP / Tools → Safety → Result
```

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

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Status
Foundation rebuilt with multi-agent contracts, orchestration, safety, memory, RAG, MCP and tool governance.

## Author
Anderson Leon Ayora — AYORAI · Applied Intelligence
