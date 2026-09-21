# AYORAI Shield Validation Gates

Every security-sensitive change should pass the following lifecycle.

```
Code
  ↓
Unit tests
  ↓
Integration tests
  ↓
Adversarial tests
  ↓
Static analysis
  ↓
Security review
  ↓
Evidence
  ↓
Documentation
  ↓
Staging validation
  ↓
Monitoring
  ↓
Rollback validation
```

## Gate 1 — Deterministic correctness

Run:

- pytest;
- Ruff;
- contract tests;
- negative tests for authorization boundaries.

## Gate 2 — Security regression

Every security control should have at least one:

- allowed case;
- blocked case;
- malformed-input case;
- boundary case.

## Gate 3 — Adversarial evaluation

Maintain a versioned corpus covering:

- direct prompt injection;
- indirect injection;
- tool abuse;
- memory poisoning;
- retrieval poisoning;
- data exfiltration;
- privilege escalation;
- multi-agent attacks.

Measure at minimum:

- true positives;
- false positives;
- false negatives;
- precision;
- recall;
- F1;
- latency P50/P95 where applicable.

## Gate 4 — Supply-chain/security tooling

CI should include:

- static analysis;
- dependency review/update automation;
- CodeQL;
- least-privilege workflow permissions.

## Gate 5 — Evidence before claims

Do not promote a design objective to a security claim until the relevant test or benchmark produces reproducible evidence.

## Gate 6 — Deployment-specific validation

Production deployments must add their own:

- identity controls;
- secrets/key management;
- network controls;
- observability;
- incident response;
- backup and rollback;
- configuration validation.

## Gate 7 — Human approval

High-impact or irreversible actions require explicit authorization outside the model's free-form reasoning.
