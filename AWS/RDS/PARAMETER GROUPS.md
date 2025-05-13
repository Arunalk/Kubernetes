## ⚙️ RDS Parameter Groups

### 🔒 Limited Access to OS
Since RDS is a **fully managed service**, users do **not get shell or OS-level access** to the underlying database instance.

However, some advanced database configuration changes typically made at the OS or database config file level are still possible.

---

### 🔧 What Are Parameter Groups?

- **Parameter groups** act like configuration files for RDS.
- They allow you to **customize database engine settings**.
- Every RDS instance is associated with a **parameter group**.
- AWS provides a **default parameter group**, but it's read-only.

---

### ✍️ Custom Parameter Groups

- You can **create a custom parameter group** to modify supported settings.
- Common use cases include:
  - **Enforcing SSL/TLS connections** (`force_ssl`)
  - **Changing timeouts**
  - **Adjusting memory or cache limits**
- After modifying parameters, you may need to **reboot the RDS instance** for changes to take effect (depending on the parameter type).

---

### 🧠 Key Points

- Parameter groups are **engine-specific** (e.g., MySQL, PostgreSQL).
- They are also **version-specific** — a parameter group for MySQL 5.7 can't be used with MySQL 8.0.
- Only settings exposed by AWS are configurable; some low-level OS or engine parameters remain restricted.

---

> **Tip**: Always clone the default group before making changes, and apply the custom parameter group to your DB instance for better control and safety.
