# Product Overview & Architecture

Dimension covering Visual TOM's identity, architecture, deployment models, and system requirements. See [citations.md](../citations.md) for full source details.

## Product Identity

Visual TOM (Visual Time Operation Manager) is a workload automation and job scheduling platform developed by Absyss, a French software publisher headquartered in Montrouge, France [1][3]. It is categorized as a Service Orchestration and Automation Platform (SOAP) by Gartner [16]. The product is available as on-premises software or as a SaaS offering delivered through partner channels [1][2].

Visual TOM is the flagship product of the Visual IT Operations suite, which also includes Visual BAM (business activity monitoring) and Visual IT Messenger (critical notification management) [3].

## Architecture

Visual TOM uses a client/server architecture organized into five module families: Servers, Agents, XVision, Xapplication, and XFR [12].

### Server Components

| Component | Code | Role |
|---|---|---|
| Enterprise Server | VT-SES | Central repository, job scheduling engine, APIs [10] |
| Departmental Server | VT-SDS | Remote site autonomy in distributed architectures [10] |
| Backup Server | VT-SBU | Automatic failover for high-availability production [10] |

### Execution Layer

| Component | Code | Role |
|---|---|---|
| Agent | VT-CS | Receives submission orders, executes batch jobs across platforms [10] |
| Net Agent | VT-CN | Autonomous local repository capability [10] |

### Interface

| Component | Code | Role |
|---|---|---|
| XVision GUI | VT-XVI | Design, control, and multi-platform management interface [10] |

### Hierarchical Model

The system uses four nested organizational levels with inheritance — values changed at higher levels automatically cascade downward [10]:

1. **Domain** — highest level; contains all production definitions, agents, users, resources, calendars, batch queues
2. **Environment** — groups applications, assigns default execution properties, controlled by a dedicated Engine process
3. **Application** — logical grouping of related jobs with shared constraints
4. **Job** — elementary executable task (script, runtime module, command)

### Communication

Default TCP ports [12]:
- **bdaemon** (port 30004): Agent listening port
- **tomDBd** (port 30001): Agent-to-server communication
- **REST API** (port 30002): Monitoring and management API [14]

Agent version must be ≤ server version; equal versions required for Job Templates functionality [12].

## Deployment Models

| Model | Description |
|---|---|
| On-Premises | Traditional datacenter deployment; perpetual or subscription licensing [2] |
| SaaS | Cloud-based, delivered through partner channels; support/maintenance included [2] |
| Hybrid | Mixed on-prem and cloud environments supported [1] |

Architecture types: centralized, distributed, combined with backup server [10].

## High Availability

- Primary and backup servers must be on the same network with identical OS [12]
- Installation trees must match between servers [12]
- Unix: same administrator username required on both servers [12]
- Backup modes: "R" (replication only) or "S" (with auto-switch) [12]
- Default 10-second refresh interval (configurable via `backup_monitor_loop`) [12]
- Automatic database replication and failover on primary failure [12]
- Cluster mode support via MC Service Guard, HACMP, MS Cluster equivalents [12]

## System Requirements

### Supported Operating Systems (v6.71c)

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
| GCOS7/GCOS8 | — | varies | ✓ | ✓ | |

Source: [11]

### Hardware Requirements

| Platform | Processor | RAM | Disk |
|---|---|---|---|
| Unix Server | ≥ 1.5 GHz | 2 GB | 1 GB |
| Windows Server | Pentium ≥ 3 GHz | 2 GB | 1 GB |

Source: [11]

### Performance Metrics

| Metric | Value |
|---|---|
| Maximum jobs per server | 100,000 [11] |
| Maximum environments per server | 100 [11] |
| Maximum applications per environment | 300 [11] |
| Maximum resources per server | 5,000 [11] |
| Safe daily workload | 50,000 jobs/day [11] |
| Object name length | 64 characters [11] |

Product page performance claims (higher than documented limits): 780,000 executions/day on 1.6 GB RAM / 2 vCPUs and 1,064,000 executions/day on 1.7 GB RAM / 4 vCPUs [1]. ⚠ These figures significantly exceed the documented safe limit of 50,000/day from the runbook [11]. No published reconciliation of this discrepancy exists — the sources do not explain the gap.

### Software Prerequisites

- Java: ≥ 1.6 (for GUI) [11]
- Database: PostgreSQL [11]
- Communication: TCP/UDP, SNMP [11]

## Version History

The most recent documented version is 7.11a (docs last updated July 7, 2023) [15]. Version 6.71 has extensive documentation across multiple builds (671c through 671i) [10][11][12]. The REST API was introduced in version 6.6.1a [14].

## Gaps and Limitations

- Specific minimum versions for Linux distributions (RHEL, SUSE, Ubuntu) are not enumerated in the runbook — only a kernel version minimum is given [11]
- The product page performance figures (780K–1.06M executions/day) significantly exceed the documented safe limit (50K/day) without published methodology for the higher figures [1][11]
- No public documentation on database sizing guidelines or storage growth rates
- Version 7.x detailed technical specifications require access to v711a documentation guides, which are behind navigation (index page only confirms their existence) [15]
