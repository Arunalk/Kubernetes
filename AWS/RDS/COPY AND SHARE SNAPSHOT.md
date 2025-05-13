## 🔁 Copying and Sharing RDS Snapshots

### ❌ Sharing Automated Snapshots
- **Automated snapshots cannot be shared**.
- Only **manual snapshots** are shareable.

---

### ✅ Sharing Manual Snapshots

You **can share manual snapshots** across:
- **Different AWS regions**
- **Different AWS accounts**

However, there are some **steps and conditions** to follow:

---

### 📋 Steps to Share Automated Snapshots

1. **Copy the Snapshot**
   - You must first **copy the snapshot**, even if you're sharing to the same region.
   - If sharing to a **different region**, copy it to that region.

2. **Handle Encryption (if applicable)**
   - If the snapshot is **encrypted with a KMS key**, ensure:
     - The **copied snapshot** uses a **KMS key from the source account**.
     - The destination account has permission to use the key (via **KMS key policy**).

3. **Share the Snapshot**
   - After copying, you can **share the snapshot** by specifying the **AWS Account ID** of the recipient.
   - You can make the snapshot **public** (not recommended) or share it **privately** with specific accounts.

---

### 🔐 Snapshot Sharing Rules (Encrypted vs Unencrypted)

| Snapshot Type     | Shareable | Notes                                                                 |
|-------------------|-----------|-----------------------------------------------------------------------|
| Automated         | ❌        | Cannot be shared                                                      |
| Manual (Unencrypted) | ✅     | Can be shared directly                                                |
| Manual (Encrypted) | ✅       | Must be copied first with a KMS key from the source account           |

---

> **Reminder**: Sharing encrypted snapshots requires careful **KMS permissions setup** to allow access in the target account.
