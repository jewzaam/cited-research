# Visual TOM: Citation-Backed Product Analysis

## Methodology

This analysis was produced using the cited-research methodology where every factual claim traces to a web source visited in-session on 2026-04-15. Seven research dimensions were investigated through parallel discovery agents, followed by direct URL fetching, structured organization into reference files, and independent verification by two audit agents. All sources are numbered in [citations.md](citations.md) and detailed in the [references/](references/) directory.

Two independent review agents — a citation auditor and a consistency reviewer — audited this document with no context from the research conversation. Their reports are in [audit/](audit/).

---

## Executive Summary

Visual TOM (Visual Time Operation Manager) is a workload automation and job scheduling platform developed by Absyss, a French software publisher founded in 1990 and headquartered in Montrouge, France [3][19]. The platform provides cross-platform job scheduling and orchestration across traditional datacenters, hybrid, and cloud environments [1].

Absyss is a small but profitable company — €13.4M revenue with €4.2M net profit (31.59% margin) in FY2024, employing 20-49 people [19]. The company maintains a partner-centric delivery model with 650+ certified colleagues across 20+ service centers spanning France, Europe, Africa, Asia, and India [5].

In the competitive landscape, Visual TOM is positioned as a **Niche Player** in the 2024 Gartner Magic Quadrant for Service Orchestration and Automation Platforms [16] and was one of only 10 vendors included in the 2025 EMA Radar for Workload Automation and Orchestration [17]. The platform competes primarily against BMC Control-M, Broadcom AutoSys, Redwood RunMyJobs/Tidal, Stonebranch UAC, and SMA OpCon.

---

## 1. Product Architecture

Visual TOM uses a client/server architecture with five module families [12]:

### Core Components

| Component | Code | Role |
|---|---|---|
| Enterprise Server | VT-SES | Central repository, scheduling engine, APIs [10] |
| Departmental Server | VT-SDS | Remote site autonomy in distributed architectures [10] |
| Backup Server | VT-SBU | Automatic failover for HA production [10] |
| Agent | VT-CS | Job execution on target platforms [10] |
| Net Agent | VT-CN | Autonomous local repository for remote autonomy [10] |
| XVision GUI | VT-XVI | Graphical interface for design, control, management [10] |

### Hierarchical Model

The system organizes work in four nested levels with configuration inheritance [10]:

```
Domain (top)
  └── Environment (controlled by Engine process)
        └── Application (job grouping with shared constraints)
              └── Job (elementary executable task)
```

Values set at higher levels cascade downward automatically but can be overridden at lower levels [10].

### Communication Ports

| Service | Port | Purpose |
|---|---|---|
| vtmanager | 30000 | Web service [18] |
| tomDBd | 30001 | Agent-to-server [12] |
| REST API | 30002 | Monitoring/management (HTTPS) [14] |
| bdaemon | 30004 | Agent listening [12] |

### Database

PostgreSQL is the backend database [11]. Configuration is managed through `vtom.ini` (server/agent), `vtomapiserver.ini` (API server), and `VTXVision.ini` (GUI) [12].

---

## 2. Platform Support

Visual TOM supports an exceptionally wide range of operating systems [11]:

| OS | Min Version | Server | Agent | GUI |
|---|---|---|---|---|
| Windows Server | > 2008 | ✓ | ✓ | ✓ |
| Linux | Kernel > 2.4.20 | ✓ | ✓ | ✓ |
| HP-UX | ≥ 11.31 | ✓ | ✓ | |
| Solaris | ≥ 5.10 | ✓ | ✓ | |
| AIX | ≥ 5.3 | ✓ | ✓ | |
| IBM i (OS/400) | ≥ 5 | ✓ | ✓ | |
| IBM z (Z/OS) | ≥ 1.11 | ✓ | ✓ | |
| VMS/DECUX | ≥ 7.2 | ✓ | ✓ | |
| GCOS7/GCOS8 | varies | ✓ | ✓ | |
| Mac OS | ≥ 10.15.2 | | | ✓ |

The GCOS7/GCOS8 support for Bull mainframes is notably rare among modern workload automation tools and reflects Absyss's French legacy system heritage [11].

Cloud platform support includes Azure, AWS, and GCP [1], with Docker and Kubernetes for containerized environments [1]. Both agent-based and agentless execution models are supported [1][22].

---

## 3. Key Capabilities

### Job Scheduling

- **Schedule-based:** Days, weeks, months with calendar validation [10]
- **Formula-based:** SNL (Syntax Notation Language) for complex rules (e.g., `test {today=3.day.work.month}`) [10]
- **Cyclic execution:** Permanent restart, time-based intervals, or cron format [10]
- **Frequency limits:** Daily, weekly, monthly, yearly maximum execution counts [10]

### Workflow Orchestration

10 resource/constraint types control job execution including text, weight, stack, date, file, numerical, SAP Event, SGBD, and remote file resources [10]. Four submit unit modes provide flexibility: single agent, multi-agent, backup (sequential fallback), and load balancing [10].

### Managed File Transfer (MFT)

