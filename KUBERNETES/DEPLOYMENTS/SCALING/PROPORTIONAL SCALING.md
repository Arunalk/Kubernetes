## Proportional Scaling During Rolling Update in Kubernetes

Proportional scaling during a rolling update ensures that when a Deployment's replica count is increased or decreased, Kubernetes distributes the new replicas proportionally between the old and new ReplicaSets. This helps maintain balance and minimizes disruption.

### How Proportional Scaling Works:

1. **Rolling Update**:
   When a new version (e.g., new container image) is applied to a Deployment, Kubernetes creates a new ReplicaSet for the updated version. The old ReplicaSet is not immediately removed, and the traffic is gradually shifted to the new ReplicaSet.

2. **Proportional Scaling**:
   If the Deployment is scaled during the rolling update, Kubernetes will distribute the additional replicas proportionally between the old and new ReplicaSets based on their current replica counts:
   - **More Replicas for the Larger ReplicaSet**: Additional replicas are added to the ReplicaSet with more replicas.
   - **Fewer Replicas for the Smaller ReplicaSet**: Fewer replicas are added to the ReplicaSet with fewer replicas.
   - **Zero-replica ReplicaSets**: ReplicaSets with zero replicas are not scaled up until they are healthy.

### Example Scenario:

**Deployment Settings**:
- Desired replicas: `10`
- maxSurge: `3`
- maxUnavailable: `2`

#### Before Update:
- **Old ReplicaSet**: `nginx-deployment-618515232` has `8` replicas running.
- **New ReplicaSet**: `nginx-deployment-1989198191` starts with `0` replicas.

#### During Update:
- **Deployment Scaled to 15 replicas**:
  - **Proportional Scaling**: Kubernetes will add `3` replicas to the old ReplicaSet and `2` replicas to the new ReplicaSet, based on the current state.

### Key Points:
- **maxSurge** and **maxUnavailable** control the number of Pods added or removed during the update.
- **Proportional scaling** balances replicas between old and new ReplicaSets based on their current state.
- **Zero-replica ReplicaSets** will not be scaled up until they are healthy.

### Why It’s Important:
Proportional scaling helps ensure that the update process is smooth and minimizes downtime by distributing replicas evenly across ReplicaSets, avoiding resource overload in any one ReplicaSet.

