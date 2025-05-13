# 🚦 Pod Readiness Gates in Kubernetes</br>

### 🧩 `What Are Readiness Gates?`
Readiness Gates are custom conditions added to a Pod's readiness status. They extend the default readiness checks (like readinessProbes) to include external or application-specific signals.

> ✅ A Pod is considered Ready only when all conditions in its Readiness Gates evaluate to True.

### 🧠 `Why Use Readiness Gates?`
Use Readiness Gates when:

- Your app needs time to register with a service mesh or load balancer.

- You rely on external controllers (like Istio or AWS VPC CNI) to determine readiness.

- You want to decouple business logic readiness from container health checks.

🛠 `How to Define a Readiness Gate
You define readiness gates in the pod.spec.readinessGates field:`

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-pod
spec:
  containers:
  - name: my-app
    image: my-app-image
  readinessGates:
  - conditionType: "mycompany.com/registered"
```

An external controller or custom process will then set this condition using the Kubernetes API:

```yaml
status:
  conditions:
  - type: "mycompany.com/registered"
    status: "True"
```

### 🌐 `Network Readiness Gates (e.g., AWS VPC CNI)`

One special type of readiness gate is network readiness, especially with advanced CNI plugins like AWS VPC CNI or service meshes like Istio.

📡 AWS VPC CNI Example
AWS VPC CNI uses readiness gates like:

```yaml
readinessGates:
- conditionType: "vpc.amazonaws.com/pod-eni"
```
This condition ensures the Pod has a secondary ENI/IP address attached and is network-ready before it is marked Ready. Until the VPC CNI plugin sets the pod-eni condition to True, the Pod won't receive traffic.

✅ `When Is This Useful?`
- Pods that rely on specific networking setups.
- Latency-sensitive applications (like financial or gaming apps).
- To avoid sending traffic before ENI/IP addresses are fully provisioned.

