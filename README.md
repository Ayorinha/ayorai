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

See [docs/shield.md](docs/shield.md) and [docs/threat-model.md](docs/threat-model.md) for the security model and current boundaries.

## Engineering goals
- deterministic agent contracts
- multi-agent orchestration
- prompt-injection and policy defenses
- auditable execution context
- retrieval and tool interfaces without vendor lock-in
- automated tests and CI
- reproducible security evaluation

## Architecture

```text
User → Shield → Planner → Router → Specialized Agents
          │                         ├─ Research
          │                         ├─ Analyst
          │                         ├─ Security
          │                         └─ Reviewer
          └→ Policy / Tool / MCP / Memory Controls
                    ↓
                 Audit → Result
```

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
tests/               automated unit and integration-style tests
pyproject.toml       package metadata and development tooling
SECURITY.md          vulnerability reporting and security guidance
CONTRIBUTING.md      contribution workflow
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

Supported Python versions are **3.11, 3.12 and 3.13**.

## Shield example

```python
from ayorai.shield.engine import ShieldEngine

shield = ShieldEngine(allowed_tools={"search"})

decision = shield.inspect_text("Please summarize this report.")
print(decision.allowed, decision.risk.value)

tool_decision = shield.authorize_tool("search")
print(tool_decision.allowed)
```

The Shield example is deterministic and local; it does not call an external LLM.

## Roadmap

The community roadmap is tracked through real project work:

- [Community roadmap issue #8](https://github.com/Ayorinha/ayorai/issues/8) — contribution tracks across agents, AI safety, RAG, MCP and security research.
- [External validation issue #17](https://github.com/Ayorinha/ayorai/issues/17) — adversarial evaluation, benchmark evidence, operational validation and independent assurance.

See [docs/community-roadmap.md](docs/community-roadmap.md).

## Status

AYORAI is an actively developed alpha framework. Production deployment still requires deployment-specific identity, authentication, durable audit storage and adversarial evaluation.

## License

MIT. See [LICENSE](LICENSE).

## Author

Anderson Leon Ayora — AYORAI · Applied Intelligence
