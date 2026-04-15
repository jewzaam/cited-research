# Platform & Integration Support

Dimension covering Visual TOM's supported platforms, cloud integrations, enterprise connectors, and API capabilities. See [citations.md](../citations.md) for full source details.

## Operating System Support

Full compatibility table from v6.71c documentation [11]:

| OS | Processor | Min Version | Server | Agent | GUI |
|---|---|---|---|---|---|
| Windows Server | x86/x86_64 | > W2008 | ✓ | ✓ | ✓ |
| Windows Workstation | x86/x86_64 | ≥ Windows 7 | | | ✓ |
| HP-UX | PA-RISC/IA64 | ≥ 11.31 | ✓ | ✓ | |
| Solaris | SPARC/x86 | ≥ 5.10 | ✓ | ✓ | |
| AIX | RS6000/Power | ≥ 5.3 | ✓ | ✓ | |
| Linux | x86/x86_64/POWER7 | Kernel > 2.4.20 | ✓ | ✓ | ✓ |
| Mac OS | x86_64 | ≥ 10.15.2 | | | ✓ |
| VMS/DECUX | Alpha/IA64 | ≥ 7.2/OSF1 V4 | ✓ | ✓ | |
| SCO | x86 | ≥ 4.0 | ✓ | ✓ | |
| OS/400 (IBM i) | RS6000 | ≥ 5 | ✓ | ✓ | |
| Z/OS (IBM z) | — | ≥ 1.11 | ✓ | ✓ | |
| GCOS7/GCOS8 (Bull) | — | varies | ✓ | ✓ | |

Notable: GCOS7/GCOS8 support for Bull mainframes is uncommon among modern workload automation tools and reflects Absyss's French legacy system heritage [11].

## Execution Models

Visual TOM supports both agent-based and agentless execution [1][22]:
- **Agent-based:** Agent installed on target machine, receives submission orders from server [10]
- **Agentless:** Referenced in product materials but detailed protocol support not documented in accessible sources

## Cloud Platforms

Marketed as supporting Azure, AWS, and Google Cloud Platform [1]. Specific integrations:

| Cloud | Integration | Source |
|---|---|---|
| Azure Blob Storage | Open-source connector (Python) | [20] |
| Azure Data Factory | Open-source connector for pipeline orchestration | [20] |
| Azure Logic Apps | Open-source connector | [20] |
| AWS S3 | MFT file transfer support | [9] |
| Google Cloud Storage | MFT file transfer support | [9] |
| Scaleway Object Storage | MFT file transfer support | [9] |
| Alibaba Object Storage | MFT file transfer support | [9] |

## Container & Virtualization

| Platform | Support Type |
|---|---|
| Docker | Deployment and orchestration [1] |
| Kubernetes | Deployment and orchestration [1] |
| VMware vSphere | Open-source connector for VM management [20] |

## SAP Integration

Dedicated SAP Guide with support for [13]:

| SAP Module | Capabilities |
|---|---|
| R/3 | ABAP programs, Variants, Batch inputs |
| BW (Business Warehouse) | Chain processes, Info packages |
| BO (BusinessObjects) | Webi, Deski, Crystal Reports |
| DS (Data Services) | Batch execution scheduling |

Supported SAP versions: v4.5, v4.6, v4.7, v6.10, v6.20, v6.40 [13]. Requires Visual TOM Agent on SAP server machine with customized Batch Queue. No SAP software modifications needed [13]. BW module requires Java + SAPJCO package [13].

## Open-Source Connectors (AbsyssLab GitHub)

21 repositories, all Python (except Jenkins/Batchfile), all Apache-2.0 licensed [20]:

| Category | Connectors |
|---|---|
| Cloud/Automation | Azure Storage, Azure Data Factory, Azure Logic Apps |
| DevOps/CI-CD | Jenkins, Ansible, Airflow, JobAsCode |
| Backup/Recovery | Veeam, Commvault |
| ITSM | ServiceNow, Jira Service Management, PagerDuty |
| Virtualization | VMware |
| Monitoring | Grafana |

The ServiceNow connector automates ticket creation from Visual TOM alarms with parent/child ticket logic, requires Visual TOM 7.2.1f+, implemented in both PowerShell 7.0+ and Python 3.10+ [21].

## REST API

Introduced in v6.6.1a [14]:
- Default port: 30002, HTTPS
- Authentication: Username/password (basic) or token-based
- Endpoints: `/auth/1.0/authorize`, `/monitoring/1.0/jobs/status`
- Capabilities: Job status monitoring, filtering by environment/application/job name (regex), service discovery, cache generation
- Timeout: 30 seconds (configurable)
- HTTP backends: LWP (default) or cURL
- Legacy plugin available for versions before 6.6.1a [14]

## Monitoring Integrations

| Tool | Integration Type |
|---|---|
| Centreon | REST API plugin pack for job monitoring [14] |
| Canopsis | Auto-remediation — VTOM triggers jobs to resolve alerts [23] |
| Grafana | Open-source dashboard connector [20] |

## Enterprise Integration Categories

Product page lists broad integration categories without specifying individual products [1]:
- ERP, BI, BigData, Databases, ITSM, Backups
- CI/CD, ETL, MFT, WebServices, Provisioning

The product page claims "150+ software application integrations" — specific product names beyond those documented above were not independently verified.

## MFT Protocols

| Protocol | Status |
|---|---|
| FTP | Supported [9] |
| SFTP | Supported [9] |
| FTPS | Supported [9] |
| PESIT | In development [9] |
| AS2 | In development [9] |

## Gaps and Limitations

- Specific Linux distributions (RHEL, SUSE, Ubuntu, Debian) and their minimum supported versions are not enumerated — only kernel version ≥ 2.4.20 specified [11]
- Cloud integration depth beyond storage/file operations (e.g., AWS Lambda, Azure Functions, GCP Cloud Functions) is not documented
- Kubernetes integration details (job scheduling via K8s Jobs/CronJobs vs. pod lifecycle management) are not publicly specified
- The "150+ software applications" claim [1] lacks a public enumeration — only ~30 specific integrations are individually documented
- Agentless execution protocols and limitations are not detailed in accessible documentation
- No documented JDBC/ODBC database connectors beyond the SGBD resource type for SQL queries [10]
