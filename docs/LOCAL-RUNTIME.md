# AYORAI Shield Local Runtime Strategy

## Objective

Reduce unnecessary dependence on external model APIs while preserving the deterministic security boundary.

## Target architecture

```
Event
  ↓
Local normalization
  ↓
Local semantic guard (optional)
  ↓
Deterministic risk engine
  ↓
Policy engine
  ├─ allow
  ├─ review
  └─ isolate
  ↓
Deep analysis only when required
```

## BitNet integration status

BitNet is **not part of the current production security boundary**.

A future experiment may evaluate Microsoft BitNet embedding models as a local semantic signal for:

- similarity to known attack patterns;
- paraphrase detection;
- retrieval/classification;
- low-latency triage.

A future local BitNet language model may also be evaluated for contextual security analysis.

Neither model should directly authorize irreversible actions.

## Evaluation requirements

Before enabling a local model in the security path, compare against the current baseline using the same corpus and report:

- precision;
- recall;
- F1;
- false-positive rate;
- false-negative rate;
- P50/P95 latency;
- memory;
- CPU;
- throughput;
- failure behavior when the model is unavailable.

## Failure policy

If the local model is unavailable, the deterministic policy layer must continue to enforce controls. A missing model must not silently disable authorization.

## Privacy objective

Local inference can reduce the amount of sensitive content sent to external providers, but deployment teams remain responsible for local storage, logs, model files, telemetry and host security.

## Status

This document defines an architecture and evaluation plan. It does not claim that BitNet is currently integrated.
