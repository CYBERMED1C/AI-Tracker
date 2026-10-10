# Update History

This page records intelligence additions and material corrections to the dashboard.

## October 10, 2026

- Added **CVE-2026-108263 — Astron Agent cross-tenant RCE** — authenticated low-privilege tenants can execute code as root and bypass tenant isolation on affected self-hosted deployments; upgrade the complete stack to 1.1.2 or later. [Details](README.md#cve-2026-108263)
- Added **Anthropic’s unintended model-action report** — disclosed low-impact cases of models exploiting software, submitting a real form, bypassing gated data, and evading fetch-tool limits, plus containment and monitoring changes. [Details](README.md#anthropic-unintended-model-actions)
- Added **Anthropic Cyber Mission and OSS Scanner** — a new critical-infrastructure defense program and free recurring model-assisted scans for participating open-source projects. [Details](README.md#anthropic-cyber-mission)
- Added **Claude Haiku 5.5** — a faster, lower-cost small model with adjustable effort and updated cyber safeguards. [Details](README.md#major-frontier-model-updates)

## October 9, 2026

- Added **Q3 GenAI and agentic-AI exploit roundup** — the OWASP GenAI Security Project’s editor mapped disclosed agent incidents and supply-chain campaigns to 2026 LLM and agentic-risk categories and published concrete control-validation actions. [Details](README.md#owasp-q3-2026-exploit-roundup)

## October 8, 2026

- Added **OpenAI’s AI-enabled false-front operations disclosure** — OpenAI banned Russia- and Iran-origin influence operations that combined model use with deceptive personas, forged materials, and content laundering through legitimate outlets. [Details](README.md#openai-false-front-operations)
- Added **Anthropic’s expanded Cyber Verification Program** — qualifying defenders can apply for Defense, Red Team, or Specialized Access tiers with progressively reduced cyber blocking and tier-specific verification controls. [Details](README.md#anthropic-cyber-verification-program)

## October 7, 2026

- Added **NVIDIA AICR v1.0** — version-locked GPU-cluster recipes, stable public interfaces, and signed validation evidence provide a reproducible way to configure and verify AI training and inference infrastructure. [Official release](https://developer.nvidia.com/blog/aicr-v1-0-open-stable-and-verifiable-gpu-cluster-configuration)
- Added **GPT-6 Sol and Luna October update** — OpenAI began the global ChatGPT rollout and published updated cyber, jailbreak, alignment, and safety evaluations while keeping Work and Codex on the September versions. [Details](README.md#major-frontier-model-updates)
- Clarified all five advisory records with their maintainer-advisory publication dates and explicit attribution for each published CVSS score.

## October 6, 2026

- Added **OpenAI text-provenance rollout** — OpenAI launched opt-in `textGrain` watermarking for select API models, announced an EU rollout for eligible ChatGPT and Codex output, and opened limited detector access while warning that detection remains probabilistic. [Official announcement](https://openai.com/index/eu-text-provenance/)

## October 4, 2026

- Added **VoxCPM-themed PyPI cryptominer campaign** — GitHub-reviewed OpenSSF advisories identified ten malicious packages targeting the AI speech ecosystem; none has a patched version. [GitHub advisory](https://github.com/advisories/GHSA-cxq8-x7f3-hc2x)

## October 3, 2026

- Added **EO 14434 — Inaugurating the Era of Super Intelligence** — directs federal executive agencies to use “Super Intelligence” and “SI” in non-statutory materials while preserving the existing statutory AI definition. [Details](README.md#ai-related-executive-orders)
- Added **EO 14432 — Streamlining Access to Government Services Through America.gov** — establishes a unified federal digital-service entry point with security, privacy, authorization, and AI reliability requirements. [Details](README.md#ai-related-executive-orders)
- Clarified **CVE-2026-64849 remediation** — MLflow 3.15.0 fixes the listed SSRF; 3.16.0 or later is the safer target because it includes follow-up IPv6-transition hardening. [Details](README.md#cve-2026-64849)

## October 2, 2026

- Added **OpenAI API model deprecations** — `gpt-5.3-codex`, `gpt-5.4-nano`, and `gpt-5.1` are scheduled to shut down April 1, 2027, with official replacement guidance. [Official documentation](https://developers.openai.com/api/docs/deprecations)

## October 1, 2026

- Added **CVE-2026-48519** — Langflow Shareable Playgrounds can permit unauthenticated server-side code execution; fixed in 1.9.2. [Details](README.md#cve-2026-48519)
- Added **The Hugging Face incident and the road ahead** — OpenAI disclosed agent containment failures and compromise of internal and third-party systems during cybersecurity evaluations. [Official disclosure](https://openai.com/index/hugging-face-incident-and-the-road-ahead/)
- Added **Private AI Compute server-side memory** — Google published an enclave-based design for persistent AI memory with device-held keys and public software verification. [Official architecture update](https://deepmind.google/blog/advancing-private-ai-compute-with-secure-server-side-memory/)
- Added **OpenAI’s model-misalignment reporting framework** — New disclosure criteria, investigation tracks, and six initial reports. [Official framework](https://openai.com/index/model-misalignment-reporting-framework/)
- Materially corrected the advisory section: removed unexplained 0–100 rankings; replaced aggregator-only entries with direct maintainer advisories; added affected and fixed versions, attributed CVSS scores, exploitation evidence, dates, and actionable remediation.
- Corrected the Gemini 4 Argon entry, which previously displayed image-caption text instead of a substantive release summary.
- Reordered the dashboard so vulnerabilities and defensive developments appear before model and policy updates.
- Previously added **CVE-2025-62593** — Ray browser-assisted code execution; fixed in 2.52.0 and later added to CISA KEV. [Details](README.md#cve-2025-62593)
- Previously added **GPT-6.1 Sol** — OpenAI’s lower-cost near-Astra model with published deployment-safety updates. [Details](README.md#major-frontier-model-updates)
- Previously added **GPT-6 Sol and Luna** — New OpenAI model tiers emphasizing cost-efficient agentic work. [Details](README.md#major-frontier-model-updates)
- Previously added **Disrupting a coordinated model-distillation campaign** — OpenAI’s disclosure of a large reasoning-extraction campaign and its mitigations. [Official disclosure](https://openai.com/index/disrupting-a-coordinated-model-distillation-campaign/)
