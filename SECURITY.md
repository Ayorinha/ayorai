# Security Policy

## Scope

AYORAI is an experimental open-source framework for agentic AI, retrieval, tool governance, and AI safety controls.

## Reporting a vulnerability

Please do not disclose exploitable vulnerabilities in a public issue.

Use GitHub's private vulnerability reporting/security advisory workflow when available. Include:
- affected component and version
- reproducible steps
- security impact
- suggested mitigation, if known

## Security design principles

AYORAI follows:
1. explicit tool allowlists
2. deterministic policy gates
3. input/output validation
4. auditable execution metadata
5. least-privilege tool access
6. tests for prompt-injection patterns

Security controls are not a substitute for deployment-specific threat modeling.
