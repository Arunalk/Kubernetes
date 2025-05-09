# Vertical Scaling in Kubernetes

Vertical Scaling refers to adjusting the **resource limits** (CPU, memory) of a pod running in a Kubernetes cluster, rather than adding or removing pods. This scaling ensures that the pods have the right amount of resources allocated to them based on their workload demands. Vertical scaling can be done either manually or automatically using the **Vertical Pod Autoscaler (VPA)**.

### Vertical Pod Autoscaler (VPA) Modes

Vertical Pod Autoscaler (VPA) has four modes that define how it adjusts the resource requests of pods:

1. **Off**  
   - In this mode, the VPA only **provides recommendations** for resource requests (CPU, memory) but does not take any actions to apply those recommendations. 
   - Useful for monitoring resource needs and making manual adjustments based on the suggestions.
   - This mode does not change the resource requests of any pods.

2. **Initial**  
   - The **Initial** mode sets the resource requests **only when a pod is first created**. 
   - It does not alter the resource requests of running pods. So, it is useful when you want to ensure that new pods are created with proper resource allocation.
   - **Use case**: Best for environments where you want to control initial resource requests but not modify running pods.

3. **Auto**  
   - In this mode, the VPA automatically adjusts the **resource requests** of running pods based on their usage patterns. 
   - It ensures that pods use appropriate resources (CPU, memory) dynamically, without user intervention. If necessary, it may **recreate the pods** to apply the new resource settings.
   - **Use case**: Ideal for applications where the workload varies over time, and you want Kubernetes to adjust resources automatically.

4. **Recreate**  
   - The **Recreate** mode works similarly to the **Auto** mode but with the additional step of **terminating and recreating pods** with the updated resource requests.
   - This mode ensures that pods with outdated resource configurations are replaced with new ones that have the correct resource requests.
   - **Use case**: Best for scenarios where it is essential to apply resource changes immediately and for new configurations to be enforced across the deployment.

### When to Use Vertical Scaling

- **Vertical Scaling** is helpful when you want to adjust the resource allocation (CPU, memory) of a pod based on its changing needs rather than adding or removing pods.
- It is commonly used in environments where workloads have varying resource consumption over time but do not necessarily require scaling the number of pods.

### Key Takeaways

- **Off**: Only provides recommendations.
- **Initial**: Sets resource requests only when a pod is created.
- **Auto**: Automatically adjusts resource requests for running pods.
- **Recreate**: Terminates and recreates pods with updated resource requests.

`Example:`

```
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: example-vpa
  namespace: default
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: example-deployment
  updatePolicy:
    updateMode: "Auto"  # Can be Off, Initial, Auto, or Recreate
```