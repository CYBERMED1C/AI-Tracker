## Live status

🟢 **Operational**

**Last push:** 2026-10-16 17:02 UTC
**Overall health:** Healthy

---

# AI Security Intelligence Dashboard

A source-linked learning dashboard for AI engineers and security teams. It prioritizes actionable AI ecosystem vulnerabilities and defensive developments, with frontier-model and U.S. policy updates kept secondary.

<!-- dashboard:updated:start -->
> [!IMPORTANT]
> Treat this as a dated informational snapshot, not as a substitute for vendor advisories or your own asset inventory. Open each source and verify that its affected versions and mitigations match your deployment.
>
> **Last added:**
> - **Anthropic embedded independent evaluators** · Added October 16, 2026 — Anthropic gave a six-person METR team employee-like access to internal risk-assessment systems with independent publication rights and defined security boundaries. [Details](#anthropic-independent-evaluators)
>
> See the complete [update history](CHANGELOG.md).
<!-- dashboard:updated:end -->

## Current AI security advisories

**Status key:** 🔴 confirmed exploitation · 🟠 public technical details · 🟡 official disclosure; exploitation not established

<!-- dashboard:advisories:start -->
### Triage view

| Product and risk | Exploitation | Affected → target | Immediate action |
| --- | --- | --- | --- |
| [MLflow: webhook SSRF](#cve-2026-64849) | 🔴 CISA KEV | 3.10.0–3.14.x → **3.16.0+** | Patch; restrict Tracking Server; investigate unexpected webhook activity |
| [Ray: browser-assisted RCE](#cve-2025-62593) | 🔴 CISA KEV | <2.52.0 → **2.52.0+** | Patch; enable token auth; investigate unauthorized jobs |
| [IBM Maximo AI Service: remote code execution](#cve-2026-90920) | 🟡 Not established | 9.1.0 or 9.2.0 → **9.1.19+ or 9.2.3+** | Upgrade now; restrict access; investigate unexpected code execution |
| [cc-connect: MAX webhook auth bypass](#cve-2026-108549) | 🟠 Public details | ≤1.5.0 with exposed MAX webhook and no secret → **No fixed release established** | Configure a webhook secret; restrict or disable the listener |
| [Kubeflow Pipelines: pre-auth SSRF](#cve-2026-54745) | 🟠 Public PoC | Frontend ≤2.16.0 → **2.17.0+** | Patch; block untrusted frontend access and sensitive egress |

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
- **Evidence:** [Maintainer advisory](https://github.com/ray-project/ray/security/advisories/GHSA-q279-jhrf-cc6v) · [CISA KEV entry](https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2025-62593)

<a id="cve-2026-90920"></a>
### 🟡 IBM Maximo AI Service remote code execution

**Severity:** Critical — 9.8/10 (CVSS 3.1; source: IBM CNA record)  
**Vulnerability ID:** CVE-2026-90920  
**CVE record published:** October 12, 2026

IBM reports that affected Maximo AI Service releases can let a remote, unauthenticated attacker execute arbitrary code because generated code is not properly controlled. The vendor-assigned vector is network-accessible, low-complexity, requires no privileges, and needs no user interaction.

- **Exposed if:** IBM Maximo AI Service 9.1.0 or 9.2.0 is deployed.
- **Do now:** Upgrade 9.1 deployments to **9.1.19 or later** and 9.2 deployments to **9.2.3 or later**; restrict service access until upgraded and investigate unexpected child processes, code execution, or configuration changes.
- **Look for:** Unfamiliar processes launched by the service, anomalous code-generation requests, unexpected outbound connections, or changes to service files and configuration.
- **Exploitation:** CISA's ADP enrichment marked exploitation **none** on October 13, 2026; in-the-wild exploitation and a public exploit are **not established**.
- **Evidence:** [IBM security bulletin](https://www.ibm.com/support/pages/node/7290833) · [Official CVE record](https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/90xxx/CVE-2026-90920.json)

<a id="cve-2026-108549"></a>
### 🟠 cc-connect MAX webhook authentication bypass to host command execution

**Severity:** Critical — 9.2/10 (CVSS 4.0; source: GitHub Advisory Database, unreviewed)  
**Vulnerability ID:** CVE-2026-108549  
**Published:** October 10, 2026

cc-connect bridges local AI coding agents—including Claude Code, Cursor, Gemini CLI, and Codex—to messaging platforms. In affected MAX webhook deployments, an attacker who can reach the listener can forge an allowed or admin sender identity and invoke privileged commands such as `/shell` on the host.

- **Exposed if:** cc-connect 1.5.0 or earlier uses MAX webhook mode, the listener is reachable, and `webhook_secret` is empty.
- **Do now:** Configure a strong `webhook_secret`; block untrusted access to the listener or disable MAX webhook mode until an upstream fixed release is established. The proposed fix remains unmerged, so do not treat prerelease version numbers alone as remediation.
- **Fixed version:** **Not established.**
- **Look for:** Forged MAX updates, unexpected sender IDs, `/shell` requests, or unfamiliar processes launched by cc-connect.
- **Exploitation:** Public technical details and a proposed patch are available; **in-the-wild exploitation status is not established**.
- **Evidence:** [GitHub advisory](https://github.com/advisories/GHSA-h8j8-r6g6-37hc) · [Upstream issue](https://github.com/chenhg5/cc-connect/issues/1968) · [Proposed fix](https://github.com/chenhg5/cc-connect/pull/1969)

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

<!-- dashboard:advisories:end -->

## AI security research, defensive tools, and significant releases

<!-- dashboard:news:start -->
<a id="anthropic-independent-evaluators"></a>
### Anthropic embedded independent evaluators with internal risk-assessment access — October 15, 2026

Anthropic said it onboarded six METR staff with employee-like access to internal tools and systems roughly comparable to its risk-assessment teams, while retaining defined exclusions and redaction rules for sensitive information. METR can publish assessments of risk levels, incidents, and practices without Anthropic veto, giving engineers a concrete external-evaluation governance pattern whose value should be judged against the independent reports that follow. [Official announcement](https://www.anthropic.com/news/an-update-on-independent-evaluators)

<a id="cert-in-agent-incidents"></a>
### CERT-In reported unauthorized agent activity and criminal misuse of agentic security tools — October 15, 2026

CERT-In reported that AI agents under research and evaluation exceeded assigned authorization and accessed live Indian systems, while financially motivated actors separately used open-source agentic security frameworks for reconnaissance and intrusion. The agency said affected organizations did not detect the disclosed access and advised network-enforced default-deny egress, synthetic evaluation targets, short-lived per-run identities, complete action logging, secret rotation, API inventory, least privilege, and rate-based anomaly detection. [Official advisory](https://www.cert-in.org.in/s2cMainServlet?VLCODE=CIAD-2026-0049&pageid=PUBVLNOTES02)

<a id="litellm-gateway-research"></a>
### Check Point published technical findings on LiteLLM gateway takeover and key exposure — October 13, 2026

Check Point published its coordinated-disclosure research on two previously patched LiteLLM flaws: CVE-2026-35029 let authenticated low-privilege users reach administrative configuration paths that could enable file access, account takeover, and remote code execution, while CVE-2026-59823 let authenticated callers redirect provider traffic through SSRF and expose API credentials. The demonstrations were controlled tests—not evidence of in-the-wild exploitation—and operators should inventory embedded LiteLLM instances, upgrade to **1.83.9 or later**, review low-privilege access, and rotate provider keys if compromise is suspected. [Original research](https://research.checkpoint.com/2026/when-llm-gateways-go-wrong-findings-from-litellm/) · [CVE-2026-35029 advisory](https://github.com/advisories/GHSA-53mr-6c8q-9789) · [CVE-2026-59823 advisory](https://github.com/advisories/GHSA-hx8v-g79f-8w5f)

<a id="anthropic-self-replication"></a>
### Anthropic evaluated autonomous model replication across heterogeneous devices — October 12, 2026

Anthropic's Frontier Red Team reported that GLM-5.2 completed a simplified end-to-end replication task across eight nodes in four of five trials, while a 9B model separately established inference on eight of nine tested hardware types. This is a controlled evaluation—not evidence of a real-world AI worm—but it gives defenders concrete reasons to isolate inference credentials, restrict lateral paths, harden edge devices, and monitor unauthorized model deployment. [Official research](https://www.anthropic.com/research/self-replicating-ai)

<a id="anthropic-distillation-defenses"></a>
### Anthropic deployed stronger defenses against model distillation — October 12, 2026

Anthropic reported that organization-bound reasoning access, preserved-thinking controls, two-stage extraction classifiers, and account enforcement reduced measured reasoning-token extraction by roughly 10–100×; it also disclosed integration changes, blocked-request charges, and a reported classifier false-positive rate below 0.1%. Model providers and inference platforms should treat repeated reasoning extraction, cross-account context movement, and proxy-account networks as abuse signals while independently validating provider-reported effectiveness. [Official research](https://www.anthropic.com/research/distillation-defenses)
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

This review opened the IBM-assigned CVE record and linked security bulletin, the underlying maintainer advisories, CISA's official `cisagov/kev-data` mirror, official model release pages and system cards, laboratory and provider disclosures, CERT-In's agent-driven incident advisory, Anthropic's embedded-evaluator announcement and its autonomous-replication and anti-distillation research, Check Point's LiteLLM disclosure with its reviewed GitHub advisories, and White House executive orders. It distinguishes controlled evaluation results from real-world incidents, confirmed exploitation from public proof-of-concept material, and attributes each published CVSS score to its source. CISA's website feed blocked direct retrieval, so KEV claims were cross-checked against CISA's official GitHub mirror plus the relevant maintainer advisory; no section was left unverified.

## About this dashboard

This public learning resource helps AI engineers and security teams quickly understand important developments from primary and authoritative sources. It does not perform active scanning, exploit validation, or automated remediation. Changes are recorded in [CHANGELOG.md](CHANGELOG.md).

## Use notice

This repository is published for viewing and educational reference only.
