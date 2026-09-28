# AYORAI Shield — Security Claims

## Purpose

This document defines what the project currently claims, what is experimental, and what is explicitly out of scope. Claims are tied to the repository version, configuration, test corpus and evaluation methodology.

## Current claims

- The project implements deterministic policy and safety controls for agentic workflows.
- Tool and MCP access can be governed by explicit allowlists and policy checks.
- Execution can retain auditable context and security-relevant provenance.
- Security-sensitive learning is treated as untrusted evidence until validated and explicitly promoted.
- The repository includes automated tests and static analysis intended to catch regressions in the implemented controls.
- The architecture is designed to reduce the blast radius of compromised or manipulated agents.

## Experimental claims

The following require empirical evaluation before stronger claims are made:

- resistance to previously unseen prompt-injection techniques;
- robustness against multi-step and multi-agent attacks;
- effectiveness of semantic detection models;
- comparative performance against external benchmarks;
- production-scale latency, throughput and resource consumption;
- effectiveness of local inference, including future BitNet integration.

## Explicit non-claims

AYORAI Shield does not currently claim to be:

- an antivirus;
- a complete EDR/XDR platform;
- a malware sandbox;
- a SIEM/SOAR replacement;
- a complete identity or key-management system;
- immune to prompt injection or adversarial manipulation;
- secure against all vulnerabilities;
- a replacement for deployment-specific security controls or independent security assessment.

## Evidence standard

A security claim should have:

1. a precise scope;
2. a reproducible test or benchmark;
3. documented inputs and expected outcomes;
4. failure cases;
5. versioned evidence;
6. limitations and known gaps.

Until those conditions are met, the claim remains a design objective rather than a demonstrated property.
