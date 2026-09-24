# AYORAI — Applied AI Engineering & AI Safety

**AYORAI · Applied Intelligence** is Anderson Leon Ayora's engineering laboratory for building **governed agentic AI systems** with reproducible execution, RAG, MCP/tool governance, auditability and security controls.

The repository is designed to demonstrate the engineering path from **AI prototype → governed system → tested production workflow**.

## What this portfolio demonstrates

- **Agentic systems:** deterministic planning, routing and specialized agents.
- **AI Safety:** prompt-injection defenses, policy gates and auditable decisions.
- **RAG:** retrieval interfaces with explicit ranking and deterministic behavior.
- **MCP & tool governance:** controlled interfaces for tools and external context.
- **Production engineering:** Python packaging, automated tests, Ruff, pre-commit, GitHub Actions and CodeQL.
- **Enterprise orientation:** traceability, least-privilege boundaries, synthetic/authorized data and explicit security scope.

## Architecture

```text
Request
  ↓
Safety / Policy Gate
  ↓
Planner
  ↓
Agent Router
  ├── Research
  ├── Analysis
  ├── Security
  └── Review
  ↓
Memory / RAG / MCP / Governed Tools
  ↓
Output Safety Check
  ↓
Audit Event
  ↓
Result
```

The architecture intentionally separates **decision-making, execution and auditability** so each boundary can be tested independently.

## Engineering tracks

| Track | Real-world purpose | Evidence in the repository |
|---|---|---|
| Agent orchestration | Route a request to the appropriate specialist | Planner, router and governed pipeline |
| AI Safety | Reject unsafe or instruction-injection patterns | SafetyGuard, PolicyEngine and regression tests |
| Auditability | Record security decisions and execution events | Immutable AuditEvent + AuditLog |
| RAG | Retrieve relevant enterprise knowledge deterministically | Retriever interface + in-memory implementation |
| Tool governance | Register and invoke approved capabilities | ToolRegistry + permission tests |
| MCP boundary | Define controlled context/tool adapters | MCP interfaces and tests |
| Quality engineering | Prevent regressions before delivery | Pytest, Ruff, pre-commit and CI |
| Security engineering | Detect defects and risky changes early | CodeQL, security policy and threat-model documentation |

## Engineering work in progress

The repository also contains focused development tracks for:

- **Safety evaluation:** adversarial text corpus, detection/blocking metrics and regression reporting.
- **AYORAI Hunter:** issue → task specification → confidence/risk gate, intentionally read-only in its current MVP.
- **Offline OCR API:** document extraction without requiring a cloud OCR dependency.
- **Governed automation:** future sandboxed execution with explicit human approval gates.

These tracks are kept separate from the stable foundation until their validation and review are complete.

## Why the project is structured this way

The objective is not to present a generic chatbot. AYORAI models the engineering concerns that appear when AI moves into environments where **security, traceability, data boundaries and predictable behavior** matter.

Every new capability should have:

1. a concrete use case;
2. a defined trust boundary;
3. automated tests;
4. documented limitations;
5. a reproducible quality gate;
6. review before integration.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pip check
python -m ruff check .
python -m pytest -q
```

Optional local hooks:

```bash
python -m pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## Security scope

AYORAI is an engineering research/portfolio project, not a security certification or antivirus product. Security claims are limited to the documented implementation, configuration, test corpus and methodology.

Use synthetic, public or explicitly authorized data.

## Portfolio positioning

**Applied AI · Agentic Systems · RAG · AI Safety · Intelligent Automation · Python**

Built by **Anderson Leon Ayora — AYORAI · Applied Intelligence**.

