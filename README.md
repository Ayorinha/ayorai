# AYORAI — Agentic Intelligence & AI Safety

[![CI](https://github.com/Ayorinha/ayorai/actions/workflows/ci.yml/badge.svg)](https://github.com/Ayorinha/ayorai/actions/workflows/ci.yml)
[![Python](https://img.shields.io/badge/python-3.11%2B-blue.svg)](https://www.python.org/)
[![Coverage](https://img.shields.io/badge/coverage-pytest--cov-informational.svg)](https://github.com/Ayorinha/ayorai/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

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

## Architecture diagram

~~~mermaid
flowchart TD
    U[User / Task] --> S[AYORAI Shield]
    S --> P[Planner]
    P --> R[Router]
    R --> RA[Research Agent]
    R --> AN[Analyst Agent]
    R --> SE[Security Agent]
    R --> RV[Reviewer Agent]
    RA --> G[Governed Tools / MCP / RAG]
    AN --> G
    SE --> G
    RV --> G
    G --> A[Audit / Execution Result]
    S -. policy .-> G
~~~

> **Design principle:** orchestration, safety, tools, memory and retrieval remain explicit engineering boundaries.

## Repository structure

```text
.github/             CI, CodeQL, Dependabot and contribution templates
docs/                architecture, security, research and roadmap documentation
examples/            runnable usage examples
src/ayorai/
  agents/            specialized agents
  core/              shared contracts and execution types
  orchestration/     planning and routing
  safety/            policy and risk controls
  shield/            runtime security enforcement
  memory/            state interfaces
  rag/               retrieval interfaces
  mcp/               tool/context adapters
  tools/             governed tools
tests/               automated tests
pyproject.toml       package metadata and development tooling
SECURITY.md          vulnerability reporting
CONTRIBUTING.md      contribution workflow
```

## Shield example

```python
from ayorai.shield.engine import ShieldEngine

shield = ShieldEngine(allowed_tools={"search"})
decision = shield.inspect_text("Please summarize this report.")
print(decision.allowed, decision.risk.value)
print(shield.authorize_tool("search").allowed)
```

## Roadmap
- [Issue #8 — Community roadmap](https://github.com/Ayorinha/ayorai/issues/8)
- [Issue #17 — External validation](https://github.com/Ayorinha/ayorai/issues/17)

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