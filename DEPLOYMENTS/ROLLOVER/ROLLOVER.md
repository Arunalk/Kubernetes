# 🚀 What is a "Rollover" in a Kubernetes Deployment?

**Rollover** isn’t an official Kubernetes term, but it’s often used informally to describe:

> A new rollout triggered *before the previous rollout has finished* — causing the deployment to “roll over” to the next version prematurely.

This usually happens when deployment specs (like image tags or environment variables) are updated repeatedly in quick succession.

---

## 📦 What Actually Happens During a Rollover?

Kubernetes handles rollouts using the **Deployment controller**, with a **RollingUpdate** strategy by default. Here's how a rollover plays out:

1. **Deployment is Updated**  
   You apply a new deployment config (new image, env var, etc.).

2. **Rolling Update Starts**  
   Pods are gradually replaced with the new version.

3. **New Change Before Completion**  
   Before the update finishes, you apply *another* change (new image or config).

4. **Deployment Starts Over**  
   Kubernetes cancels the previous rollout, updates the ReplicaSet again, and starts the new one.

**🧨 End Result:** Intermediate pods from the first rollout may be deleted before finishing, and new pods from the latest change begin deployment.

---

## 🔁 Why It's Called a Rollover?

Because the deployment essentially **"rolls over"** the in-progress rollout and starts over with the **most recent desired state**.

---

## 🎯 Use Case Scenarios

- 🚧 **Rapid Development**  
  Developers pushing updates frequently (e.g., CI/CD pipelines firing off back-to-back).

- 🧪 **Testing Canaries or Blue-Green Deployments**  
  Fast config/image switches can trigger rollover side effects.

- 🔄 **Mid-Rollout Changes**  
  Updating image tags, resource limits, or environment variables before the previous rollout completes.

---

## ⚠️ Drawbacks of Rollovers

- ❌ **Incomplete Rollouts**  
  Pods from a previous update might be killed before they pass readiness.

- 🧟 **Zombie ReplicaSets**  
  Intermediate versions linger, consuming resources unless cleaned.

- ⏳ **Inconsistent State**  
  Services may route traffic to both old and new versions during the transition.

- 🧪 **Testing Instability**  
  Harder to verify each version individually if updates happen too quickly.

---
