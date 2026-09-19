# AYORAI Safety Evaluation

The safety evaluation suite measures how the current deterministic SafetyGuard
responds to adversarial and benign text inputs.

## Metrics

- BLOCK: malicious case rejected by the guard.
- FAIL: malicious case accepted by the guard (false negative).
- FALSE_POSITIVE: benign case rejected by the guard.
- SAFE: benign case accepted.

Main metric: block_rate = blocked_attacks / malicious_cases * 100.

A false negative is an adversarial pattern that the current policy did not catch.

## Scope

This is a text-policy evaluation. It does not scan files, inspect hashes, run
malware, or claim to detect real computer viruses. The cases are inert strings
and are never executed.

The initial corpus covers prompt injection, jailbreak, instruction extraction,
tool/MCP abuse, RAG poisoning, data exfiltration, multi-agent manipulation,
output manipulation, and benign enterprise-AI tasks.

## Baseline

Run:
python -c "from ayorai.safety.evaluation import run_baseline; print(run_baseline()['metrics'])"

The baseline measures the current rule-based guard; it is not a production
security certification.

## Next iterations

1. Expand the corpus with paraphrases and indirect attacks.
2. Add provenance-aware RAG cases.
3. Add MCP authorization scenarios.
4. Add multi-agent trust-boundary tests.
5. Track metrics across commits.
6. Add regression cases whenever a bypass is discovered.
