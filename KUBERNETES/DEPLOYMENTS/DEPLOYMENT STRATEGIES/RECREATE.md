## RECREATE/REPLACEMENT STRATEGY

`What it does:`
Deletes all existing pods before creating new ones.

`Impact:`
Causes downtime, as there’s a gap between old pods being removed and new ones becoming ready.

`Use Case:`
Useful when the user wants to clean up the previous version completely before deploying changes — particularly in scenarios where:

Some pods are in an error state, and those problematic pods don’t impact customers, so it’s acceptable to remove them during the next deployment.

`Why RECREATE helps here:`
Since rolling strategies don’t touch pods stuck in bad states, RECREATE ensures a clean slate by forcefully removing all existing pods, including the problematic ones.


---
**`RollingUpdate Behavior with Unhealthy Pods:`**
- RollingUpdate only replaces pods that are considered "available" (i.e., passing readiness probes).

- If a pod is not ready (e.g., it's stuck in CrashLoopBackOff), the Deployment controller might wait indefinitely, depending on the maxUnavailable setting.

- As a result, unhealthy pods can stall the rollout.

- Zombie pods can persist (temporarily) during a rollout if:

- They're failing readiness/liveness probes.

- They're not being automatically cleaned up because of limits like `maxSurge` and `maxUnavailable`.

RollingUpdate does not aggressively replace "bad" pods unless they're entirely removed or fail beyond a certain point.
---

🧟 `When Do Pods Become Zombies?`

> 1. `RollingUpdate Didn't Replace It
During a rolling update`:
> - Only Ready pods are gradually replaced.
> - If a pod is stuck in a CrashLoopBackOff or some non-ready state, it might not be terminated right away.
> - Kubernetes says, “This pod isn’t contributing to availability, but I still need to maintain N replicas that are.”
> - `Result:` The broken pod just sits there doing nothing = zombie.</br>
> 🔍 `Note:` Kubernetes won’t delete non-ready pods until it has healthy replacements — so they linger.
> 2. Orphaned Pods After Node Crash
> - If a node dies, and the pod’s status doesn’t get updated quickly:
> - The pod might appear to still be “Running” in the cluster.
> - But the node is gone — so it’s really dead.
> - Until the node controller marks the node as “NotReady” and removes pods, these are zombies.
> 3. Failed Termination
> - Sometimes, pods get stuck in a Terminating state:
> - A kubectl delete pod was issued,
> - But a container inside is hanging (e.g., due to a long shutdown or hung process),
> - Kubernetes waits for the grace period, and if it doesn't stop, it force-kills it.