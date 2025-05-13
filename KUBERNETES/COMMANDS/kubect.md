## Kubectl commands

**1. List Resources**

```
kubectl get pods
kubectl get deployments
kubectl get rs
```
**1. List ALl Resources**
```
kubectl get all
```
**2. Get Pods with more detail (IP, Node, etc.)**
```
kubectl get pods -o wide
```

**3. List all Nodes**
```
kubectl get nodes
```

**List Nodes with specific label:**

```
kubectl get nodes -l tenant=dogfood
```

**Restart a Deployment (e.g., after ConfigMap/Secret change):**

```
kubectl rollout restart deployment <deployment-name>
```

**Describe a pod (for detailed troubleshooting):**

```
kubectl describe pod <pod-name>
```

**Get logs from a pod:**

```
kubectl logs <pod-name>
```
**Execute a command inside a running container:**

```
kubectl exec -it <pod-name> -- /bin/bash
```

**Apply a manifest file:**
```
kubectl apply -f myapp.yaml
```

**Port forward a pod to localhost:**

```
kubectl port-forward pod/<pod-name> 8080:80
```