Visual TOM MFT provides natively integrated file transfer [9]:
- **MFT Gateway:** Remote-to-remote transfers with integrated SFTP server
- **MFT Portal:** Browser-based secure exchange for partners ("Dropbox-like")
- **Protocols:** FTP, SFTP, FTPS (PESIT and AS2 in development)
- **Storage:** AWS S3, Azure Blob, GCS, Scaleway, Alibaba OSS, NAS, NFS, SMB, SharePoint, Google Drive

Positioned as a French sovereign alternative to Axway, IBM Sterling, Fortra GoAnywhere, and Progress MOVEit [9].

### Monitoring & Alerting

- REST API for job status monitoring (v6.6.1a+) with token-based auth [14]
- Alarms on schedule deviation, duration, or status with SNMP, email, script actions [10]
- Notification via email, SMS, WhatsApp, Teams, Slack [1]
- SmartView mobile app for iOS/Android [1]
- Integration with Centreon [14] and Canopsis (auto-remediation) [23]

### Environment Promotion

Built-in Dev → Test → Prod promotion mechanism [1][22].

### AI/LLM Integration

Support for agentic AI and LLM tasks within workflows is claimed in marketing materials [1]. ⚠ No technical documentation was found specifying supported models, integration architecture, or real-world implementations.

---

## 4. Integration Ecosystem

### Enterprise Integrations

| Category | Specifics |
|---|---|
| SAP | R/3, BW, BO, DS — versions v4.5 through v6.40 [13] |
| Cloud | Azure (Storage, Data Factory, Logic Apps), AWS S3, GCS [9][20] |
| DevOps | Jenkins, Ansible, Airflow, JobAsCode [20] |
| ITSM | ServiceNow, Jira Service Management, PagerDuty [20][21] |
| Backup | Veeam, Commvault [20] |
| Monitoring | Centreon, Canopsis, Grafana [14][20][23] |
| Virtualization | VMware vSphere [20] |

### Open-Source Connectors

AbsyssLab maintains 21 open-source repositories on GitHub, primarily Python, all Apache-2.0 licensed [20]. The ServiceNow connector (requiring Visual TOM 7.2.1f+) provides automated ticket creation from alarms with parent/child logic, available in both PowerShell 7.0+ and Python 3.10+ [21].

### REST API

Available since v6.6.1a [14]:
- Port 30002, HTTPS, token-based authentication
- Job status monitoring with environment/application/job filtering (regex)
- Service discovery for dynamic monitoring
- Legacy plugin for pre-6.6.1a versions

The product page claims "150+ software application integrations" [1] — approximately 30 specific integrations are individually documented through accessible sources.

---

## 5. System Requirements & Performance

### Hardware (Server)

| Platform | Processor | RAM | Disk |
|---|---|---|---|
| Unix | ≥ 1.5 GHz | 2 GB | 1 GB |
| Windows | Pentium ≥ 3 GHz | 2 GB | 1 GB |

Source: [11]

### Performance Limits

| Metric | Documented Value |
|---|---|
| Maximum jobs per server | 100,000 [11] |
| Safe daily workload | 50,000 jobs/day [11] |
| Maximum environments per server | 100 [11] |
| Maximum applications per environment | 300 [11] |
| Maximum resources per server | 5,000 [11] |

The product page claims capacity of 780,000–1,064,000 executions/day on minimal resources (1.6–1.7 GB RAM, 2–4 vCPUs) [1]. These marketing figures significantly exceed the documented safe limit (50,000/day) from the technical runbook [11]. ⚠ No published reconciliation of this discrepancy exists — the sources do not explain the gap between the marketing figures and the documented safe limit.

---

## 6. Pricing & Licensing

### Licensing Models

| Model | Maintenance/Support |
|---|---|
| Perpetual | 20% annual maintenance [2] |
| Subscription (on-prem) | Included [2] |
| SaaS (via partners) | Included [2] |

### Editions

Three editions: **Starter**, **Performance**, **Ultimate** [1][2]. Feature differentiation between editions is not publicly documented.

### Measurement

Customers choose one pricing metric: **Agents**, **Executions**, or **Processes** [1][2]. This three-metric flexibility is unusual in the market — most competitors standardize on one or two metrics.

### Pricing Transparency

No pricing figures are publicly available. Absyss directs prospects to custom quotes via the contact page [2]. The 20% annual maintenance rate for perpetual licenses falls within the typical 18-22% enterprise software range.

---

## 7. Competitive Landscape

### Analyst Positioning

| Report | Year | Absyss Position |
|---|---|---|
| Gartner MQ for SOAP | 2024 | Niche Player (alongside OpCon, BatchMan) [16] |
| EMA Radar for WA&O | 2025 | Included among 10 vendors [17] |
| Gartner Peer Insights | 2026 | 4.9/5.0, NPS 94 (9 reviews) [25] |

Leaders in the 2024 Gartner MQ are Redwood Software (RunMyJobs) and Stonebranch (UAC) [16].

### Migration as Competitive Strategy

