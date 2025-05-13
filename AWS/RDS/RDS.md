# AWS RDS Overview

## What is RDS?

- **Amazon RDS (Relational Database Service)** is a **managed service** that allows you to run relational databases in AWS without handling the underlying infrastructure.
- Compared to **EC2**:
  - EC2 is a **not managed service** — you choose the OS, install software, manage updates, backups, etc.
  - RDS is a **managed service** — you choose the database engine and version, but AWS handles:
    - Backups
    - Snapshots
    - Software patching
    - Upgrades
    - Monitoring

---

## Supported Database Engines in RDS:

- SQL-based:
  - PostgreSQL
  - MySQL
  - Oracle
  - MariaDB
  - Amazon Aurora

---

## RDS Features & Characteristics:

- **No shell access** to the underlying database server (as it is a managed service).
- **Runs in a private subnet** within a VPC.
  - You can configure **firewalls** (via security groups and NACLs).
- **Monitoring**:
  - Integrates with **Amazon CloudWatch** to set alarms and collect metrics.
- **Storage**:
  - Uses **Amazon EBS** as the underlying storage layer.
  - Supports **storage auto-scaling**.
- **Maintenance**:
  - You can set **maintenance windows** for upgrades and patches.
- **Billing**:
  - Depends on:
    - Engine type and version
    - Storage capacity
    - Storage throughput
    - Read/write operations
    - Data transfer
- **Pricing Options**:
  - **On-Demand Instances**
  - **Reserved Instances**

---

## Summary Table

| Feature                  | Description                                                               |
|--------------------------|---------------------------------------------------------------------------|
| Managed by AWS           | Yes – backups, patching, scaling, etc.                                    |
| Shell Access             | Not provided                                                              |
| Network                  | Runs in private subnet, can configure firewall                            |
| Monitoring               | CloudWatch integration                                                    |
| Storage                  | EBS-based, supports auto-scaling                                          |
| Maintenance              | Customizable maintenance windows                                          |
| Billing Factors          | Engine type, storage, throughput, IOPS, data transfer                     |
| Pricing Models           | On-Demand, Reserved                                                       |
