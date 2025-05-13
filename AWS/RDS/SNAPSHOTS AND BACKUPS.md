## 🛡️ RDS Snapshots and Backups

### **Automated Backups**
- Enabled by default when you create an RDS instance.
- **Daily volume snapshot** of the database stored in **Amazon S3**.
- Allows **point-in-time recovery** within the backup retention period.

#### Key Details:
- **Retention Period**: 
  - Can be configured from **1 to 35 days**.
  - Longer retention increases storage cost.
- **Deleted on RDS Deletion**:
  - All automated backups are **removed** when the RDS instance is deleted.
- **I/O Suspension**:
  - Brief suspension of I/O may occur during backups.
  - **Multi-AZ** deployment is recommended — AWS performs backups from the **standby instance**, not the primary.
- **Retention = 0**:
  - All automated backups are deleted.
  - No point-in-time recovery available if set to 0.

---

### **Manual Snapshots**
- Must be **created manually** by the user.
- Persist even after the RDS instance is deleted.
- Stored until **explicitly deleted** by the user.

#### Key Details:
- **Full snapshot** of the DB instance, not just the database itself.
- Useful for **long-term archival** or cloning environments.
- Minor I/O suspension during snapshot creation (again, multi-AZ recommended).
- Can be used to **restore a DB instance** at any time.

---

### ✅ Comparison: Automated Backups vs Manual Snapshots

| Feature                     | Automated Backups                         | Manual Snapshots                             |
|----------------------------|--------------------------------------------|-----------------------------------------------|
| Creation                   | Daily, automatic                          | User-initiated                                |
| Retention                  | 1 to 35 days (configurable)               | Until deleted manually                         |
| Deleted with RDS           | Yes                                       | No                                             |
| Recovery Type              | Point-in-time recovery                    | Restore to the time snapshot was taken         |
| Backup Target              | Standby (Multi-AZ) or primary (Single-AZ) | Same                                           |
| I/O Suspension             | Brief (if no standby)                    | Brief (multi-AZ minimizes impact)              |

---

> **Tip**: Whether restoring from an automated or manual snapshot, the result is the same — a new RDS instance with data as of the snapshot time.
