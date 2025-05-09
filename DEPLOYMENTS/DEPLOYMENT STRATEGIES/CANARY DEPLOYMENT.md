# Canary Deployment or Ramped Slow Rollout

A Canary Deployment is a deployment strategy used to release a new version of an application gradually by initially exposing it to a small subset of users or traffic. This allows developers to monitor the behavior of the new version in real-world conditions without affecting the entire user base. The goal of Canary Deployment is to reduce the risk of bugs, failures, or performance issues that could affect all users in a traditional full deployment.

The name "Canary Deployment" comes from the practice of using canaries in coal mines to detect dangerous gases. Similarly, the canary in a Canary Deployment is like the early tester — if it fails, the consequences are limited.

## How Canary Deployment Works

The process of a Canary Deployment typically follows these steps:

1. **Deploy the New Version**: A new version of the application is deployed alongside the old (stable) version, but only a small percentage of the traffic is directed to the new version. The rest of the traffic continues to go to the stable version.

2. **Gradual Traffic Shift**: Initially, a small subset (e.g., 5-10%) of the total traffic is routed to the canary version. As the application proves to be stable and error-free, the percentage of traffic going to the canary version is increased incrementally.

3. **Monitoring**: During this process, developers continuously monitor the canary version for any issues related to performance, reliability, or bugs. Metrics, logs, and user feedback are often used to assess the performance of the new version.

4. **Full Release or Rollback**: If the canary version performs well, traffic is gradually shifted to the canary until it becomes the primary version. However, if issues are detected during the canary phase, the traffic is rerouted back to the stable version, and the canary version can be rolled back or fixed.

5. **Complete Traffic Migration**: Once confidence in the canary version is high, it becomes the new stable version, and the old version is eventually phased out.

## Benefits of Canary Deployment

- **Reduced Risk**: By exposing a small portion of traffic to the new version, you minimize the potential negative impact of bugs or performance issues. Only a small subset of users are affected if something goes wrong.
  
- **Early Detection of Issues**: Canary Deployments allow teams to identify and resolve issues before they affect the entire user base. Issues like performance degradation, security vulnerabilities, and bugs can be detected early.
  
- **Continuous Feedback**: Canary Deployment provides real-world data and feedback on the new version's performance. This allows developers to make data-driven decisions about whether to roll out the update more broadly or roll it back.
  
- **Flexibility**: It allows you to experiment with new features in a controlled manner. This is especially useful in testing new features, optimizations, or configurations before fully releasing them to all users.
  
- **Incremental Rollouts**: You can gradually increase the exposure to the new version. This approach helps maintain service availability and ensures that the deployment process is smooth and can be paused or adjusted as necessary.

## Drawbacks of Canary Deployment

- **Complex Traffic Routing**: Canary Deployments require sophisticated traffic management strategies. This can be tricky to implement with basic Kubernetes Ingress controllers. More advanced solutions like Istio or NGINX Ingress controllers may be required to manage weighted traffic routing effectively.
  
- **Resource Consumption**: Running two versions of the application simultaneously (the stable and canary versions) consumes additional resources, such as CPU and memory. This can increase costs, particularly if the number of canaries or the overall application scale is large.
  
- **Possible User Confusion**: If users experience different versions (stable vs. canary), it can lead to inconsistent experiences across the application. This is especially problematic if users are not aware that they are interacting with a canary version.
  
- **Monitoring Overhead**: The monitoring and logging required to track the performance of the canary version can be resource-intensive. Detailed metrics, error tracking, and performance monitoring are crucial to ensure the success of the canary deployment.
  
- **Manual Traffic Shifting**: In some cases, manual intervention might be required to adjust the traffic split. This can complicate the deployment process unless automated traffic management tools are in place.

## Use Cases for Canary Deployment

- **Feature Rollouts**: You can use Canary Deployments to introduce new features gradually. This allows you to test new functionality on a small group of users before rolling it out to everyone.
  
- **Performance Improvements**: If you are deploying performance improvements, a Canary Deployment allows you to test whether the changes improve performance without affecting all users immediately.
  
- **Bug Fixes or Security Patches**: When deploying bug fixes or security patches, Canary Deployments can help ensure that the fixes don’t cause unexpected side effects by testing them with a subset of users first.
  
- **A/B Testing**: Canary Deployments can also be used for A/B testing, where you serve two different versions of an application to different user segments and monitor their behavior and feedback.
  
- **Infrastructure Changes**: If you're making changes to infrastructure (such as database migrations or configuration updates), Canary Deployments provide a safe way to verify that the new infrastructure setup works correctly before fully transitioning all traffic.

## Canary Deployment in Kubernetes: Setup Example

In Kubernetes, a Canary Deployment can be achieved by using Deployment objects, Services, and Ingress controllers that support traffic splitting. Here's how a Canary Deployment might look in practice:

### Example 1: Canary Deployment with NGINX Ingress Controller

