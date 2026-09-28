# AYORAI Shield Evaluation Plan

## Goal

Measure security behavior rather than infer it from architecture.

## Baseline corpus

Maintain a versioned corpus containing safe and adversarial examples. Every release should report the corpus version.

## Required scenarios

- direct prompt injection;
- indirect prompt injection;
- goal hijacking;
- unauthorized tool invocation;
- malicious tool metadata;
- memory poisoning;
- retrieval poisoning;
- sensitive-data exfiltration;
- privilege escalation;
- cross-agent trust abuse;
- malformed requests;
- policy ambiguity.

## Metrics

For classification or detection:

- precision;
- recall;
- F1;
- false-positive rate;
- false-negative rate.

For runtime behavior:

- P50 latency;
- P95 latency;
- throughput;
- memory;
- CPU;
- external API calls.

For security operations:

- audit completeness;
- provenance verification success;
- policy-promotion traceability;
- rollback success.

## Comparative experiments

When a new detector, model or policy is introduced:

1. freeze the baseline corpus;
2. run baseline;
3. run candidate;
4. compare identical metrics;
5. inspect regressions;
6. publish limitations;
7. only then update security claims.

## External validation

The project intends to evaluate applicable public agent-security benchmarks and research probes, including AgentDojo and related adversarial evaluation work. Results must be reported with exact versions, configurations and limitations.

## Reproducibility

Experiments should record:

- commit SHA;
- corpus version;
- model/version;
- configuration;
- hardware;
- software environment;
- command;
- result artifact.

A benchmark without this metadata should not be treated as reproducible evidence.
