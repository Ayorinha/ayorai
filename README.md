# AYORAI — Agentic Intelligence & AI Safety

AYORAI is an applied AI engineering framework for governed agentic systems with explicit orchestration, safety controls, auditability, memory, RAG, MCP and tool governance.

## What the project demonstrates

- deterministic agent contracts and routing
- governed multi-agent execution
- prompt-injection and policy defenses
- auditable input/output decisions
- RAG and MCP integration boundaries
- permission-controlled tools
- adversarial safety regression tests
- CI, CodeQL and dependency governance

## Security model

```
User request
    ↓
Safety Guard
    ↓
Planner
    ↓
Router
    ├── Research Agent
    ├── Analyst Agent
    ├── Security Agent
    └── Reviewer Agent
    ↓
Memory / RAG / MCP / Tools
    ↓
Output Safety Check
    ↓
Audit Event
    ↓
Result
```

The security evaluation separates **detection** from **containment**:

```
DETECTED + BLOCKED       → protected
DETECTED + NOT BLOCKED   → incident
NOT DETECTED + EXECUTED  → critical failure
BENIGN + BLOCKED         → false positive
BENIGN + ALLOWED         → safe
```

This distinction is intentional: a security system must report when an attack is identified and separately report whether containment succeeded.

## Safety evaluation

The deterministic evaluation corpus is maintained in `src/ayorai/safety/evaluation.py` and covered by `tests/test_safety_evaluation.py`.

It measures:

- detection rate
- block rate
- false negatives
- false positives
- incidents
- critical failures

The evaluation is a **text-level adversarial benchmark**. It does not scan, execute or classify real malware and must not be described as a traditional antivirus engine.

## Architecture boundaries

- `src/ayorai/agents` — specialized agents
- `src/ayorai/core` — shared contracts
- `src/ayorai/orchestration` — planning and routing
- `src/ayorai/safety` — detection, policy and audit
- `src/ayorai/memory` — state interfaces
- `src/ayorai/rag` — retrieval interfaces
- `src/ayorai/mcp` — tool/context adapters
- `src/ayorai/tools` — governed tools
- `tests` — automated regression suite
- `.github/workflows` — CI, CodeQL and safety evaluation

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
ruff check .
```

## CI quality gates

Pull requests are expected to pass:

1. Ruff lint checks
2. full pytest suite
3. safety regression evaluation
4. CodeQL analysis

The safety workflow also publishes a machine-readable `safety-report.json` artifact.

## Current status

**AYORAI 0.3.0 — Safety Evaluation & Governance**

The project is designed as a reproducible engineering laboratory: security claims should be tied to explicit test cases, recorded metrics and published evidence rather than broad guarantees.

## Author

Anderson Leon Ayora — AYORAI · Applied Intelligence
