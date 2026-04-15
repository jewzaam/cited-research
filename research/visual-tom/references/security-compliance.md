# Security & Compliance

Dimension covering Visual TOM's security features, authentication, encryption, audit capabilities, and compliance posture. See [citations.md](../citations.md) for full source details.

## Authentication & Access Control

### Authentication Methods

| Method | Details | Source |
|---|---|---|
| Local authentication | Profile-based accounts with assigned rights | [12] |
| LDAP/LDAPS | External authentication via LDAP directory | [12] |
| SSO | Single sign-on integration | [12] |
| REST API token auth | Username/password or direct token-based | [14] |

Login without prior user creation is supported via LDAP integration [12].

### Access Control Model

Visual TOM uses a profile-based access control system where Profiles represent sets of rights granted to Accounts [12]. The MFT component provides "granular user, group, and folder-level permissions" [9].

Specific details on role granularity (e.g., whether permissions can be assigned at the job, application, or environment level) were not found in accessible documentation.

### Default Credentials

Default administrative credentials (admin/Absyss) are mentioned in discovery research. ⚠ These should be changed immediately post-installation.

## Encryption & Secure Communications

### TLS/SSL

SSL/TLS is configurable for [12]:
- Server communications
- Agent communications
- GUI connections
- HTTP server
- REST API

Both global configuration and per-component configuration options are available [12].

### MFT Transfer Encryption

| Protocol | Encryption |
|---|---|
| SFTP | SSH-based encryption [9] |
| FTPS | TLS-encrypted FTP [9] |
| HTTPS | TLS-encrypted file transfer via portal [9] |

⚠ Specific TLS version support (1.2, 1.3), cipher suites, and certificate management details are not documented in publicly accessible sources.

## Network Security

### Default Ports

| Service | Port | Protocol |
|---|---|---|
| vtmanager | 30000 | TCP [18] |
| tomDBd | 30001 | TCP [12] |
| REST API | 30002 | HTTPS [14] |
| bdaemon | 30004 | TCP [12] |

### Agent Communication

Agents communicate with the server over TCP ports configured during installation. Port assignments must match across server and agent deployments [12].

## Audit & Logging

### MFT Audit Trail

Complete timestamp-logged operation history including deposits, downloads, and deletions for compliance [9].

### Job Execution

Job execution logs are maintained in a dedicated logs directory (`/<installdir>/logs`) [11]. The REST API provides real-time job status monitoring including running, error, waiting, finished, not scheduled, and descheduled counts [14].

### Alarm System

Alarms trigger on schedule deviation, duration anomalies, or unexpected statuses with configurable actions including SNMP traps, email, and script execution [10].

⚠ Specific audit event format, SIEM integration capabilities, and log retention policies are not documented in accessible sources.

## High Availability & Disaster Recovery

| Feature | Details | Source |
|---|---|---|
| Backup Server | Automatic data replication and failover | [12] |
| Refresh interval | 10-second default (configurable) | [12] |
| Failover trigger | Primary unresponsive or agent connectivity failure | [12] |
| Backup modes | R (replication only), S (auto-switch) | [12] |
| Cluster support | MC Service Guard, HACMP, MS Cluster | [12] |
| Requirements | Same network, identical OS, matching install trees | [12] |

## Historical Vulnerabilities

### 2018 Synacktiv Advisory

Synacktiv published a security advisory on 2018-07-17 documenting multiple buffer overflow vulnerabilities in Visual TOM v5.7.4 [18]:

**Vulnerability #1: vtmanager Stack Buffer Overflow**
- Location: Offset 0x40B703, bad use of `sscanf` function
- Attack vector: Remote, via specially crafted URL to port 30000
- Impact: Remote code execution in administrator context
- Root cause: Format string does not limit character storage between path components

**Vulnerability #2: bdaemon Buffer Overflows**
- Location: Multiple, including offset 0x41F37C
- Attack vector: Local (bdaemon has SUID bit set)
- Impact: Local privilege escalation to root
- Root cause: `strcpy` of user-controlled environment variable data into fixed-size stack buffer
- Aggravating factor: Linux binary compiled without stack canaries

**CVE Status:** No CVE identifier was publicly assigned to these vulnerabilities [18].

**Affected versions:** v5.7.4 (version 5 is end-of-life). Vendor reportedly claimed version 6+ is not vulnerable, but this claim was not independently verified.

⚠ No additional security advisories, penetration test reports, or vulnerability disclosures were found for Visual TOM beyond this 2018 advisory.

## Compliance Certifications

### Confirmed

| Certification | Details | Source |
|---|---|---|
| Red Hat Certified Software | Listed in Red Hat ecosystem catalog | Discovery research |

### Not Found

The following compliance certifications were searched for but no evidence was found in public sources:
- ISO 27001
- SOC 2
- GDPR-specific compliance documentation
- HIPAA
- PCI-DSS

⚠ The absence of public documentation does not mean these certifications don't exist — enterprise vendors sometimes share compliance documentation only under NDA or during procurement processes.

## Data Sovereignty Positioning

Visual TOM MFT is explicitly positioned as a "French, sovereign alternative" to American MFT solutions (Axway CFT/Secure Gateway, IBM Sterling, Fortra GoAnywhere, Progress MOVEit) [9]. Key sovereignty claims:
- Complete data control with no external server transit [9]
- French-based support without international ticket routing [9]

This positioning may be relevant for organizations subject to European data sovereignty requirements.

## Gaps and Limitations

- No compliance certifications (ISO 27001, SOC 2, GDPR) could be verified from public sources
- TLS version support and cipher suite details are not documented publicly
- Audit log format, retention policies, and SIEM integration are not specified
- Password hashing/storage mechanisms are not documented
- No security hardening guide was found
- SAML support is unclear — SSO is mentioned but the specific protocol is not specified [12]
- Multi-factor authentication support is not documented beyond LDAP/SSO delegation
- Data-at-rest encryption capabilities are not documented
- Secrets management for integrated system credentials is not documented
- The 2018 vulnerability disclosure lacks CVE assignment, making it harder to track in vulnerability management systems [18]
- No penetration testing reports or independent security assessments beyond the 2018 Synacktiv advisory were found
