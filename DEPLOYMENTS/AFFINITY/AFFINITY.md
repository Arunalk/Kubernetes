# 🧭 Kubernetes Affinity Cheat Sheet

Affinity and anti-affinity rules control where pods get scheduled in a Kubernetes cluster, based on labels and topology.

---

## 🖥️ Node Affinity

Controls which **nodes** a pod **can (or prefers to)** run on.

### ✅ Hard Requirement

```yaml
spec:
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
        - matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
```
### 🟡 Soft Preference

```yaml
spec:
  affinity:
    nodeAffinity:
      preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 1
        preference:
          matchExpressions:
          - key: disktype
            operator: In
            values:
            - ssd
```
### 👥 Pod Affinity

Schedules pods close to other pods (on the same node or topology).

```yaml
spec:
  affinity:
    podAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchLabels:
            app: web
        topologyKey: "kubernetes.io/hostname"
```
`topology key:` defines scope (e.g. node, zone).

### 🚫 Pod Anti-Affinity
Prevents pods from running close to certain other pods.
```yaml
spec:
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - labelSelector:
          matchLabels:
            app: web
        topologyKey: "kubernetes.io/hostname"
```
This ensures better fault tolerance (e.g., spreading replicas across nodes).

