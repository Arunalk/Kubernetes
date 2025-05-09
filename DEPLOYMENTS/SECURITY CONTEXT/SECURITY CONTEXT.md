# 🔐 Security Context in Kubernetes

## 📘 Introduction

In Kubernetes, a **Security Context** defines privilege and access control settings for a Pod or Container. It allows you to specify the user and group to run as, whether the container has privileged access, file system permissions, Linux capabilities, and more. This is critical for enforcing the principle of **least privilege**, improving container isolation, and hardening workloads.

Security contexts can be applied at two levels:
- **Pod-level**: Applies settings to all containers within the pod.
- **Container-level**: Applies settings only to a specific container.

---

## ❓ Why Use a Security Context

### ✅ Enforce Least Privilege
Limit what a process can do or access inside the container, minimizing the risk from vulnerabilities or compromised apps.

### ✅ Improve Isolation
Prevent containers from performing privileged operations unless explicitly required.

### ✅ Comply with Security Policies
Meet organizational or regulatory compliance standards (e.g., PCI-DSS, HIPAA) by ensuring workloads do not run as root.

### ✅ Protect Host System
Avoid unintended access to host resources, filesystem, or devices, especially in shared or multi-tenant environments.

---

## 🚨 When Security Context is Needed

### 🔸 Example Scenarios:
- You want your containers to **run as a non-root user** for better security (`runAsUser`, `runAsNonRoot`).
- You need containers to **share volume data safely** (`fsGroup`).
- You want to make the **filesystem read-only** (`readOnlyRootFilesystem`).
- You want to **restrict system-level calls** using seccomp profiles (`seccompProfile`).
- You want to **grant specific capabilities** like `NET_ADMIN` without running as root.

---

## 🔧 When Privileged Access Is Needed

While it's best to avoid privileged containers, there are cases where it's justified:

| Use Case | Why Privileged Mode is Needed |
|----------|-------------------------------|
| **Docker-in-Docker** | Needs access to Docker daemon or create other containers. |
| **Hardware Access** | Access GPUs, USBs, or other host devices. |
| **Networking Tools** | Modify routing tables, interfaces, or use raw sockets. |
| **Monitoring Tools** | Kernel-level monitoring, packet capturing, syscalls tracing. |
| **Admin Tools** | Modify users, kernel modules, or host configuration. |

> ⚠️ **Best Practice:** Instead of full `privileged: true`, prefer adding only necessary capabilities using the `capabilities` field.

---

## 🧩 Example

```yaml
securityContext:
  runAsUser: 1000
  runAsGroup: 3000
  fsGroup: 2000
  readOnlyRootFilesystem: true
  allowPrivilegeEscalation: false
  capabilities:
    drop:
      - ALL
    add:
      - NET_ADMIN
  seccompProfile:
    type: RuntimeDefault
```

