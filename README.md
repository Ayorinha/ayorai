# AYORAI — Agentic Intelligence & AI Safety

AYORAI is an applied AI engineering framework for modular agentic systems with explicit orchestration, safety controls, memory, RAG, MCP and tool governance.

## 🛡️ AYORAI Shield

**Runtime Security Control Plane for AI Agents & MCP Systems**

AYORAI Shield treats agent inputs, retrieved content, tool metadata, tool calls and persistent memory as separate trust boundaries. It provides deterministic controls for high-impact actions and produces structured security decisions that can be audited and tested.

Current controls include:
- goal-hijacking / prompt-injection pattern detection;
- explicit tool authorization and least privilege;
- tool-definition integrity baselines and metadata-drift detection;
- untrusted memory-write gating;
- credential-like data boundary detection.

See docs/shield.md for the security model and roadmap.

## Engineering goals
- deterministic agent contracts
- multi-agent orchestration
- prompt-injection and policy defenses
- auditable execution context
- retrieval and tool interfaces without vendor lock-in
- automated tests and CI

## Architecture
~~~text
User → Shield → Planner → Router → Specialized Agents
          │                         ├─ Research
          │                         ├─ Analyst
          │                         ├─ Security
          │                         └─ Reviewer
          └→ Policy / Tool / MCP / Memory Controls
                    ↓
                 Audit → Result
~~~

## Repository structure
- src/ayorai/agents — specialized agents
- src/ayorai/core — shared contracts
- src/ayorai/orchestration — planning and routing
- src/ayorai/safety — policy and risk controls
- src/ayorai/shield — runtime security enforcement
- src/ayorai/memory — state interfaces
- src/ayorai/rag — retrieval interfaces
- src/ayorai/mcp — tool/context adapters
- src/ayorai/tools — governed tools
- tests — automated tests

## Quick start
~~~bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
~~~

## Status
Foundation rebuilt with multi-agent contracts, orchestration, safety, memory, RAG, MCP and tool governance. AYORAI Shield is now the dedicated runtime-security layer; production deployment still requires deployment-specific identity, authentication, audit storage and adversarial evaluation.

## Author
Anderson Leon Ayora — AYORAI · Applied Intelligence