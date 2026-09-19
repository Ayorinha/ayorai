# AYORAI Threat Model

## Assets

- agent instructions
- retrieved documents
- tool credentials and permissions
- execution history
- model outputs

## Threats

| Threat | Control |
|---|---|
| Prompt injection | SafetyGuard + PolicyEngine |
| Unauthorized tool use | SafeMCPAdapter allowlist |
| Untrusted retrieval | source-aware DocumentChunk |
| Output policy bypass | runtime output enforcement |
| Excessive tool privileges | explicit ToolRegistry/MCP permissions |

## Trust boundaries

User input crosses into the runtime. Retrieval and external tools are treated as untrusted boundaries. Security controls are applied before execution and before returning an agent result.

## Residual risk

The current implementation is a deterministic foundation, not a complete production security system. Future work includes structured provenance, stronger policy evaluation, adversarial evaluations, and authenticated tool adapters.
