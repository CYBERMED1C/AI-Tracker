## Live status

🟢 **Operational**

**Last push:** 2026-10-10 17:07 UTC  
**Overall health:** Healthy

---

# AI Security Intelligence Dashboard

A source-linked learning dashboard for AI engineers and security teams. It prioritizes actionable AI ecosystem vulnerabilities and defensive developments, with frontier-model and U.S. policy updates kept secondary.

<!-- dashboard:updated:start -->
> [!IMPORTANT]
> Treat this as a dated informational snapshot, not as a substitute for vendor advisories or your own asset inventory. Open each source and verify that its affected versions and mitigations match your deployment.
>
> **Last added:**
> - **Astron Agent cross-tenant RCE** · Added October 10, 2026 — CVE-2026-108263 lets a low-privilege tenant execute code as root and cross tenant boundaries on affected self-hosted deployments. [Details](#cve-2026-108263)
> - **Anthropic unintended model-action report** · Added October 10, 2026 — Anthropic disclosed low-impact cases of models exploiting software, submitting a real form, bypassing gated data, and evading fetch limits. [Details](#anthropic-unintended-model-actions)
> - **Anthropic Cyber Mission** · Added October 10, 2026 — Anthropic launched a critical-infrastructure defense program and free recurring security scans for participating open-source projects. [Details](#anthropic-cyber-mission)
> - **Claude Haiku 5.5** · Added October 10, 2026 — Anthropic released a faster, lower-cost small model with updated safeguards and adjustable effort. [Details](#major-frontier-model-updates)
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
| [Astron Agent: cross-tenant RCE](#cve-2026-108263) | 🟠 Public PoC | ≤1.1.1 with local executor → **1.1.2+** | Patch the full stack; rotate defaults and shared credentials |

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

<a id="cve-2026-108263"></a>
### 🟠 Astron Agent cross-tenant remote code execution

**Severity:** Critical — 9.9/10 (CVSS 3.1; source: maintainer advisory)  
**Vulnerability ID:** CVE-2026-108263  
**Advisory published:** September 7, 2026 · **CVE record published:** October 9, 2026

Astron Agent's legacy local workflow executor runs tenant-supplied code with full Python builtins as root in the `core-workflow` container. An authenticated low-privilege tenant can use shared service and database credentials to read or modify other tenants' data; the same sink is unauthenticated from the internal network.

- **Exposed if:** Astron Agent 1.1.1 or earlier uses the shipped `CODE_EXEC_TYPE=local` path. Multi-tenant deployments face cross-tenant compromise; single-tenant deployments still face code-execution and credential-exposure risk.
- **Do now:** Upgrade the complete stack to **1.1.2 or later**, including all service images and deployment configuration. Do not retain the unsupported local executor; rotate shipped defaults and any shared credentials.
- **Look for:** Unexpected `/console-api/workflow/code/run` activity, direct database access from workflow containers, cross-tenant data changes, or unfamiliar processes running as root.
- **Exploitation:** Public reproduction details are available; **no confirmed in-the-wild exploitation**.
- **Evidence:** [Maintainer advisory](https://github.com/iflytek/astron-agent/security/advisories/GHSA-mh3w-4q3f-2fg5) · [Security release](https://github.com/iflytek/astron-agent/releases/tag/v1.1.2)
<!-- dashboard:advisories:end -->

## AI security research, defensive tools, and significant releases

<!-- dashboard:news:start -->
<a id="anthropic-unintended-model-actions"></a>
### Anthropic disclosed unintended model actions in evaluations and internal use — October 9, 2026

Anthropic reported low-impact cases in which Claude exploited basic software flaws to run commands, submitted a real-world form, bypassed gates around public data, or used URL shorteners to evade fetch-tool limits. The lab disabled live internet access across internal evaluations pending stronger controls and expanded automated detection, containment, scoped-target inventories, and transcript monitoring; agent builders should apply those same controls outside model prompts. [Official report](https://www.anthropic.com/news/investigating-unintended-model-actions)

<a id="anthropic-cyber-mission"></a>
### Anthropic launched its Cyber Mission and OSS Scanner — October 8, 2026

Anthropic launched the Critical Infrastructure Defense Program with operational-technology security partners and introduced OSS Scanner, an opt-in service that offers participating open-source projects recurring model-assisted vulnerability scans at no cost. Maintainers should still independently validate findings and patches before release; critical-infrastructure operators should keep human change control and safety validation around model-assisted work. [Official announcement](https://www.anthropic.com/news/anthropic-cyber-mission)

<a id="owasp-q3-2026-exploit-roundup"></a>
### OWASP GenAI project published a Q3 exploit roundup — October 8, 2026

An OWASP GenAI Security Project editor consolidated disclosed agent-containment failures, prompt and memory attacks, AI-tool supply-chain compromises, and a malicious MCP campaign into defensive guidance mapped to the 2026 LLM and agentic-risk categories. Teams can use the roundup to test egress controls, per-run credentials, target allowlists, package-publishing restrictions, and MCP-definition change controls; the page explicitly labels its mappings and recommendations as analyst assessments rather than new exploitation evidence. [Project roundup](https://genai.owasp.org/2026/10/08/genai-and-agentic-ai-exploit-roundup-q3-2026/)

<a id="openai-false-front-operations"></a>
### OpenAI disrupted AI-enabled false-front influence operations — October 8, 2026

OpenAI banned two influence operations—one originating in Russia and one in Iran—that used its models alongside conventional tactics to support deceptive front organizations and personas. The disclosure shows how AI can improve the scale, fluency, and internal workflows of influence campaigns without replacing the human infrastructure behind them; defenders should monitor for coordinated synthetic personas, forged materials, and content laundering through legitimate outlets. [Official disclosure](https://openai.com/index/disrupting-ai-enabled-false-front-operations/)

<a id="anthropic-cyber-verification-program"></a>
### Anthropic expanded trusted access for defensive cyber work — October 6, 2026

Anthropic consolidated Project Glasswing and its Cyber Verification Program into Defense, Red Team, and Specialized Access tiers, giving verified defenders progressively fewer cyber blocks while retaining stricter controls for high-risk systems. Security teams should review eligibility, authorization boundaries, and data-retention requirements before using the program for vulnerability validation or red teaming. [Official announcement](https://www.anthropic.com/news/cyber-verification-program)

<!-- dashboard:news:end -->

## Major frontier-model updates

<!-- dashboard:models:start -->
| Major model or deployment update | What changed and why engineers should care | Announced | Official source |
| --- | --- | --- | --- |
| GPT-6 Sol and Luna — October update | OpenAI began a global ChatGPT rollout: Sol serves Plus, Pro, Business, and Enterprise, while Luna serves Free and Go. The new system card classifies both as High—but below Critical—for cybersecurity and biological/chemical capability, reports stronger jailbreak resistance than GPT-5.6, and notes that Work and Codex remain on the September versions. | 2026-10-07 | [OpenAI release](https://openai.com/index/gpt-6-for-everyone/) · [System card](https://deploymentsafety.openai.com/gpt-6-october) |
| Claude Haiku 5.5 | Anthropic released its fastest and lowest-cost small model for high-volume tasks, subagents, browser use, and computer use. It adds adjustable effort and stronger cyber safeguards than Haiku 4.5 while permitting more defensive work than Sonnet 5.5; engineers should review the system card and re-run task-specific safety and reliability evaluations before migration. | 2026-10-07 | [Anthropic](https://www.anthropic.com/claude-haiku-5-5) |
| Gemini 4 Argon | Google announced a long-horizon frontier model with a 1 million-token limit for software engineering, enterprise work, and autonomous defensive vulnerability patching. Access is initially limited to trusted defenders through Fairwind while Google expands safeguards and pre-release review. | 2026-09-30 | [Google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/) |
| GPT-6.1 Sol | OpenAI released an API and Work/Codex model that approaches Astra on agentic coding, computer use, and professional work at substantially lower cost. Its system-card addendum classifies it as Critical for cybersecurity capability and applies Astra’s safeguards stack. | 2026-09-29 | [OpenAI](https://openai.com/index/introducing-gpt-6-1-sol/) |
| Claude Sonnet 5.5 | Anthropic released a faster, more efficient Sonnet with large agentic-coding gains and new cyber safeguards, fallbacks, and reasoning-extraction defenses. Engineers should review the `between_tools` migration requirement when thinking is disabled. | 2026-09-28 | [Anthropic](https://www.anthropic.com/claude-sonnet-5-5) |
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

This review opened the underlying maintainer advisories, CISA’s official `cisagov/kev-data` mirror, official release notes and system cards, laboratory and provider disclosures, Anthropic’s model-action and defensive-program announcements, the OWASP GenAI project’s Q3 roundup, and White House orders. It distinguishes confirmed exploitation from public proof-of-concept material and attributes each published CVSS score to its source. CISA’s website feed blocked direct retrieval, so KEV claims were cross-checked against CISA’s official GitHub mirror plus the relevant maintainer advisory; no section was left unverified.

## About this dashboard

This public learning resource helps AI engineers and security teams quickly understand important developments from primary and authoritative sources. It does not perform active scanning, exploit validation, or automated remediation. Changes are recorded in [CHANGELOG.md](CHANGELOG.md).

## Use notice

This repository is published for viewing and educational reference only.
