## **<span style="color:#A7C7E7;">DEPLOYMENTS</span>**

A Deployment in Kubernetes is a `higher-level controller` that manages ReplicaSets and Pods. It is used to deploy, update, scale, and rollback applications in a cluster efficiently.

💡 `Think of a Deployment as a manager for your applications:`

- It ensures the right number of pods are running.
- It allows rolling updates without downtime.
- It enables easy rollback if something goes wrong.
- It can automatically scale up/down based on demand.

**`Rolling Update:`**
    - To make sure that the app is not down</br>
    `How does it work?`

    1️⃣ A new ReplicaSet is created for the updated deployment.
    2️⃣ New pods start running under the new ReplicaSet.
    3️⃣ Old pods are gradually removed, keeping the application available.
    4️⃣ Once all old pods are replaced, the old ReplicaSet is scaled down to 0 pods, but it still exists in case of rollback.

### `Kubernetes Rolling Update History`

Kubernetes keeps track of **rolling update history** for a Deployment, allowing you to **view past changes, check previous ReplicaSets, and roll back if needed**.

---

### 📌 `Viewing Rolling Update History`

### 1️⃣ `Check the Rollout History`
To see the previous revisions of a deployment:
```sh
kubectl rollout history deployment my-app
```

#### **Example Output:**
```
REVISION  CHANGE-CAUSE
1         Initial deployment
2         Updated image to my-app:v2
3         Updated memory limits
```

ℹ️ If you don’t see a **CHANGE-CAUSE**, it means no `--record` flag was used when updating.

### 2️⃣ `View Details of a Specific Revision`
```sh
kubectl rollout history deployment my-app --revision=2
```
This command shows the details of **revision 2**, including **image versions, resource limits, and changes made**.

---

## 🔄 Rolling Back to a Previous Version

### 1️⃣ `Roll Back to the Last Stable Version`
```sh
kubectl rollout undo deployment my-app
```
✅ This reverts the deployment to the last successful version.

### **2️⃣ Roll Back to a Specific Revision**
```sh
kubectl rollout undo deployment my-app --to-revision=2
```
✅ This rolls back to **revision 2**.

---

### 📌 `Ensuring Change History is Recorded`

When updating a deployment, **use `--record`** so Kubernetes tracks what changes were made.

Example:
```sh
kubectl set image deployment my-app my-container=my-app:v2 --record
```
Now, when you check `kubectl rollout history`, you will see a **clear change history**.

---

### 🔍 `Checking ReplicaSets in Update History`

Since each update creates a **new ReplicaSet**, you can list them:
```sh
kubectl get rs
```
This command shows old ReplicaSets from previous versions.

If needed, you can manually **delete old ReplicaSets**:
```sh
kubectl delete rs my-app-old123
```

---


`DEPLOYMENT YAML`

# Kubernetes Deployment YAML Fields

This document explains the key fields in a **Kubernetes Deployment YAML** file without specific values, providing descriptions instead.

---

## **📌 Deployment YAML Structure**

### **1️⃣ apiVersion**
```yaml
apiVersion: 
```
- Specifies the **Kubernetes API version** used for the Deployment.
- Common value: `apps/v1`.

### **2️⃣ kind**
```yaml
kind: 
```
- Defines the **type of Kubernetes resource**.
- In this case, it is `Deployment`.

### **3️⃣ metadata**
```yaml
metadata:
  name: 
  labels:
    key: value
  annotations:
    key: value
```
- **Contains identifying information** about the Deployment.
- **`name`** → Unique identifier for the Deployment.
- **`labels`** → Key-value pairs to organize and select resources.
- **`annotations`** → Stores additional metadata (e.g., rollout history, deployment tracking).

### **4️⃣ spec**
```yaml
spec:
  replicas: 
  revisionHistoryLimit: 
  progressDeadlineSeconds: 
```
- Defines the **desired state** of the Deployment.
- **`replicas`** → Number of pod instances to run.
- **`revisionHistoryLimit`** → Number of old ReplicaSets to retain for rollback.
- **`progressDeadlineSeconds`** → Maximum time allowed for an update to complete before it’s considered failed.

### **5️⃣ selector**
```yaml
selector:
  matchLabels:
    key: value
```
- Ensures the Deployment **manages the correct pods**.
- **`matchLabels`** → Must match labels in `template.metadata.labels`.

### **6️⃣ template**
```yaml
template:
  metadata:
    labels:
      key: value
```
- Defines the **pod template** for the Deployment.
- Includes metadata and pod specifications.

### **7️⃣ spec (Inside template)**
```yaml
spec:
  imagePullSecrets:
    - name: 
```
- **Specifies how the pod pulls images** from private registries.

### **8️⃣ containers**
```yaml
containers:
  - name: 
    image: 
    imagePullPolicy: 
    ports:
      - containerPort: 
```
- Defines **the container(s) running inside the pod**.
- **`name`** → Name of the container.
- **`image`** → Docker image used for the container.
- **`imagePullPolicy`** → Defines when the image should be pulled.
- **`ports`** → Specifies exposed ports.

### **9️⃣ Probes (Health Checks)**
```yaml
readinessProbe:
  httpGet:
    path: 
    port: 
  initialDelaySeconds: 
  periodSeconds: 

livenessProbe:
  httpGet:
    path: 
    port: 
  initialDelaySeconds: 
  periodSeconds: 
```
- **Readiness Probe** → Checks if the container is ready to serve traffic.
- **Liveness Probe** → Checks if the container is still running.

### **🔟 Resources (CPU & Memory Limits)**
```yaml
resources:
  requests:
    cpu: 
    memory: 
  limits:
    cpu: 
    memory: 
```
- **Requests** → Minimum resources the container needs.
- **Limits** → Maximum resources the container can use.

### **🔟 Deployment Strategy**
```yaml
strategy:
  type: 
  rollingUpdate:
    maxSurge: 
    maxUnavailable: 
```
- **Defines how updates happen**.
  - Kubernetes provides different strategies for updating pods in a deployment. The two main strategies are:

    1️⃣ RollingUpdate (Default Strategy)
    Gradually replaces old pods with new ones, ensuring zero downtime.
    New pods are created before old ones are terminated.

    2️⃣ Recreate Strategy
    Deletes all existing pods first, then creates new ones.
    Causes downtime because all pods are removed before new ones start.
    ```
    strategy:
    type: Recreate
    ```

- **RollingUpdate** → Ensures zero downtime by gradually replacing old pods.
- **`maxSurge`** → Number of extra pods that can be created during an update. → can be either percentage or integer
- **`maxUnavailable`** → Number of pods that can be unavailable during an update.

### **🔟 Revision History**
```yaml
revisionHistoryLimit: 
```
- Specifies the **number of old ReplicaSets to retain**.
- Helps in rolling back to previous versions if needed.
- Example: If `revisionHistoryLimit: 5`, Kubernetes will keep **5 old ReplicaSets** and delete older ones.

### **🔟 Deployment Status**
```yaml
status:
  conditions:
    - type: 
      status: 
      reason: 
      message: 
  replicas: 
  updatedReplicas: 
  unavailableReplicas: 
```
- **Tracks the current state of the Deployment**.
- **`conditions`** → Provides information about the Deployment’s progress.
- **`replicas`** → Total number of pods managed by the Deployment.
- **`updatedReplicas`** → Number of pods that have the latest update.
- **`unavailableReplicas`** → Number of pods that are not ready yet.

---

