## **`REPLICA SETS`**

- A ReplicaSet in Kubernetes is a controller that ensures a specified number of `identical pod replicas are always running in the cluster`. If a pod crashes or is deleted, the ReplicaSet automatically creates a new pod to maintain the desired count.

**Key Features:**

- Ensures a fixed number of pod replicas are running.
- Automatically replaces failed or terminated pods.
- Works by selecting pods using labels.

- `Why Must Labels Match the Selector?`
    - A ReplicaSet uses a selector to find and manage pods. The selector ensures that:

        - Only the correct pods are managed → The ReplicaSet should not control unrelated pods.
        - It can scale and replace pods properly  → If a pod is deleted, the ReplicaSet creates a new one with the same label.
        - Existing pods aren’t duplicated → If labels don’t match, the ReplicaSet might not recognize existing pods and may create extra replicas.

```
spec:
  selector:
    matchLabels:
      app: my-app  # Matches pod label

  template:
    metadata:
      labels:
        app: my-app  # Same label as selector
```
---
### `Challenges with ReplicaSets`:

- `No Automated Updates to Pods (Configuration or Image Changes)`

    - ReplicaSets do not perform rolling updates automatically. If you change the image or configuration of the container, ReplicaSets won't apply those changes until the pods are deleted and recreated manually.

       -   For instance, if you update the Docker image tag in the ReplicaSet’s pod spec, ReplicaSet doesn’t automatically update running pods with the new image.

      - Instead, it would still keep running the old pods until they are terminated (e.g., due to a crash), but new pods created after termination will get the updated configuration.

- `No Rolling Updates or Zero Downtime Updates`

  - ReplicaSets lack the built-in ability to perform rolling updates (like gradually replacing pods with new ones to ensure availability).
    - You would need to handle this yourself, using manual processes to delete old pods and create new ones.</br>
    - This can result in downtime during updates, as there is no seamless update mechanism.

- `Label Collison with Replicaset Selectors` 

  - When a Replicaset selector mataches labels of pods that it didn't create, it starts trating those pods as a part of its managed set.  This causes unintended consequences. 

---
### **`Summary:`**
- ReplicaSets manage scaling by ensuring the desired number of pods are running.
- Manual scaling can be done with kubectl scale.
```
kubectl scale --replicas=10 rs/<replicaset-name>
```
- For automatic scaling, you use Horizontal Pod Autoscaler (HPA).