Migration is central to Absyss's growth strategy, with automated job conversion from Control-M, Dollar Universe, Vega, Automator, and OpCon [8]. Track record: 30+ migrations, 50,000+ servers, 1.5M+ jobs transferred in the past 3 years [8]. Absyss claims migrations generate "strong ROI by lowering licensing/maintenance as well as operating costs" [8]. A specific "30-50% TCO savings" figure appears in marketing brochure search snippets [26] but the brochure PDF was inaccessible for verification.

### Competitive Visibility Gap

Visual TOM is underrepresented on North American review platforms (G2, PeerSpot) compared to Control-M, ActiveBatch, and Tidal. The predominantly French customer base and limited English-language presence suggest the primary market remains France and French-speaking regions.

---

## 8. Company Profile

| Attribute | Value |
|---|---|
| Founded | February 26, 1990 [19] |
| Revenue (FY2024) | €13,442,236 [19] |
| Net profit (FY2024) | €4,246,840 (31.59% margin) [19] |
| Employees | 20-49 (SME category) [19] |
| Partners | 24 integrators, 15 outsourcers, 4 OEM [5][6][7] |
| Certified colleagues | 650+ across partner network [5] |

### Named Customers

Customers span 11 sectors including major French and international organizations [4]: AP-HP, SNCF, Sanofi, Orange, SFR, ENGIE, Veolia, Fnac Darty, Chanel, MAIF, BPCE, European Commission, CNES, Ministry of Defence, Radio France.

---

## 9. Security

### Strengths

- SSL/TLS for all communication channels (server, agent, GUI, REST API) [12]
- LDAP/LDAPS and SSO authentication [12]
- Profile-based access control [12]
- MFT with granular permissions, audit trail, encrypted transfers [9]
- Automatic HA failover with 10-second refresh [12]

### Concerns

- **2018 vulnerability disclosure:** Synacktiv found critical buffer overflows in v5.7.4 — remote code execution via vtmanager, local privilege escalation via SUID bdaemon. No CVE assigned. Vendor claimed v6+ not affected [18]
- **No compliance certifications** (ISO 27001, SOC 2, GDPR) found in public sources
- **Limited security documentation:** TLS versions, cipher suites, password hashing, audit log format, SIEM integration are not publicly documented
- **No security hardening guide** found

### Data Sovereignty

Visual TOM MFT is positioned as a French sovereign alternative to US-based MFT vendors, with data control and French-based support [9]. This may be relevant for European organizations subject to data sovereignty requirements.

---

## 10. Key Considerations for Evaluation

### Strengths

1. **Exceptional platform breadth** — supports mainframes (z/OS, IBM i, GCOS, VMS) through containers (Docker, K8s) to cloud, with 12+ OS families [11]
2. **Profitable, established vendor** — 35 years in operation, €13.4M revenue, 31.6% profit margin [19]
3. **Strong French enterprise customer base** — includes major organizations across public and private sectors [4]
4. **Flexible licensing** — three models and three measurement metrics allow cost optimization [2]
5. **Active open-source connector ecosystem** — 21 GitHub repos under Apache-2.0 [20]
6. **Native MFT integration** — unified file transfer without third-party tooling [9]
7. **Proven migration path** — 30+ migrations from competing platforms [8]

### Risks

1. **Niche Player analyst positioning** — Gartner MQ 2024 [16]; limited visibility outside France
2. **Small company size** — 20-49 employees may limit support capacity for large global deployments [19]
3. **Security documentation gaps** — no public compliance certifications, limited security specs [12]
4. **AI/LLM claims unsubstantiated** — marketing mentions but no technical documentation [1]
5. **Performance discrepancy** — marketing claims (780K-1M+ executions/day) vs. documented safe limit (50K/day) [1][11]
6. **Limited English-language ecosystem** — documentation and community are primarily French-oriented
7. **Small review sample** — Gartner Peer Insights 4.9/5.0 based on only 9 reviews [25]

### Information Gaps

- No public pricing to evaluate cost-competitiveness
- No independent benchmark or comparison studies
- No published security audit or compliance certification
- AI/LLM integration details are marketing claims without specification
- Edition feature differentiation not publicly documented

---

## Methodology Notes

### Sources

27 sources were used, of which:
- 1 Tier 1 (French government registry)
- 18 Tier 2 (manufacturer documentation, analyst firms, platform certifications)
- 6 Tier 3 (partner pages, industry blogs)
- 2 Tier 2 sources were FAILED (PDFs unreadable)
- 3 sources were PARTIAL (accessed via search snippets due to 403 errors)

### Limitations

- Absyss is a French company with a primarily French customer base; English-language sources are limited
- Three PDF documents (brochures, feature differential) could not be extracted due to binary encoding
- Specific Gartner MQ strengths/cautions and EMA Radar scores are behind paywalls
- The 2018 security advisory PDF was also unreadable but key details were recovered via WebSearch
- No independent technical review or benchmark study of Visual TOM was found

Full source details: [citations.md](citations.md) | Reference files: [references/](references/) | Audit reports: [audit/](audit/)
