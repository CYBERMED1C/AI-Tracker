# AI Security Intelligence Dashboard

A source-linked learning dashboard for AI engineers and security teams. It highlights actionable AI ecosystem vulnerabilities, U.S. AI policy, major frontier-model changes, and noteworthy security projects—without collecting targets or scanning internet infrastructure.

<!-- dashboard:updated:start -->
> [!IMPORTANT]
> Treat this as a dated informational snapshot, not as a substitute for vendor advisories or your own asset inventory. Open an item's source and verify its publication date before taking action.
>
> **Dashboard health:** ✅ Status as of October 1, 2026
>
> **Last updated:** October 1, 2026
>
> **Last added:**
> - **CVE-2025-62593** · Added October 1, 2026 — Ray-Project Ray Code Injection Vulnerability. [Details](#top-5-ai-security-advisories)
> - **Introducing GPT-6.1 Sol** · Added October 1, 2026 — Meet GPT-6.1 Sol: near-Astra intelligence for coding, computer use, and professional work at one-fifth of Astra’s standard API input and output token…. [Details](#major-frontier-model-updates)
> - **Introducing GPT-6 Sol and Luna** · Added October 1, 2026 — Meet GPT-6 Sol and Luna, two models that bring frontier intelligence to everyday work with different balances of capability and cost. [Details](#major-frontier-model-updates)
> - **Disrupting a coordinated model-distillation campaign** · Added October 1, 2026 — Learn how OpenAI disrupted a campaign to extract protected model reasoning and is strengthening defenses against adversarial distillation. [Details](#major-ai-security-news-and-projects)
>
> See the complete [update history](CHANGELOG.md).
<!-- dashboard:updated:end -->

## Top 5 AI security advisories

Ranked by known exploitation, EchelonGraph risk, exploit evidence, severity, and recency. Results are limited to vulnerabilities that match widely used AI/ML frameworks, serving stacks, orchestration tools, or model infrastructure.

<!-- dashboard:advisories:start -->
| Priority | Advisory | Severity | Published | Source |
| --- | --- | --- | --- | --- |
| 100/100 | [CVE-2026-64849: MLflow Server-Side Request Forgery Vulnerability](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | KNOWN EXPLOITED | 2026-08-19 | CISA KEV |
| 100/100 | [CVE-2025-62593: Ray-Project Ray Code Injection Vulnerability](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | KNOWN EXPLOITED | 2026-08-17 | CISA KEV |
| 95/100 | [CVE-2026-27966: Langflow is a tool for building and deploying AI-powered agents and workflows](https://echelongraph.io/pulse/CVE-2026-27966) | CRITICAL | 2026-02-26 | EchelonGraph |
| 76/100 | [CVE-2026-54745: Kubeflow Pipelines enables users to build and deploy portable, scalable machine learning workflows](https://echelongraph.io/pulse/CVE-2026-54745) | CRITICAL | 2026-08-28 | EchelonGraph |
| 76/100 | [CVE-2026-44182: Jupyter Enterprise Gateway launches remote Jupyter Notebook kernels across distributed clusters like Apache Spark, Kubernetes, and Docker Swarm](https://echelongraph.io/pulse/CVE-2026-44182) | CRITICAL | 2026-06-03 | EchelonGraph |
<!-- dashboard:advisories:end -->

## Latest 3 AI.gov executive orders

These are the three most recent entries in the Executive Orders section of AI.gov, linked to the authoritative order.

<!-- dashboard:orders:start -->
| Executive order | Date | Source |
| --- | --- | --- |
| [Promoting Advanced AI Innovation and Security](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/) | 2026-06-02 | AI.gov |
| [Ensuring a National Policy Framework for AI](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/) | 2025-12-11 | AI.gov |
| [Launching the Genesis Mission](https://www.whitehouse.gov/presidential-actions/2025/11/launching-the-genesis-mission/) | 2025-11-24 | AI.gov |
<!-- dashboard:orders:end -->

## Major frontier-model updates

Only official announcements involving leading model families are eligible: OpenAI GPT/Codex, Anthropic Claude, Google Gemini/Gemma, Meta Llama, Mistral/Mixtral, DeepSeek, xAI Grok, Microsoft Phi, Amazon Nova, Cohere Command, and Alibaba Qwen. Routine product posts are excluded.

<!-- dashboard:models:start -->
| Major model update | What changed | Date | Official source |
| --- | --- | --- | --- |
| [Gemini 4 Argon: our next era of frontier intelligence](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) | Stylized promotional blog key art graphic with modern editorial branding and the text "Gemini 4 Argon" | 2026-09-30 | Google DeepMind |
| [Introducing GPT-6.1 Sol](https://openai.com/index/introducing-gpt-6-1-sol) | Meet GPT-6.1 Sol: near-Astra intelligence for coding, computer use, and professional work at one-fifth of Astra’s standard API input and output token prices. | 2026-09-29 | OpenAI |
| [Introducing Claude Sonnet 5.5](https://www.anthropic.com/claude-sonnet-5-5) | A clear upgrade over Sonnet 5 that runs 30% faster and costs up to 30% less for most work. | 2026-09-28 | Anthropic |
| [Introducing GPT-6 Sol and Luna](https://openai.com/index/introducing-gpt-6-sol-and-luna) | Meet GPT-6 Sol and Luna, two models that bring frontier intelligence to everyday work with different balances of capability and cost. | 2026-09-22 | OpenAI |
| [Introducing Claude Opus 5.5](https://www.anthropic.com/claude-opus-5-5) | Opus 5.5 performs at the level of Claude Fable 5.1 on most work and costs 40% less to run than Opus 5. | 2026-09-22 | Anthropic |
<!-- dashboard:models:end -->

## Major AI security news and projects

Official government notices, lab publications, and releases from established AI-security projects.

<!-- dashboard:news:start -->
| News / project | Why it matters | Date | Source |
| --- | --- | --- | --- |
| [Disrupting a coordinated model-distillation campaign](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign) | Learn how OpenAI disrupted a campaign to extract protected model reasoning and is strengthening defenses against adversarial distillation. | 2026-09-30 | OpenAI |
| [v0.17.0](https://github.com/NVIDIA/garak/releases/tag/v0.17.0) | What's Changed New features EU AI Act Mapping by @erickgalinkin in #2094 This new mapping provides reference tags to surface and group probes results that relate to various categories of risk called out in the EU AI Act. Improved plugins F… | 2026-09-09 | garak |
| [v0.1.12](https://github.com/trailofbits/fickling/releases/tag/v0.1.12) | Security Fix MLAllowlist shadowing ( 41ce7cb ). Thanks to @reapermunky for the report! ( GHSA-cffv-grgg-g429 ) This fix makes MLAllowlist functional again, and opt-in as originally intended. If you need to scan ML pickles with an import al… | 2026-06-26 | Fickling |
| [v0.8.8](https://github.com/protectai/modelscan/releases/tag/v0.8.8) | Bug fixes | 2026-02-18 | ModelScan |
| [DevDay 2026 Recap](https://openai.com/index/devday-2026-recap) | Explore more than 20 announcements from OpenAI DevDay 2026, including GPT-6 Astra, ChatGPT, Codex, APIs, security, and new tools for builders. | 2026-09-29 | OpenAI |
<!-- dashboard:news:end -->

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

<!-- dashboard:health:start -->
- ✅ **EchelonGraph** — 179 AI-related records
- ✅ **CISA KEV** — 2 AI-related records
- ✅ **GitHub Advisories** — 2 AI-related records
- ✅ **AI.gov** — 3 executive orders
- ✅ **OpenAI** — 30 feed entries
- ✅ **Anthropic** — 5 feed entries
- ✅ **Google DeepMind** — 20 feed entries
- ✅ **Meta AI** — 3 feed entries
- ✅ **Microsoft AI** — 10 feed entries
- ✅ **NIST** — 0 feed entries
- ✅ **ModelScan** — 10 feed entries
- ✅ **garak** — 10 feed entries
- ✅ **Fickling** — 10 feed entries
<!-- dashboard:health:end -->

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
