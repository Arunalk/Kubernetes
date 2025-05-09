# 🌐 Kubernetes Pod Topology Spread Constraints (PTSC)

Use **Pod Topology Spread Constraints** to **distribute pods evenly across nodes, zones, racks**, or other topology domains — improving availability and fault tolerance.

---

## ✅ Basic Example: Spread Across Nodes

```yaml
spec:
  topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: "kubernetes.io/hostname"
    whenUnsatisfiable: DoNotSchedule
    labelSelector:
      matchLabels:
        app: myapp
```
### 🔍 Field Breakdown

| Field               | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `maxSkew`          | Maximum allowed difference in number of matching pods across topology domains |
| `topologyKey`      | Node label key to define topology (e.g. `kubernetes.io/hostname`, `zone`)   |
| `whenUnsatisfiable`| `DoNotSchedule` (strict) or `ScheduleAnyway` (best-effort)                  |
| `labelSelector`    | Selects which pods the spread rule applies to                               |

### 🚀 Spread Across Zones Example

```yaml
spec:
  topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: topology.kubernetes.io/zone
    whenUnsatisfiable: DoNotSchedule
    labelSelector:
      matchLabels:
        app: frontend
```