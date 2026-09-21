# AYORAI Shield Security Architecture

## 1. Security objective

Protect an agentic application from attacks that exploit the interaction between:

- model reasoning;
- untrusted natural language;
- retrieved documents and web content;
- memory;
- tools and MCP;
- identity and delegated authority;
- multi-agent communication;
- application state.

Shield follows a **zero-trust-for-agents** model: every boundary is explicit and every high-impact transition is policy checked.

## 2. Control planes

### A. Provenance plane

Every untrusted artifact should carry provenance metadata:

- source;
- origin;
- retrieval timestamp;
- trust classification;
- content hash;
- tenant/session scope;
- transformation history.

The security engine should be able to distinguish *instructions* from *data* and preserve that distinction through the agent pipeline.

### B. Contextual defense plane

A single string denylist is insufficient. Shield should evaluate:

- direct and indirect prompt injection;
- instruction/data boundary violations;
- goal hijacking;
- suspicious tool intent;
- privilege escalation;
- data-exfiltration intent;
- memory poisoning;
- cross-agent instruction laundering.

### C. Authorization plane

Every tool invocation should be evaluated against:

- agent identity;
- user/delegator identity;
- requested capability;
- resource scope;
- arguments;
- sensitivity;
- current risk;
- session state;
- provenance of the instruction that caused the call.

### D. Action plane

Actions are classified by impact:

| Class | Example | Default control |
|---|---|---|
| Read | retrieve public document | allow if scoped |
| Internal read | access protected enterprise data | policy + identity |
| Write | modify non-critical data | policy + audit |
| External side effect | send message / submit form | policy + confirmation |
| High impact | financial/admin/security action | explicit approval |

## 3. Multi-agent containment

Agents must not inherit authority merely because another agent requested an action.

A future capability token should contain:

- issuer;
- subject agent;
- delegated capability;
- resource scope;
- maximum impact;
- expiration;
- nonce;
- parent delegation;
- policy version.

Delegation must be narrow and auditable.

## 4. Memory security

Persistent memory is treated as hostile state.

Required controls:

- namespace isolation;
- tenant/session separation;
- provenance;
- integrity verification;
- retention limits;
- sensitive-data classification;
- poisoning detection;
- rollback/quarantine.

## 5. MCP security

MCP/tool servers are treated as external security boundaries.

Required controls:

- positive tool allowlists;
- typed argument schemas;
- no arbitrary shell by default;
- server identity;
- credential isolation;
- per-tool permissions;
- execution timeout;
- output validation;
- complete audit trail.

## 6. Fail-safe behavior

When the risk engine cannot establish sufficient authority or provenance, Shield should prefer:

```
ALLOW  -> low impact + sufficient evidence
REVIEW -> ambiguous/high impact
DENY   -> unauthorized or strongly malicious
QUARANTINE -> suspicious persistent state
```

The implementation must avoid presenting heuristic scores as cryptographic guarantees.

## 7. Important limitation

The current repository is a research foundation. Authenticated identity, sandbox enforcement, persistent tamper-evident logging and comprehensive adversarial evaluation remain required before production security claims are appropriate.
