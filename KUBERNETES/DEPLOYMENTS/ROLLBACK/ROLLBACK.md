# 🔁 Rollbacks

## Why Rollbacks Are Needed
Rollbacks help you **revert to a previous stable state** if a new deployment or release causes:
- Application crashes
- Unintended bugs or regressions
- Misconfigurations
- Performance issues

---

## 🛠️ Option 1: `kubectl rollout undo`

### ✅ Best for:
- Manually deployed workloads (e.g., `kubectl apply`)
- Quick fixes to `Deployment` objects
- Rollback of non-Helm-managed apps

### 🔧 Commands:
```bash
# Rollback the latest Deployment to the previous revision
kubectl rollout undo deployment <deployment-name>

# Rollback to a specific revision
kubectl rollout undo deployment <deployment-name> --to-revision=2

# Check rollout history
kubectl rollout history deployment <deployment-name>
```

## 🎩 Option 2: `helm rollback`

### ✅ Best for:
- Apps deployed with Helm charts
- Managing the full lifecycle of applications
- Reverting multiple Kubernetes objects as a set

### 🔧 Commands:
```bash
# List previous release revisions
helm history <release-name>

# Rollback to a previous revision
helm rollback <release-name> <revision-number>

# Example:
helm rollback my-app 2
```
## 🔍 Notes:

- Rolls back everything defined in the Helm chart (Deployment, Services, ConfigMaps, etc.)
- Works best when changes were made via Helm (not via `kubectl` directly)

---

## ⚖️ Summary Comparison

| Feature        | `kubectl rollout undo`             | `helm rollback`                                |
|----------------|------------------------------------|-------------------------------------------------|
| **Scope**      | Specific resource (e.g., Deployment) | Entire Helm release (all related resources)     |
| **Tracking**   | ReplicaSet history in Kubernetes   | Helm release revision history                   |
| **Granularity**| Fine control over single resource  | All-in-one rollback                             |
| **Use Case**   | Non-Helm deployments               | Helm-managed apps                               |
| **Complexity** | Simple for single resource         | Powerful for app stacks                         |

