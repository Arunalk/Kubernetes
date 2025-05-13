# Shadow Deployment in Kubernetes

## What is Shadow Deployment?

**Shadow Deployment** is a deployment strategy where a **new version** of an application is deployed alongside the **current stable version**, but **does not serve live user traffic**.  
Instead, **copies of real production requests** are sent to the new version ("shadow" version) **for testing purposes**, without the shadow service's responses ever affecting real users.

It’s like your new app is "listening" in on production traffic but **without impacting users** at all.

---

## Why Use Shadow Deployment?

- **Safe Testing**: Test how a new version behaves under real-world production load without risking production stability.
- **Performance Validation**: Measure performance metrics such as response time, error rates, or memory usage under real traffic.
- **Behavior Verification**: Ensure that logic changes (e.g., new features, refactoring) behave correctly.
- **Infrastructure Changes**: Validate backend infrastructure changes (like new databases, caching systems) safely.

---

## When to Use Shadow Deployment?

- When you want to **test at full production scale** but can't risk affecting users.
- When migrating to a **new architecture**, **new framework**, or **backend service**.
- When doing **performance benchmarking** or **load testing** in production conditions.
- When validating **critical business logic changes** before official release.

---

## Benefits of Shadow Deployment

- **Zero Risk to Users**: Even if the shadow app crashes or returns errors, users are unaffected.
- **Real Traffic Testing**: No need to simulate traffic — you test using real user patterns.
- **Early Issue Detection**: Catch bugs, performance issues, and unexpected behavior before users ever see it.
- **Continuous Validation**: You can continuously run shadows for newer versions without major operational impact.

---

## Drawbacks of Shadow Deployment

- **Resource Overhead**: Shadow apps consume CPU, memory, and bandwidth even though they aren't serving users.
- **Traffic Duplication Complexity**: Properly duplicating real traffic (especially POST requests, sessions, authentication tokens) can be tricky.
- **Monitoring Complexity**: Requires separate monitoring pipelines to analyze the shadow application's performance.
- **Silent Failures**: Since shadow apps don't respond to users, failures might go unnoticed unless well-monitored.

---

## Shadow Deployment Architecture

Typically, the architecture looks like:

``User Request | |--> Live App (serves response to user) | |--> Shadow App (observes request, processes internally, discards response)``


---

## Example: Shadow Deployment in Kubernetes (Using Istio)

With **Istio** (a service mesh), you can easily create a shadow deployment by mirroring traffic.

### Step 1: Deploy Live and Shadow Versions

**Live Deployment (v1)**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app-v1
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
      version: v1
  template:
    metadata:
      labels:
        app: my-app
        version: v1
    spec:
      containers:
      - name: my-app
        image: my-app:v1
        ports:
        - containerPort: 80
```
**Shadow Deployment (v2)**

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app-v2
spec:
  replicas: 3
  selector:
    matchLabels:
      app: my-app
      version: v2
  template:
    metadata:
      labels:
        app: my-app
        version: v2
    spec:
      containers:
      - name: my-app
        image: my-app:v2
        ports:
        - containerPort: 80

```

### **Step 2: Kubernetes service: Service for both versions**

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-app
spec:
  selector:
    app: my-app
  ports:
  - port: 80
    targetPort: 80

```
### **Step 3: Configure Istio VirtualService for Traffic Mirroring : `VirtualService to route live traffic and mirror it`**

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: my-app
spec:
  hosts:
  - my-app.example.com
  http:
  - route:
    - destination:
        host: my-app
        subset: v1   # Live traffic goes to v1
    mirror:
      destination:
        host: my-app
        subset: v2   # Shadow traffic is mirrored to v2
    mirrorPercentage:
      value: 100.0  # Mirror 100% of traffic (can also mirror partial %)
```
