# AYORAI Shield Evaluation Plan

## Principle
A security system is credible when its defenses are measured against adaptive attacks and its safety/usability trade-offs are visible.

## Layers
1. Unit tests: injection variants, obfuscation, multilingual attacks, tool authorization, malformed arguments, memory poisoning and output exfiltration.
2. Scenario tests: malicious web page, poisoned RAG document, compromised MCP tool, compromised agent, malicious memory and high-impact action.
3. Public benchmarks: AgentDojo, AgentDyn and applicable garak probes.
4. Adaptive attacker: payload mutation, tool-description abuse, indirect injection, memory manipulation and authorization probing.
5. Regression: every discovered attack becomes a permanent test.

## Metrics
- ASR: attack success rate
- BTS: benign task success
- FPR: false-positive rate
- UCR: unauthorized call rate
- DER: data-exfiltration rate
- APR: attack propagation rate
- ACR: audit completeness
- RRS: recovery success

Security evaluation must not optimize blocking alone; legitimate task completion and over-defense must be reported.

## Reproducibility
Record model/version, policy version, tools, benchmark version, attack corpus hash, configuration, seeds where applicable, runtime, date, raw results and limitations.

## Publication standard
No security percentage without a defined denominator, test corpus, configuration and reproducible artifact.
