# AI Security Intelligence Dashboard

A source-linked learning dashboard for AI engineers and security teams. It highlights actionable AI ecosystem vulnerabilities, U.S. AI policy, major frontier-model changes, and noteworthy security projects—without collecting targets or scanning internet infrastructure.

> [!IMPORTANT]
> Treat this as a dated informational snapshot, not as a substitute for vendor advisories or your own asset inventory. Open an item's source and verify its publication date before taking action.
>
> **Last updated:** October 1, 2026
>
> **Last added:** Update-history tracker — find it in [CHANGELOG.md](CHANGELOG.md).

## Top 5 AI security advisories

Ranked by known exploitation, EchelonGraph risk, exploit evidence, severity, and recency. Results are limited to vulnerabilities that match widely used AI/ML frameworks, serving stacks, orchestration tools, or model infrastructure.

| Priority | Advisory | Severity | Published | Source |
| --- | --- | --- | --- | --- |
| 100/100 | [CVE-2026-64849: MLflow webhook test endpoint SSRF](https://echelongraph.io/pulse/CVE-2026-64849) | CRITICAL | 2026-08-17 | EchelonGraph |
| 95/100 | [CVE-2026-27966: Langflow CSV Agent prompt injection to RCE](https://echelongraph.io/pulse/CVE-2026-27966) | CRITICAL | 2026-02-26 | EchelonGraph |
| 76/100 | [CVE-2026-54745: Kubeflow Pipelines unauthenticated SSRF](https://echelongraph.io/pulse/CVE-2026-54745) | CRITICAL | 2026-08-28 | EchelonGraph |
| 76/100 | [CVE-2026-44182: Jupyter Enterprise Gateway YAML injection](https://echelongraph.io/pulse/CVE-2026-44182) | CRITICAL | 2026-06-03 | EchelonGraph |
| 76/100 | [CVE-2026-44181: Jupyter Enterprise Gateway template injection](https://echelongraph.io/pulse/CVE-2026-44181) | CRITICAL | 2026-06-03 | EchelonGraph |

## Latest 3 AI.gov executive orders

These are the three most recent entries in the Executive Orders section of AI.gov, linked to the authoritative order.

| Executive order | Date | Source |
| --- | --- | --- |
| [Promoting Advanced Artificial Intelligence Innovation and Security](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/) | 2026-06-02 | AI.gov |
| [Ensuring a National Policy Framework for Artificial Intelligence](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/) | 2025-12-11 | AI.gov |
| [Launching the Genesis Mission](https://www.whitehouse.gov/presidential-actions/2025/11/launching-the-genesis-mission/) | 2025-11-24 | AI.gov |

## Major frontier-model updates

Only official announcements involving leading model families are eligible: OpenAI GPT/Codex, Anthropic Claude, Google Gemini/Gemma, Meta Llama, Mistral/Mixtral, DeepSeek, xAI Grok, Microsoft Phi, Amazon Nova, Cohere Command, and Alibaba Qwen. Routine product posts are excluded.

| Major model update | What changed | Date | Official source |
| --- | --- | --- | --- |
| [Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) | A phased frontier model for long-horizon software engineering, enterprise knowledge work, and defensive cybersecurity; initially rolling out to trusted cyber defenders. | 2026-09-30 | Google DeepMind |
| [Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5) | A faster, lower-cost Sonnet with major agentic-coding gains, stronger long-horizon work and image understanding, plus frontier-model cyber safeguards. | 2026-09-28 | Anthropic |
| [Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) | Anthropic's leading model for agentic coding, computer use, and knowledge work, with lower cost, faster output, stronger prompt-injection resistance, and expanded safeguards. | 2026-09-22 | Anthropic |
| [Gemini 3.8 Live and Live Extended Thinking](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-8-live-gemini-3-8-live-extended-thinking/) | Production voice models with real-time visual grounding, parallel tool use, and extended reasoning for complex background tasks. | 2026-09-15 | Google DeepMind |
| [GPT-6 Astra](https://openai.com/index/safety-overview-gpt-6-astra/) | OpenAI's most capable broadly deployed model, with advances in coding, research, computer use, multi-step work, and critical-level cybersecurity capability with strengthened safeguards. | 2026-09-03 | OpenAI |

## Major AI security news and projects

Official government notices, lab publications, and releases from established AI-security projects.

| News / project | Why it matters | Date | Source |
| --- | --- | --- | --- |
| [Anthropic: Detecting and countering misuse of AI](https://www.anthropic.com/threat-intelligence-report-september-2026) | Threat-intelligence case studies describe how malicious use of Claude evolved during 2026 and the operations Anthropic disrupted. | 2026-09-10 | Anthropic |
| [garak v0.17.0](https://github.com/NVIDIA/garak/releases/tag/v0.17.0) | Adds EU AI Act risk mapping and improves agent, exfiltration, package-hallucination, Ollama, and OpenAI-compatible endpoint probes and detectors. | 2026-09-09 | NVIDIA garak |
| [Anthropic alignment assessment of cybersecurity incidents](https://www.anthropic.com/research/alignment-assessment-cybersecurity-incidents) | An assessment of four incidents in which evaluation models obtained unauthorized live-internet access, including containment and alignment lessons for AI evaluators. | 2026-09-09 | Anthropic |
| [OpenAI Daybreak for Frontline Defenders](https://openai.com/index/daybreak-for-frontline-defenders/) | A $1 billion initiative for subsidized access, training, support, and partnerships intended to put frontier cyber capabilities in defenders' hands. | 2026-09-03 | OpenAI |
| [NIST seeks comment on AI for Cybersecurity Framework 2.0](https://www.nist.gov/news-events/news-updates/topic/2753736) | NIST released a draft publication on using AI for Cybersecurity Framework 2.0 analysis and reporting and requested public feedback. | 2026-08-19 | NIST |

## Trusted government and standards sources

| Source | Use it for |
| --- | --- |
| [AI.gov](https://www.ai.gov/) | White House AI strategy, executive orders, and federal initiatives |
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | Govern, map, measure, and manage AI risk |
| [NIST AI Resource Center](https://airc.nist.gov/) | AI RMF playbooks, profiles, and evaluation resources |
| [CISA AI](https://www.cisa.gov/ai) | U.S. critical-infrastructure AI guidance and cyber advisories |
| [NSA AI Security Center](https://www.nsa.gov/Press-Room/AI-Security-Center/) | National-security guidance for secure AI adoption |
| [MITRE ATLAS](https://atlas.mitre.org/) | Adversarial tactics and techniques against AI systems |
| [ENISA AI cybersecurity](https://www.enisa.europa.eu/topics/artificial-intelligence) | European threat landscape and security guidance |
| [UK NCSC AI](https://www.ncsc.gov.uk/section/technology/artificial-intelligence) | Secure AI development and deployment guidance |

## Useful AI security tools

| Tool | Purpose |
| --- | --- |
| [EchelonGraph CVE Pulse](https://echelongraph.io/pulse) | CVE intelligence enriched with KEV, EPSS, vendor advisories, and risk scoring |
| [garak](https://github.com/NVIDIA/garak) | LLM vulnerability scanning and red-team probes |
| [PyRIT](https://github.com/Azure/PyRIT) | Risk identification and red teaming for generative AI |
| [ModelScan](https://github.com/protectai/modelscan) | Scan serialized model files for unsafe code patterns |
| [Fickling](https://github.com/trailofbits/fickling) | Inspect and help secure Python pickle files used by ML models |
| [Giskard](https://github.com/Giskard-AI/giskard) | Test AI models for security, safety, and quality failures |
| [OWASP GenAI Security](https://genai.owasp.org/) | LLM application risks, controls, and testing guidance |
| [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | Framework for large-language-model safety evaluations |

## Source verification

- ✅ **EchelonGraph** — Public CVE API verified during initial build
- ✅ **AI.gov** — Latest executive-order list verified during initial build
- ✅ **Official lab sources** — Current model and security announcements verified during initial build
- ✅ **GitHub project releases** — Curated project releases verified during initial build

## About this dashboard

This public learning resource is designed to help AI engineers and security teams quickly understand important developments from trusted sources. Changes to the dashboard are recorded in [CHANGELOG.md](CHANGELOG.md).

### Ranking and trust policy

- Security advisories come from EchelonGraph, CISA's Known Exploited Vulnerabilities catalog, and GitHub's reviewed Advisory Database.
- Known exploitation outranks theoretical severity. EchelonGraph risk and CVSS provide additional ordering signals.
- Policy comes directly from AI.gov; model changes come from first-party lab feeds.
- Every item must link to its original source. Aggregator-only stories are excluded.
- This project does not perform active scanning, exploit validation, or automated remediation.

## Use notice

This repository is published for viewing and educational reference only. All rights are reserved; no license is granted to reuse, modify, distribute, or republish its code or original content. Linked upstream information remains subject to each source's own terms.
