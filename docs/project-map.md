# AYORAI Project Map

This document explains the portfolio as a set of engineering problems rather than a list of disconnected demos.

## 1. Governed Multi-Agent Pipeline

**Problem:** A multi-agent application needs deterministic boundaries between planning, routing, specialist execution and review.

**Implementation:** `GovernedPipeline` composes the planner, router and reviewer and returns an `ExecutionContext` containing the execution history.

**Usability:** A team can inspect what happened during a request instead of receiving only an opaque final answer.

**Engineering evidence:** unit tests verify the order of planner → specialist → reviewer execution.

## 2. AI Safety & Policy Guard

**Problem:** Agentic systems can receive instruction-injection attempts through user input or generated content.

**Implementation:** `SafetyGuard` provides deterministic normalization and a policy gate. `PolicyEngine` exposes the same decision boundary as a structured `PolicyDecision`.

**Usability:** Applications can validate content before execution and before returning sensitive output.

**Limitations:** The current guard is intentionally lightweight and pattern-based. It is not a complete prompt-injection defense.

## 3. Auditable Runtime

**Problem:** Enterprise AI workflows need traceability around security decisions.

**Implementation:** `AyoraiRuntime` records input and output policy decisions using immutable `AuditEvent` records.

**Usability:** A caller can inspect the sequence of policy decisions after an execution.

**Engineering evidence:** tests cover both successful execution and rejected input.

## 4. RAG Boundary

**Problem:** Retrieval should be testable independently of a model provider or vector database.

**Implementation:** `Retriever` defines the interface and `InMemoryRetriever` provides a deterministic reference implementation.

**Usability:** Retrieval behavior can be tested before integrating embeddings, a vector store or a production document pipeline.

**Engineering evidence:** tests cover relevance, limits, blank queries and deterministic tie ordering.

## 5. Governed Tools

**Problem:** Agents should not invoke arbitrary capabilities without an explicit registration boundary.

**Implementation:** `ToolRegistry` requires a `ToolSpec` before execution and rejects duplicate or unknown tools.

**Usability:** Tool capabilities are discoverable through `names()` and execution happens through a controlled registry.

## 6. MCP Integration Boundary

**Problem:** Model Context Protocol integrations need a clear abstraction so the core system is not tightly coupled to one server implementation.

**Implementation:** MCP adapters are represented as explicit interfaces, with permission-focused tests in the repository.

**Usability:** An implementation can be replaced without changing the agent contracts.

## 7. Safety Evaluation Suite — development track

**Problem:** A safety claim should be supported by measurable regression cases rather than a single happy-path test.

**Planned evidence:** adversarial corpus, detection/blocking metrics, false-positive tracking and machine-readable reports.

**Status:** maintained as a separate feature branch/PR until validation is complete.

## 8. AYORAI Hunter — development track

**Problem:** Software-engineering agents need a controlled way to turn an issue into an actionable specification.

**Current MVP:** GitHub issue → structured task specification → risk/confidence gate.

**Safety boundary:** the MVP is read-only against target repositories. Repository modification, execution and PR delivery require a future sandbox and explicit approval gates.

## 9. Offline OCR API — development track

**Problem:** Document Intelligence workflows may need local/offline extraction where sending documents to external services is undesirable.

**Target architecture:** document input → local OCR/extraction → normalized result → governed pipeline.

**Status:** kept isolated until its API, tests and dependency boundary are validated.

## Recruiter-facing engineering narrative

AYORAI is intentionally organized around real system boundaries:

**Input safety → planning → routing → specialized execution → retrieval/tools → output safety → audit → CI/security validation.**

That structure maps directly to the skills the portfolio is intended to demonstrate:

**Applied AI · Agentic Systems · RAG · AI Safety · Intelligent Automation · Python · Production Quality.**