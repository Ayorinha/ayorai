# AI Security Research Landscape — 2026

This document is a living research map for AYORAI Shield. It does not claim affiliation, endorsement or superiority. New findings should become a threat-model update, test, benchmark, control or documented limitation.

## United States

- **NIST:** agent identity/authorization, adversarial ML, AI security controls and multi-agent security overlays.
- **Carnegie Mellon / SEI / CyLab:** AI security incident response and scientific foundations for autonomous cyber defense.
- **MIT CSAIL:** contextual and deterministic defenses for agentic AI, plus autonomous cyber-security research.
- **Stanford:** authenticated delegation, agent identity, authorization, accountability and least-privilege access.

## United Kingdom

- **NCSC / GCHQ:** Cyber Shield research direction for federated agents, trusted communication, coordinated detection/response and safe autonomous cyber defense. NCSC also emphasizes threat modeling, dependency security, monitoring and incident response for agentic AI.

## European Union

- **ENISA:** multilayer AI cybersecurity, AI threat landscape and standardization.
- **ETH Zürich:** AgentDojo dynamic prompt-injection evaluation and AI security research.
- **Oxford:** AI cybersecurity spanning security of AI, AI for security and AI-enabled threats.
- **Cambridge:** agent transparency and safety evidence.

## Canada

- **Canadian Centre for Cyber Security / CSE:** frontier-AI cyber-risk guidance.
- **NRC / Canadian AI Safety Institute:** international testing of autonomous AI systems across nine languages and cybersecurity tasks.

## Australia

- **Australian Signals Directorate / Australian Cyber Security Centre:** secure adoption of agentic AI and agentic AI harness security, emphasizing least privilege, monitoring, audit and human oversight.

## Singapore

- **Cyber Security Agency of Singapore / GovTech / IMDA:** AI Agents Sandbox and agentic-AI security research.
- CSA/FAR.AI: agentic-AI discussion paper covering new attack surfaces and shared ecosystem responsibility.

## Japan

- **NICT:** integrated AI/communication and cybersecurity R&D, including AI-enabled cybersecurity and next-generation cryptography/privacy.

## South Korea

- **KISA:** AI security threat response manual and AI red-team activity covering AI-specific threat classification, diagnosis, scenarios and mitigations.

## China

- **Tsinghua:** secure/robust AI, privacy-preserving and distributed LLM research.
- **Shanghai Jiao Tong:** AI agent security governance.
- **Nanjing University SecLab:** AI-system security, intelligent-agent defense, fuzzing, vulnerability mining and AI-assisted software security.

## Open research ecosystems

- **AgentDojo:** dynamic environment for prompt-injection attacks/defenses.
- **AgentDyn:** open-ended dynamic benchmark for real-world agent security.
- **garak:** LLM vulnerability probing.
- **OWASP AI Agent Security:** practical agent controls.
- **OWASP MCP Security:** MCP-specific attack surface and controls.

## Research synthesis for Shield

Across these ecosystems, recurring technical requirements are:

1. **Identity and delegated authority** — an agent's ability to reason must remain separate from its ability to act.
2. **Contextual deterministic controls** — security cannot rely only on static prompt filters.
3. **Least privilege and scoped tools** — permissions should be narrow, explicit and revocable.
4. **Untrusted-content boundaries** — web, RAG, memory and tool output must not become implicit authority.
5. **Federated multi-agent trust** — agents need explicit identity and communication boundaries.
6. **Transactionality and reversibility** — high-impact operations should be staged, verified and recoverable.
7. **Continuous adversarial evaluation** — static benchmarks are insufficient; adaptive and open-ended testing is required.
8. **Operational harness security** — the software connecting models to tools and data is a critical security boundary.
9. **Multilingual evaluation** — defenses must be evaluated across languages and modalities.
10. **Evidence and assurance** — security claims require reproducible artifacts, denominators and limitations.

## Sources

- NIST — https://csrc.nist.gov/pubs/other/2026/02/05/accelerating-the-adoption-of-software-and-ai-agent/ipd
- NIST — https://www.nist.gov/publications/summary-analysis-responses-request-information-regarding-security-considerations-ai
- MIT CSAIL — https://www.csail.mit.edu/event/securing-agentic-ai-contextual-security-and-beyond
- CMU CyLab — https://cylab.cmu.edu/research/cyber-autonomy-initiative/index.html
- Stanford — https://digitaleconomy.stanford.edu/project/loyal-agents/authentication-for-ai-agents-privacy-and-security/
- NCSC — https://www.ncsc.gov.uk/blogs/cyber-shield-the-path-to-an-agentic-ai-future-for-cyber-defence
- ENISA — https://www.enisa.europa.eu/publications/multilayer-framework-for-good-cybersecurity-practices-for-ai
- ETH Zürich / AgentDojo — https://www.research-collection.ethz.ch/items/21acec58-727b-46a8-9570-3ec6815ac9f1
- Canada NRC — https://www.nrc.canada.ca/en/research-development/products-services/technical-advisory-services/ai-safety-responsible-ai
- Australia ACSC — https://www.cyber.gov.au/about-us/view-all-content/news/asd-releases-new-guidance-on-the-agentic-ai-harnesses
- Singapore CSA — https://www.csa.gov.sg/resources/publications/securing-agentic-ai-a-discussion-paper/
- Japan NICT — https://www.nict.go.jp/en/press/2026/07/31-1.html
- South Korea KISA — https://www.kisa.or.kr/401/form?lang_type=KO&page=1&postSeq=3712
- Nanjing University SecLab — https://seclab.nju.edu.cn/
