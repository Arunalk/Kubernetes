## 🧩 RDS Option Groups

### 📦 What Are Option Groups?

- **Option Groups** are used to enable **additional features** in RDS that are **not part of Parameter Groups**.
- They allow you to configure **extra capabilities** supported by certain database engines.

---

### 🔧 Use Cases

- Enable advanced options like:
  - **Oracle features** (e.g., TDE, APEX)
  - **SQL Server features**
  - **MySQL features like Memcached or audit plugins**
- For example, enabling a **memory cache** layer could require an option group, not a parameter change.

---

### 🌐 Scope & Limitations

- Option Groups are:
  - **Region-specific**
  - **VPC-specific**
- This means if you **migrate an RDS instance to another region**, its option group **does not carry over** automatically.
- You must **recreate the option group** in the target region.

---

### 🧠 Key Points

| Feature                | Option Groups                           | Parameter Groups                          |
|------------------------|------------------------------------------|--------------------------------------------|
| Purpose                | Add-on features and plugins              | Engine settings and configurations         |
| Region/VPC Bound?      | ✅ Yes                                    | ❌ No                                       |
| Example                | Enable Memcached, Oracle APEX            | Set force SSL, max_connections             |
| Reboot Needed?         | Sometimes (depends on the option)        | Sometimes (depends on the parameter type)  |

---

> **Note**: Option groups are supported only by specific engines and engine versions. Not all DB types require or use them.
