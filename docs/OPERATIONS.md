# AYORAI Shield Operations Baseline

## Deployment principles

- Pin application and model versions.
- Record configuration and policy versions.
- Keep security logs separate from mutable application state where practical.
- Protect signing keys and deployment credentials.
- Test rollback before production use.
- Never treat a green CI run as proof of production security.

## Observability

Track at minimum:

- policy decisions;
- blocked/reviewed high-impact actions;
- tool authorization failures;
- provenance verification failures;
- policy promotion events;
- model/provider failures;
- latency and resource metrics;
- security evaluation regressions.

Avoid logging secrets or unnecessary sensitive payloads.

## Incident response

For a suspected compromise:

1. stop or isolate affected high-impact actions;
2. preserve relevant audit evidence;
3. identify affected policy/model/configuration versions;
4. revoke compromised credentials;
5. roll back to the last known-good policy/configuration;
6. reproduce the failure in a controlled test;
7. add a regression case;
8. document the remediation.

## Adaptive-defense operations

New rules or threat intelligence should enter quarantine first.

```
External evidence
      ↓
Quarantine
      ↓
Validation
      ↓
Security review
      ↓
Explicit promotion
      ↓
Active policy
```

No external feed should have direct write authority over active security policy.
