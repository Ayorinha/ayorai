# Security Architecture

AYORAI treats every agent boundary as a policy boundary.

## Request path

1. Runtime receives a task.
2. SafetyGuard validates the input.
3. The planner creates a deterministic execution plan.
4. The router selects an explicit agent mode.
5. Tool and MCP adapters enforce allowlists.
6. The result is validated before leaving the runtime.
7. AuditLog records policy decisions.

## Security properties

- least privilege for tools
- deterministic policy decisions
- explicit trust boundaries
- auditable decisions
- testable controls
- dependency monitoring
- static analysis through CodeQL

## Not yet production-complete

The project still needs authenticated tool adapters, persistent tamper-resistant audit storage, adversarial evaluation suites, and deployment-specific identity controls before it should be considered production security infrastructure.
