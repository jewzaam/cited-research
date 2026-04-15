# Feature Set & Capabilities

Dimension covering Visual TOM's functional capabilities across scheduling, orchestration, MFT, monitoring, and AI integration. See [citations.md](../citations.md) for full source details.

## Job Scheduling

### Scheduling Methods

Visual TOM supports two primary scheduling approaches [10]:

1. **Schedule-based:** Days, weeks, months, day numbers with calendar validation
2. **Formula-based:** Complex rules using SNL (Syntax Notation Language) with keywords like `today`, `first`, `last`, `work`, `closed`

Example formula: `test {today=3.day.work.month}` executes on the 3rd working day of each month [10].

### Frequency Controls

- Daily, weekly, monthly, or yearly maximum execution counts [10]
- **Cyclic execution** modes: Permanent (immediate restart), Time-based (interval), Cron format (`MINUTES [HOURS]`) [10]

### Operation Date

Production day runs "midnight to midnight" independent of system date, with three modes [10]:
- Automatic: Changes when all jobs complete and constraints validate
- System: Changes at midnight regardless of job status
- Constant: Manual updates only

## Workflow Orchestration

### Resource/Constraint Types

10 resource types control job execution [10]:

| Type | Purpose |
|---|---|
| Text | Conditional start via string comparison |
| Weight | Limit simultaneous job quantities across agents |
| Stack | FIFO queue-based triggering |
| Date | Temporal validation and parametrized date values |
| Generic | Script execution validation (return code = 0) |
| File | File presence/absence detection |
| Numerical | Numeric value comparison |
| SAP Event | SAP R/3 or BW event availability |
| SGBD | SQL query or stored procedure results |
| Remote File | FTP/SFTP/SCP file detection |

### Submit Unit Modes

| Mode | Behavior |
|---|---|
| Single Agent | First agent in list only [10] |
| Multi-Agent | All agents execute (instantiated jobs) [10] |
| Backup | Sequential fallback if agent unavailable [10] |
| Load Balancing | Least-loaded agent selection [10] |

### Execution Modes

Four modes: Execution (actual submission), Simulation (validation only), Test (environment variable injection before submission), Stop (planning invalidated) [10].

### Error Handling

Configurable successor management on error [10]:
- "Deschedule successors": Immediate cancellation of dependent jobs
- "Deschedule at time": Delayed cancellation
- "Do not deschedule": Error isolation

Automatic restart with configurable retry attempts and delay, recovery script support, max duration enforcement [10].

## Event-Driven Automation

Real-time responsiveness with dynamic plan mechanisms for daily execution monitoring [1]. VTOM can trigger automated job execution in response to external events, including integration with Canopsis for auto-remediation — successful remediation suppresses alerts and feeds statistics, failures escalate to operators [23].

## Managed File Transfer (MFT)

Visual TOM MFT is a natively integrated managed file transfer solution [9].

### Components

| Component | Purpose |
|---|---|
| MFT Gateway | Remote-to-remote transfers with integrated SFTP server [9] |
| MFT Portal | Browser-based secure file exchange for partners [9] |
| Unified Cockpit | Real-time supervision across distributed servers [9] |
| Virtual Folders | Logical file views independent of physical storage [9] |

### Supported Protocols and Storage

| Category | Options |
|---|---|
| Transfer protocols | FTP, SFTP, FTPS [9] |
| Cloud storage | AWS S3, Azure Blob Storage, Google Cloud Storage, Scaleway, Alibaba OSS [9] |
| On-prem storage | NAS, NFS, SMB, SharePoint, Google Drive [9] |
| In development | PESIT, AS2 [9] |

### Automated Orchestration

File deposit triggers Visual TOM workflows automatically [9].

## Monitoring & Alerting

### Alarms

Deviation detection on schedule, duration, or status with actions [10]:
- Script execution
- SNMP traps
- Email notifications
- Event sending
- ITMessenger integration

### Notification Channels

Email, SMS, WhatsApp, Teams, Slack [1].

### REST API Monitoring

Available since v6.6.1a, default port 30002 over HTTPS [14]:
- Token-based authentication
- Job status endpoints (running, error, waiting, finished, not scheduled, descheduled)
- Filtering by environment, application, job name (regex)
- Service discovery for dynamic monitoring
- Cache generation for performance [14]

### SmartView Mobile

Dedicated mobile app for iOS and Android providing operational intelligence and KPI monitoring [1]. Available on Google Play and Apple App Store.

## Self-Service & Dashboards

- Web-based self-service portal for end-user IT autonomy [1]
- Customizable cross-technology dashboards for ops and business users [1]
- Dedicated training/certification track for self-service and dashboards [24]

## Environment Promotion

Built-in Dev → Test → Prod promotion mechanism for batch updates [1][22].

## AI/LLM Integration

Support for agentic AI and LLM tasks directly within workflows, including diagnostic and analytical capabilities [1]. This appears to be a recent addition based on 2026-era marketing materials. ⚠ No detailed technical documentation was found on the specific AI/LLM integration capabilities, supported models, or implementation architecture.

## Advanced Features

- **Contexts:** Environment variable sets with inheritance and overloading across Environment → Application → Job levels [10]
- **Instructions:** Decision-support documentation linked to objects via URI or internal HTML/text [10]
- **Templates:** Reusable job definitions [10]
- **Collections & Snapshots:** Differential graph comparison for change tracking [10]
- **Periods & Tokens:** Custom time intervals and formula fragments for planning reuse [10]
- **JobAsCode:** Repository for managing scheduling definitions as code (Python, Apache-2.0) [20]

## Training & Certification

Three certification tracks [24]:
1. **Designer Certification** — functional knowledge on designing and controlling
2. **Administrator Certification** — functional and technical knowledge, Level II, 1.5 hour exam
3. **Self-Service & Dashboards** — portal and dashboard proficiency

## Gaps and Limitations

- AI/LLM integration claims lack technical documentation — no details on supported models, API integration method, or real-world use cases
- The functional differential document (v7.2 feature comparison) was inaccessible as a PDF [27]
- Specific Agentic AI capabilities are marketing claims without published specifications
- No public documentation on webhook support for inbound event triggers (REST API is primarily for monitoring [14])
