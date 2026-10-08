## Live status

🟢 **Operational**

**Last push:** 2026-10-08 17:03 UTC  
**Overall health:** Healthy

---

# AI Security Intelligence Dashboard

A source-linked learning dashboard for AI engineers and security teams. It prioritizes actionable AI ecosystem vulnerabilities and defensive developments, with frontier-model and U.S. policy updates kept secondary.

<!-- dashboard:updated:start -->
> [!IMPORTANT]
> Treat this as a dated informational snapshot, not as a substitute for vendor advisories or your own asset inventory. Open each source and verify that its affected versions and mitigations match your deployment.
>
> **Last added:**
> - **OpenAI disrupted AI-enabled false-front influence operations** · Added October 8, 2026 — OpenAI banned Russia- and Iran-origin operations that combined model use with deceptive media and organizational fronts. [Details](#openai-false-front-operations)
> - **Anthropic expanded the Cyber Verification Program** · Added October 8, 2026 — Verified defenders can apply for tiered access to advanced cyber capabilities with controls matched to defensive, red-team, or specialized work. [Details](#anthropic-cyber-verification-program)
>>
> See the complete [update history](CHANGELOG.md).
<!-- dashboard:updated:end -->

## Current AI security advisories

**Status key:** 🔴 confirmed exploitation · 🟠 public proof of concept; no confirmed in-the-wild exploitation

<!-- dashboard:advisories:start -->
### Triage view

| Product and risk | Exploitation | Affected → target | Immediate action |
| --- | --- | --- | --- |
| [MLflow: webhook SSRF](#cve-2026-64849) | 🔴 CISA KEV | 3.10.0–3.14.x → **3.16.0+** | Patch; restrict Tracking Server; investigate unexpected webhook activity |
| [Ray: browser-assisted RCE](#cve-2025-62593) | 🔴 CISA KEV | <2.52.0 → **2.52.0+** | Patch; enable token auth; investigate unauthorized jobs |
| [Langflow: public-flow RCE](#cve-2026-48519) | 🟠 Public PoC | ≤1.9.1 → **1.9.2+** | Patch; disable or restrict public sharing |
| [Kubeflow Pipelines: pre-auth SSRF](#cve-2026-54745) | 🟠 Public PoC | Frontend ≤2.16.0 → **2.17.0+** | Patch; block untrusted frontend access and sensitive egress |
| [Jupyter Enterprise Gateway: manifest injection](#cve-2026-44182) | 🟠 Public PoC | ≤3.2.3 → **3.3.0+** | Patch; constrain kernel launchers and Kubernetes permissions |

---

<a id="cve-2026-64849"></a>
### 🔴 MLflow webhook SSRF

**Severity:** High — 8.6/10 (CVSS 3.1; source: maintainer advisory)  
**Vulnerability ID:** CVE-2026-64849  
**Published:** August 2, 2026

An attacker who can reach the MLflow Tracking Server can use webhook redirects to read responses from internal, loopback, or cloud-metadata services.

- **Exposed if:** MLflow 3.10.0–3.14.x is reachable by an untrusted user or network.
- **Do now:** Upgrade to **3.16.0 or later**; version 3.15.0 fixes this CVE, while 3.16.0 adds follow-up IPv6-transition hardening. Restrict and authenticate the Tracking Server.
- **Look for:** Unexpected webhook tests, access to metadata addresses, or requests to internal-only services.
- **Exploitation:** CISA added this CVE to KEV on **August 19, 2026**, confirming in-the-wild exploitation.
- **Evidence:** [Maintainer advisory](https://github.com/mlflow/mlflow/security/advisories/GHSA-7gwp-5pfp-969j) · [CISA KEV entry](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-64849)

<a id="cve-2025-62593"></a>
### 🔴 Ray browser-assisted remote code execution

**Severity:** Critical — 9.4/10 (CVSS 4.0; source: maintainer advisory)  
**Vulnerability ID:** CVE-2025-62593  
**Published:** November 26, 2025

A malicious webpage can combine DNS rebinding with weak browser-request checks to reach Ray job APIs and execute code on a workstation or network-adjacent node.

- **Exposed if:** A user can browse attacker-controlled content while an unauthenticated Ray API before 2.52.0 is reachable.
- **Do now:** Upgrade to **2.52.0 or later**, enable token authentication, and isolate dashboard/job APIs.
- **Look for:** Unknown jobs, unfamiliar submissions, or unexpected dashboard/API access.
- **Exploitation:** CISA added this CVE to KEV on **August 17, 2026**, confirming in-the-wild exploitation.
- **Evidence:** [Maintainer advisory](https://github.com/ray-project/ray/security/advisories/GHSA-q279-jhrf-cc6v) · [CISA alert](https://www.cisa.gov/news-events/alerts/2026/08/17/cisa-adds-one-known-exploited-vulnerability-catalog)

<a id="cve-2026-48519"></a>
### 🟠 Langflow public-flow remote code execution

**Severity:** Critical — 9.6/10 (CVSS 3.1; source: maintainer advisory)  
**Vulnerability ID:** CVE-2026-48519  
**Published:** May 27, 2026

A public Shareable Playground can accept attacker-controlled custom Python node code through its public build endpoint and execute it on the server.

- **Exposed if:** Public-flow sharing is enabled on Langflow 1.9.1 or earlier.
- **Do now:** Upgrade to **1.9.2 or later**; disable or restrict public sharing until patched.
- **Look for:** Unexpected public build requests or unfamiliar custom node code.
- **Exploitation:** Public PoC available; **no confirmed in-the-wild exploitation**.
- **Evidence:** [Maintainer advisory](https://github.com/langflow-ai/langflow/security/advisories/GHSA-v5ff-9q35-q26f)

<a id="cve-2026-54745"></a>
### 🟠 Kubeflow Pipelines pre-auth SSRF and HTTP smuggling

**Severity:** Critical — 10.0/10 (CVSS 3.1; source: maintainer advisory)  
**Vulnerability ID:** CVE-2026-54745  
**Published:** July 12, 2026

The frontend `/_proxy/` route can forward unauthenticated requests to cluster-internal services—even when `ENABLE_AUTHZ=true`—putting cloud credentials and internal APIs at risk.

- **Exposed if:** An untrusted user can reach `kfp-frontend` 2.16.0 or earlier.
- **Do now:** Upgrade to **2.17.0 or later**; block untrusted access and egress to metadata or sensitive internal destinations.
- **Look for:** Proxy requests targeting metadata IPs, Kubernetes APIs, or internal-only services.
- **Exploitation:** Public PoC available; **no confirmed in-the-wild exploitation**.
- **Evidence:** [Maintainer advisory](https://github.com/kubeflow/pipelines/security/advisories/GHSA-gqww-5pj5-8fq7)

<a id="cve-2026-44182"></a>
### 🟠 Jupyter Enterprise Gateway Kubernetes manifest injection

**Severity:** Critical — 10.0/10 (CVSS 4.0; source: maintainer advisory)  
**Vulnerability ID:** CVE-2026-44182  
**Published:** June 3, 2026

Attacker-controlled `KERNEL_*` values can alter rendered Kubernetes manifests, create privileged workloads, and potentially compromise notebook worker nodes or the cluster.

- **Exposed if:** Untrusted users can launch kernels through Enterprise Gateway 3.2.3 or earlier.
- **Do now:** Upgrade to **3.3.0 or later**; reduce service-account rights and enforce admission controls against privileged pods and host mounts.
- **Look for:** Unexpected privileged pods, extra Kubernetes resources, host mounts, or unusual kernel environment values.
- **Exploitation:** Reproducible PoC available; **no confirmed in-the-wild exploitation**.
- **Evidence:** [Maintainer advisory](https://github.com/jupyter-server/enterprise_gateway/security/advisories/GHSA-cfw7-6c5v-2wjq) · [3.3.0 release notes](https://github.com/jupyter-server/enterprise_gateway/releases/tag/v3.3.0)
<!-- dashboard:advisories:end -->

## AI security research, defensive tools, and significant releases

<!-- dashboard:news:start -->
<a id="openai-false-front-operations"></a>
### OpenAI disrupted AI-enabled false-front influence operations — October 8, 2026

OpenAI banned two influence operations—one originating in Russia and one in Iran—that used its models alongside conventional tactics to support deceptive front organizations and personas. The disclosure shows how AI can improve the scale, fluency, and internal workflows of influence campaigns without replacing the human infrastructure behind them; defenders should monitor for coordinated synthetic personas, forged materials, and content laundering through legitimate outlets. [Official disclosure](https://openai.com/index/disrupting-ai-enabled-false-front-operations/)

<a id="anthropic-cyber-verification-program"></a>
### Anthropic expanded trusted access for defensive cyber work — October 6, 2026

Anthropic consolidated Project Glasswing and its Cyber Verification Program into Defense, Red Team, and Specialized Access tiers, giving verified defenders progressively fewer cyber blocks while retaining stricter controls for high-risk systems. Security teams should review eligibility, authorization boundaries, and data-retention requirements before using the program for vulnerability validation or red teaming. [Official announcement](https://www.anthropic.com/news/cyber-verification-program)

<a id="nvidia-aicr-v1"></a>
### NVIDIA released AICR v1.0 for verifiable AI cluster configuration — October 6, 2026

NVIDIA AI Cluster Runtime 1.0 provides version-locked, validated recipes for GPU-accelerated Kubernetes clusters, stable CLI/REST/Go and artifact contracts, and signed validation evidence. AI infrastructure teams can use it to reproduce compatible configurations and detect drift across training and inference platforms including Kubeflow, Slurm, Dynamo, and NIM. [Official release](https://developer.nvidia.com/blog/aicr-v1-0-open-stable-and-verifiable-gpu-cluster-configuration)

<a id="openai-text-provenance"></a>
### OpenAI launched opt-in text watermarking and limited detector access — October 5, 2026

OpenAI made its `textGrain` watermark available as an opt-in for select API models, announced an EU rollout for eligible ChatGPT and Codex output, and opened detector applications to approved researchers and expert organizations. Teams should treat detection as a probabilistic provenance signal—not proof of authorship or authenticity—because short, constrained, edited, or translated text can evade detection and false positives remain possible. [Official announcement](https://openai.com/index/eu-text-provenance/)

<a id="voxcpm-typosquat-cryptominers"></a>
### OpenSSF identified VoxCPM-themed PyPI cryptominer packages — October 3, 2026

GitHub-reviewed OpenSSF advisories linked ten packages to the `2026-10-voxeval` campaign: `caoxiltts`, `voxcpmruntime`, `voxcpmui4`, `voxcpmkit`, `voxcpmintel`, `voxcpmeval`, `voxcpmui3`, `voxel-tts`, `voxcpmtts3`, and `voxeval`. Each has no patched version and deploys a coin miner. AI and speech teams should remove these packages, rebuild affected environments, and use the official OpenBMB package name `voxcpm`; package indicators are intentionally non-clickable. [GitHub advisory](https://github.com/advisories/GHSA-cxq8-x7f3-hc2x) · [Campaign example](https://github.com/advisories/GHSA-xmhj-hj4f-c924) · [Official VoxCPM repository](https://github.com/OpenBMB/VoxCPM)
<!-- dashboard:news:end -->

## Major frontier-model updates

<!-- dashboard:models:start -->
| Major model or deployment update | What changed and why engineers should care | Announced | Official source |
| --- | --- | --- | --- |
| OpenAI API model deprecations | OpenAI deprecated `gpt-5.3-codex`, `gpt-5.4-nano`, and `gpt-5.1` with shutdown scheduled for April 1, 2027. Teams should inventory pinned model IDs and plan migrations to `gpt-6-sol` or `gpt-6-luna` as recommended. | 2026-10-01 | [OpenAI API documentation](https://developers.openai.com/api/docs/deprecations) |
| Gemini 4 Argon | Google announced a long-horizon frontier model with a 1 million-token limit for software engineering, enterprise work, and autonomous defensive vulnerability patching. Access is initially limited to trusted defenders through Fairwind while Google expands safeguards and pre-release review. | 2026-09-30 | [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) |
| GPT-6.1 Sol | OpenAI released an API and Work/Codex model that approaches Astra on agentic coding, computer use, and professional work at substantially lower cost. Its system-card addendum classifies it as Critical for cybersecurity capability and applies Astra’s safeguards stack. | 2026-09-29 | [OpenAI](https://openai.com/index/introducing-gpt-6-1-sol/) |
| Claude Sonnet 5.5 | Anthropic released a faster, more efficient Sonnet with large agentic-coding gains and new cyber safeguards, fallbacks, and reasoning-extraction defenses. Engineers should review the `between_tools` migration requirement when thinking is disabled. | 2026-09-28 | [Anthropic](https://www.anthropic.com/claude-sonnet-5-5) |
| GPT-6 Sol and Luna — October update | OpenAI began a global ChatGPT rollout: Sol serves Plus, Pro, Business, and Enterprise, while Luna serves Free and Go. The new system card classifies both as High—but below Critical—for cybersecurity and biological/chemical capability, reports stronger jailbreak resistance than GPT-5.6, and notes that Work and Codex remain on the September versions. | 2026-10-07 | [OpenAI release](https://openai.com/index/gpt-6-for-everyone/) · [System card](https://deploymentsafety.openai.com/gpt-6-october) |
<!-- dashboard:models:end -->

## AI-related executive orders

These are executive orders—not memoranda, fact sheets, or speeches—and are linked to the official text.

<!-- dashboard:orders:start -->
| Executive order | Signed | Practical relevance | Official source |
| --- | --- | --- | --- |
| **EO 14434 — Inaugurating the Era of Super Intelligence** | 2026-09-29 | Directs executive agencies to use “Super Intelligence” and “SI” in non-statutory materials while retaining the existing statutory AI definition unless later changed. It does not alter prior regulations, presidential actions, contracts, grants, or historical documents. | [White House](https://www.whitehouse.gov/presidential-actions/2026/09/inaugurating-the-era-of-super-intelligence/) |
| **EO 14432 — Streamlining Access to Government Services Through America.gov** | 2026-09-29 | Directs GSA to establish America.gov as a unified federal-services entry point using Login.gov, with data minimization, secure authentication, auditable authorization, and accuracy, reliability, and transparency requirements for AI used by the service. | [White House](https://www.whitehouse.gov/presidential-actions/2026/09/streamlining-access-to-government-services-through-america.gov/) |
| **EO 14409 — Promoting Advanced Artificial Intelligence Innovation and Security** | 2026-06-02 | Directs federal cyber-defense prioritization and a classified process for assessing advanced model cyber capabilities and designating covered frontier models, alongside voluntary secure pre-release access. | [White House](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/) |
<!-- dashboard:orders:end -->

## Reference resources

### Quick tips for AI risk research

| Resource | Best use | Quick tip |
| --- | --- | --- |
| [MIT AI Risk Repository](https://airisk.mit.edu/risks) | Threat modeling, risk scoping, and control-gap analysis | Filter by cause, lifecycle timing, domain, and subdomain to turn a broad AI concern into a testable scenario. Taxonomy placement is context—not proof of exploitation. |
| [CVE Artificial Intelligence Working Group](https://www.cve.org/Media/News/item/news/2024/10/15/New-CVE-Artificial-Intelligence-Working-Group) | Understanding how the CVE Program is approaching AI vulnerabilities | Use its official guidance to decide whether an issue may be CVE-able. It is a policy source, not an operational advisory feed. |
| [AI Vulnerability Database (AVID)](https://avidml.org/database/) | Finding documented AI failure modes, reports, and vulnerabilities | Start with AVID for discovery, then open the cited maintainer, vendor, CVE, or original evidence before acting or publishing. |
| [AI Incident Database](https://incidentdatabase.ai/) | Learning from real-world AI harms and near harms | Hunt for recurring failure patterns, then verify the underlying reports and separate the incident date from the publication date. |
| [arXiv](https://arxiv.org/) | Tracking emerging AI-security research | Treat papers as preprints unless confirmed otherwise. Look for released code, independent reproduction, and primary-source corroboration before elevating a claim. |

### Government, standards, and knowledge bases

| Source | Use it for |
| --- | --- |
| [CISA Known Exploited Vulnerabilities](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Confirmed exploitation and federal remediation direction |
| [NVD](https://nvd.nist.gov/) | CVE records and attributed CVSS data |
| [GitHub Advisory Database](https://github.com/advisories) | Maintainer and ecosystem security advisories |
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | AI governance and risk-management guidance |
| [NIST AI Resource Center](https://airc.nist.gov/) | AI RMF playbooks, profiles, and evaluation resources |
| [CISA AI](https://www.cisa.gov/ai) | Critical-infrastructure AI guidance |
| [NSA AI Security Center](https://www.nsa.gov/Press-Room/AI-Security-Center/) | National-security guidance for secure AI adoption |
| [MITRE ATLAS](https://atlas.mitre.org/) | Adversarial tactics and techniques against AI systems |
| [OWASP GenAI Security](https://genai.owasp.org/) | Application risks and defensive controls |

### Defensive tools

| Tool | Purpose |
| --- | --- |
| [garak](https://github.com/NVIDIA/garak) | LLM vulnerability scanning and red-team probes |
| [PyRIT](https://github.com/Azure/PyRIT) | Risk identification and red teaming for generative AI |
| [ModelScan](https://github.com/protectai/modelscan) | Serialized-model artifact scanning |
| [Fickling](https://github.com/trailofbits/fickling) | Inspection and analysis of Python pickle files used by ML systems |
| [Giskard](https://github.com/Giskard-AI/giskard) | AI model security, safety, and quality testing |
| [Inspect AI](https://github.com/UKGovernmentBEIS/inspect_ai) | Framework for model safety evaluations |

## Verification notes

This review opened the underlying maintainer advisories, CISA’s official `cisagov/kev-data` mirror, OpenSSF malware records, official release notes and system cards, vendor security disclosures, laboratory announcements, and White House orders. It distinguishes confirmed exploitation from public proof-of-concept material and attributes each published CVSS score to its source. CISA’s website feed blocked direct retrieval, so KEV claims were cross-checked against CISA’s official GitHub mirror plus the relevant maintainer advisory; no section was left unverified.

## About this dashboard

This public learning resource helps AI engineers and security teams quickly understand important developments from primary and authoritative sources. It does not perform active scanning, exploit validation, or automated remediation. Changes are recorded in [CHANGELOG.md](CHANGELOG.md).

## Use notice

This repository is published for viewing and educational reference only.
