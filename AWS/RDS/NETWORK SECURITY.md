## 🔒 Securing EC2 to RDS Communication

### 📡 Architecture Overview
- A **web server** (EC2 instance) runs in a **public subnet** to serve frontend traffic.
- An **RDS database** resides in a **private subnet** for security.
- Internet traffic first hits the EC2 instance, which then forwards **backend requests to RDS**.

---

### 🔐 Security Groups (SG)
- Security Groups are **stateful firewalls** applied at the **instance level**.
- You can configure RDS security group to allow **incoming traffic**:
  - **Source**: EC2 instance's security group
  - **Port**: The database port (e.g., 3306 for MySQL)
- Ensures **only the EC2 instance can access the RDS** instance directly.

---

### 🧱 Network ACL (NACL)
- NACLs are **stateless firewalls** applied at the **subnet level**.
- Key differences from security groups:
  | Feature            | Security Group        | Network ACL            |
  |--------------------|------------------------|-------------------------|
  | Scope              | Specific instances     | Entire subnet           |
  | Stateful?          | ✅ Yes                | ❌ No (stateless)       |
  | Use case           | Per-instance filtering | Broad subnet filtering  |
  | Return traffic     | Automatically allowed  | Must be explicitly allowed |

- For additional security, apply **inbound and outbound rules** at the NACL level to filter traffic entering or leaving the subnet.

---

### 🔐 SSL Encryption in Transit
- You can enforce **SSL (TLS) encryption** for connections between EC2 (database client) and RDS.
- This protects data from **man-in-the-middle attacks** by encrypting traffic at both ends.

#### How to Enable:
- Modify the **DB parameter group** to enforce SSL:
  - For example, set `rds.force_ssl=1` in PostgreSQL.
- Ensure the client (EC2 app) supports SSL connections and is configured to use them.

---
### Client Validation (Authentication)
There are two main methods to authenticate the DB client:

**a. Username & Password**
**b. IAM authentication**

> **Best Practice**: Combine **Security Groups**, **NACLs**, and **SSL encryption** to build a layered security model that protects your RDS deployment against both internal and external threats.
