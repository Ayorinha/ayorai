# AYORAI — Agentic Intelligence, AI Safety & Hunter

AYORAI is an applied AI engineering framework for modular agentic systems with explicit orchestration, safety controls, memory, RAG, MCP and tool governance.

## AYORAI Hunter

Hunter is the autonomous engineering layer: it turns a GitHub issue into a structured task specification using an OpenAI Responses API model, with confidence and risk gates before implementation is attempted.

Current MVP flow:

```text
GitHub Issue → Hunter → Task Specification → Risk/Confidence Gate → Engineer (next phase)
```

The MVP is intentionally read-only against target repositories. Code execution, branch creation and PR delivery are planned as the next sandboxed phase.

### Run locally

```bash
export OPENAI_API_KEY="..."
python -m ayorai.hunter.cli "https://github.com/OWNER/REPO/issues/123" --json
```

### Run inside GitHub

The repository includes `.github/workflows/hunter-smoke.yml`, a manual GitHub Actions workflow. Add `OPENAI_API_KEY` as a repository Actions secret, then run the workflow and provide a public issue URL. GitHub supplies `GITHUB_TOKEN` for read-only issue access.

## Engineering goals
- deterministic agent contracts
- multi-agent orchestration
- prompt-injection and policy defenses
- auditable execution context
- retrieval and tool interfaces without vendor lock-in
- automated tests and CI
- safe autonomous software engineering

## Architecture
```text
User → Safety Guard → Planner → Router → Specialized Agents
                                      ├─ Research
                                      ├─ Analyst
                                      ├─ Security
                                      ├─ Hunter
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
- `src/ayorai/hunter` — autonomous task analysis
- `tests` — automated tests

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

## Status
Hunter MVP added on `feature/ayorai-hunter-mvp`. The next phase will add sandboxed repository execution, test loops, branch/commit/PR tooling and human approval gates.

## Author
Anderson Leon Ayora — AYORAI · Applied Intelligence
