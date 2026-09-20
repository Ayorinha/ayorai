# Contributing to AYORAI

AYORAI is an open-source engineering project focused on agentic AI, AI safety, RAG, MCP governance and auditable execution.

## Ways to contribute

- implement an issue
- review a pull request
- improve tests
- improve documentation
- propose security improvements
- participate in GitHub Discussions

## Development flow

1. Pick or open an issue.
2. Create a feature branch.
3. Implement the change with tests.
4. Run the local quality gate.
5. Open a pull request.
6. Wait for GitHub Actions and review feedback.
7. Merge only after validation.

## Local quality gate

Run the same checks used by CI:

```bash
python -m pip install -e ".[dev]"
python -m pip check
python -m ruff check .
python -m pytest -q
```

Install the optional pre-commit hooks:

```bash
python -m pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## Branch hygiene

Keep branches focused and based on the current `main`. Before merging older work, compare the branch with `main` and resolve divergence deliberately.

## Security contributions

Security research must stay within authorized scope. Do not test systems, repositories or accounts you do not own or that have not explicitly authorized the activity.

See SECURITY.md before reporting a vulnerability.