In this example, we use NGINX as an ingress controller to split traffic between the stable and canary versions of a service.

**`Stable Deployment`**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: stable-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
      version: stable
  template:
    metadata:
      labels:
        app: my-app
        version: stable
    spec:
      containers:
      - name: my-app
        image: my-app:v1

```

**`Canary Deployment (v2):`**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: canary-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: my-app
      version: canary
  template:
    metadata:
      labels:
        app: my-app
        version: canary
    spec:
      containers:
      - name: my-app
        image: my-app:v2
```

**`Stable Deployment Ingress`**

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: base-ingress
spec:
  ingressClassName: nginx
  rules:
  - host: canary.echo.pod.name.com
    http:
      paths:
      - pathType: Prefix
        path: /
        backend:
          service:
            name: base-svc
            port:
              number: 80
```
**`Canary Deployment Ingress:`**

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: canary-ingress
  annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: "30"
spec:
  ingressClassName: nginx
  rules:
  - host: canary.echo.pod.name.com
    http:
      paths:
      - pathType: Prefix
        path: /
        backend:
          service:
            name: canary-svc
            port:
              number: 80
```

# Canary Deployments with ALB in EKS

## 📌 Overview

Amazon EKS supports ALB (Application Load Balancer) integration through the **AWS Load Balancer Controller**, which provisions ALB resources via Kubernetes Ingress objects. While ALB itself doesn't support `canary-weight` annotations like NGINX, you can still implement **canary deployments** using alternative methods.

---

## 🚀 ALB in EKS

- Deployed using the **AWS Load Balancer Controller**
- Manages ALB resources through **Ingress** and **Service** definitions in Kubernetes
- Supports:
  - Path-based routing
  - Host-based routing
  - Header-based routing

---

## 🧪 Canary Deployment Strategies with ALB

### Option 1: Manual Canary Using Different Paths

You can define multiple `Ingress` rules with different paths:

```yaml
# Stable
path: /
backend: stable-service

# Canary
path: /canary
backend: canary-service
```
Testing the canary manually using different paths.

### Weighted Routing with AWS ALB Ingress Controller

#### Overview

In Kubernetes, the **AWS ALB Ingress Controller** allows you to route traffic to multiple services based on various conditions (e.g., path, header). However, the **Ingress resource** in Kubernetes does not natively support **weighted routing** between different services or target groups.

### Why Weighted Routing is Not Possible via Ingress YAML

The **Ingress resource** in Kubernetes primarily provides **routing logic** based on **path-based** or **header-based** conditions. It doesn't directly support the concept of **weighted traffic distribution** between multiple target groups, which is needed for things like **Canary deployments** or **gradual traffic shifting**.

Here are the reasons why **weighted routing** cannot be directly defined in **Ingress YAML**:

1. **Limited Routing Logic in Ingress Resource**:
   - Kubernetes **Ingress** resources allow you to define simple routing rules based on **paths** or **headers**. For example, you can route traffic to a service if the path is `/api/v1`, or if the request header contains `X-Canary: true`.
   - **Ingress** does not have an option to specify traffic weights (e.g., 80% of traffic to one target group, 20% to another), which is required for canary deployments.

2. **Target Groups Are Registered via Services**:
   - When you define services in Kubernetes and associate them with an ALB Ingress, the **target groups** for those services are automatically registered by the AWS ALB Ingress Controller.
   - However, the **weights** assigned to each target group are not configurable in the **Ingress YAML**. The weight-based distribution of traffic between target groups must be managed externally after the resources are created.

3. **Lack of Native Weighted Traffic Features in ALB Ingress Controller**:
   - The **ALB Ingress Controller** does not natively support **weighted routing** in the same way that you might use tools like **AWS CodeDeploy** or **App Mesh** to perform traffic shifting with weights.

## Solution: Using AWS CLI or Terraform for Weighted Routing

While you cannot directly specify weighted routing in the **Ingress YAML**, you can achieve **weighted traffic distribution** by **modifying ALB listener rules** after the Kubernetes resources are created. This can be done using the **AWS CLI** or **Terraform**.

### 1. **Using AWS CLI to Modify Listener Rules**

After deploying the **Ingress** resource and creating the services (which map to target groups), you can modify the listener rules on the ALB to introduce weighted routing.

#### Example AWS CLI Command to Modify Listener Rule:

```bash
aws elbv2 modify-rule \
  --rule-arn arn:aws:elasticloadbalancing:region:account-id:listener-rule/app/my-alb/arn:aws:elasticloadbalancing:region:account-id:rule/abcd1234 \
  --actions Type=forward,ForwardConfig='{
    "TargetGroups":[
      {"TargetGroupArn":"arn:aws:elasticloadbalancing:region:account-id:targetgroup/stable/abcd1234","Weight":80},
      {"TargetGroupArn":"arn:aws:elasticloadbalancing:region:account-id:targetgroup/canary/abcd1234","Weight":20}
    ]
  }'
```