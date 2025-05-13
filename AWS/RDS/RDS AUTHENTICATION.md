## 🔐 Authentication to Amazon RDS

### ✅ 1. IAM Database Authentication

IAM allows applications to connect to RDS databases **without using permanent passwords**.

#### 🔧 How It Works:
- An IAM role is created and attached to the EC2 instance (or Lambda).
- The application uses this role to generate a **temporary authentication token**.
- This token is used in place of a password to connect to the database.
- RDS validates the token against the IAM policies assigned to the role.

#### 🔒 Key Points:
- Tokens are **valid for only 15 minutes**.
- Ensures **temporary, secure, and auditable** access.
- Supported only for **MySQL** and **PostgreSQL** databases.
- Follows the **least privilege** principle via IAM policies.

---

### 🔐 2. AWS Secrets Manager

Secrets Manager securely stores **RDS database credentials** (such as username and password).

#### 🔧 How It Works:
- The secret is created to store the RDS credentials.
- EC2 or other clients must have **permission to access the secret**.
- The application fetches the secret at runtime for authentication.
- Credentials are **not hard-coded** and are securely retrieved when needed.

#### 🔁 Automatic Credential Rotation:
- Secrets Manager supports **automatic rotation** of database credentials.
- A background Lambda function is used to rotate credentials on a set schedule.
- Rotation increases security by regularly updating passwords.

---

### 🔑 Summary

| Feature                     | IAM Authentication                              | AWS Secrets Manager                          |
|----------------------------|--------------------------------------------------|----------------------------------------------|
| Stores Password?           | ❌ No                                             | ✅ Yes                                       |
| Secure Access              | Temporary token via IAM role                     | IAM-controlled access to stored secret       |
| Rotation                   | Not applicable                                   | ✅ Supported with automated Lambda rotation   |
| Use Case                   | Passwordless access                              | Secure storage and rotation of credentials   |
| DB Engines Supported       | MySQL, PostgreSQL                                | All supported RDS engines                    |

---

> **Best Practice**: Use IAM for secure, temporary authentication. Use Secrets Manager for secure storage and automated rotation of credentials.
