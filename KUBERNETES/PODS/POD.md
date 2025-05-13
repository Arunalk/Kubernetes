**PODS**

A Pod can contain one or more containers[which is nothing but a process it can be http website, wordpress, database process]. If a Pod contains multiple containers, they share the same network IP and port space, and can communicate with each other via localhost.
`Ideally it is preferred to have a single container pods.`

- Docker allows you to define a health check to monitor the health of a container. If the check fails, Docker marks the container as unhealthy, which can be useful for orchestrators like Kubernetes or Docker Swarm. </br>
    ```
        FROM nginx
        HEALTHCHECK --interval=10s --timeout=5s --retries=3 \
        CMD curl -f http://localhost || exit 1

    ```
- Container has health probes.
Kubernetes also performs health check on pods. We can write a shell-script to do health-check or it is a website, kubernetes will trying connecting to it.

**Kubernetes has built-in health probes similar to Docker:**</br>
`Why probes are essential?`</br>
When there is a malfunction in pods, the pods should get restarted. Probes functionality is to handle that:

- Liveness Probe – Checks if the application is still running.

- Readiness Probe – kuberntes ensures that the application is ready to serve traffic, by satisfying the condition mentioned in the readinessProbe

- Startup Probe – Checks if the application has started successfully.

**Sidecar container:**
A common use case for having multiple containers in a Pod with a shared network is the sidecar pattern. In this pattern, a primary container performs the main application logic, and a sidecar container provides additional functionality, such as logging, monitoring, or a proxy. These containers need to communicate directly with each other using the shared network.

---
**Types of Volumes:**
1. EmptyDir: A temporary volume that is created when a Pod is assigned to a node and deleted when the Pod is removed. It's commonly used for scratch data that doesn't need to be persisted.
2. PersistentVolume (PV) and PersistentVolumeClaim (PVC): These are used for long-term storage and are useful when you need to persist data even beyond Pod lifecycles. Persistent Volumes can be backed by a variety of storage systems (like cloud providers' block storage, NFS, etc.).
3. ConfigMap and Secret: Volumes that store configuration data and sensitive data like passwords, certificates, etc.
4. HostPath: A volume that maps to a file or directory on the host node, useful for accessing node-level files.

**What Data Do Pods Write to Volumes?**

1. `Application Data`: If you’re running a database, the application will write its data (e.g., table records, logs) to a volume to ensure persistence across Pod restarts.
2. `Logs:` Containers may write logs to a volume so that even if a container crashes, the logs persist. This is particularly important for debugging.
3. `Configuration Files:` Volumes can be used to store configuration files that are shared between containers. For instance, if one container runs a web app and another runs a caching service, they may both need access to the same configuration file.
4. `Cache Data:` Temporary data or cache from a web application may be stored in a volume.

---

1. **Shared networks:**
    
    - **Single IP Address:**

        All containers in the same Pod share a **single IP address**. This allows them to `communicate directly with each other as if they were running in the same host, using localhost`.

        For example, if you have two containers in the same Pod, one serving a web application and the other logging incoming traffic, the web container can simply send log data to localhost:8081 (if that’s the port the logging container is listening to) without needing to worry about networking complexities.

    - **Shared Ports:**

        Containers in a Pod cannot bind to the same port. Since they share the same network namespace, they need to manage ports in a way that avoids conflicts.

        If there are multiple containers within the same Pod, each container typically exposes different ports. However, these ports are within the same network namespace and are accessible using same localhost.


2. **Shared Storage Volumes in Pods:**

    **Why Use Shared Storage Volumes for Logs?**
    
    `Persistent Logs:` Containers in a Pod are ephemeral, meaning if the container crashes or is restarted, all of its data (including logs) will be lost. By using a shared volume, logs can be persisted even if the containers are restarted.

    `Centralized Log Access:` By using a shared volume, multiple containers in the same Pod can write to the same log files, making it easier for monitoring systems or external tools to access and process those logs.


    - **Persistent Data Storage:**

        By default, containers in Kubernetes are ephemeral. This means that any data stored in a container’s filesystem is lost if the container is restarted or deleted.

        Volumes provide a way to persist data beyond container restarts and allow data to be shared between containers in a Pod.

    - **Shared Across Containers in the Same Pod**

        When you define a volume in a Pod specification, all containers in that Pod can access and share the same volume.

        This makes volumes extremely useful for scenarios where multiple containers in a Pod need to access the same file system, such as shared logs, configuration files, or data.

    - **Volume Mounts:**
    
         You can mount a volume inside a container at a specified path, and any data written to that path will be stored in the volume. If multiple containers in the Pod mount the same volume, they can read from and write to the same storage, enabling data sharing.


---
**Selectors and labels on Pods:**

| Aspect           | Labels                                                   | Selectors                                                 |
|------------------|----------------------------------------------------------|-----------------------------------------------------------|
| **Definition**   | Key-value pairs used to attach metadata to objects       | Queries used to select a set of objects based on their labels |
| **Purpose**      | Organize and categorize objects (e.g., Pods, Services)   | Select groups of objects based on labels for actions like routing or scaling |
| **Usage**        | Attached to objects (e.g., Pods, Deployments)            | Used by controllers (e.g., Services, Deployments) to target objects |
| **Example**      | `labels: app=myapp, environment=production`              | `selector: app=myapp, environment=production`             |
| **Who Uses Them**| Kubernetes objects (e.g., Pods, Deployments)             | Controllers like Services, Deployments, ReplicaSets, etc.  |
| **Format**       | Key-value pairs                                          | Logical expression matching labels (e.g., `key=value`, `key in [value1, value2]`) |


- Kubernetes controllers (like Deployments, ReplicaSets, or Services) use selectors to identify which Pods they should manage or interact with. Here’s what that means:

    - Deployments: A Deployment uses a label selector to decide which Pods it manages. For example, a Deployment might be responsible for ensuring that exactly 3 replicas of Pods with a specific label (e.g., app=myapp) are running. If any of those Pods go down, the Deployment will automatically create new Pods to match the desired state.


**POD ATTRIBUTES:**

- Each Pod has its own localhost

   > Containers inside the same Pod can communicate using localhost.

- Each Pod gets a unique IP address

    > However, this IP is ephemeral and can change if the Pod is restarted or rescheduled.

- Pods run on different Nodes

    > A Pod on Node A cannot directly access a Pod on Node B using just localhost or the Pod IP, because the IP is internal to the cluster.

- Ports are Node-Specific

    > Multiple pods/services cannot use the same port on the same node. If a web service is running on port 80 on a Node, then only one service on that Node can use that specific port at the node level


`How to make a service highly available?`</br>
We increase pods not the containers inside a single pod

- It is usually not recommended to create pods using yaml. Pods are basically created via workload resources such as deployments, replicasets, jobs and cronjobs.


**POD LIFECYCLE**

1. `Pending:`
    > Node not available > ImagePullBackOff[If image not present in the registry, or if the secrets for accessing the registry is not valid] > Cluster AutoScaler taking time to spin new nodes

2. `Running`

3. `Successed or Failed`

4. `Unknown` : When there is problem with node or a control plane



**`POD YAML`**

1. apiVersion
2. kind
3. metadata:</br>
    - labels and selectors
4. spec:</br>
    -   `nodeSelector`:
        - If the company uses both linux and windows, then nodeSelector helps in scheduling the pods on nodes → this label will be present on nodes.
    - `containers`:
        - `name` → container name
        - `image` → image-registry-path
        - imagePullPolicy > recommended to have images with git commit hash while using CI/CD
        - `livenessProbe` → runs all the time to check the health of an app
            - port
            - path
            - initialdelayseconds → how much time it should wait for starting heath checks
            - periodseconds → time interval between each health checks 
        - `readinessProbe` → runs to ensure that app is ready to serve traffic by checking whether the app is accessible
            - port
            - path
            - initialdelayseconds → how much time it should wait for starting heath checks
            - periodseconds → time interval between each health checks 
        - `resource` → makes sure that resources such as memory and cpu are available on nodes. This makes scheduling of pods easier
            - `requests` → reserves the resources on a node
            - `limits` → max threshold that a pod can consume so that there will be no resource exhaustion. while setting memory is easy as we know the value but cpu is difficult as it works in cycle.



**`Image-policy`:**

- `Never:` 
    - Kubernetes will not try to pull the image from any registry.
    - The image must be present locally on the node.
- `Always:` 
    - Kubernetes will always pull the image from the registry, even if it is already present on the node.
    - Ensures the pod always gets the latest version of the image.
- `IfNotPresent:`
    - Kubernetes will pull the image only if it is not already present on the node.
    - If the image is available locally, Kubernetes does not pull from the registry.

**`NodeSelector:`**

- Useful for scheduling pods onto the right nodes.


## `📌 Pod Management Ways`

>       Deployments → Manage stateless applications with rolling updates.

>       ReplicaSets → Ensure a fixed number of pods are running.

>        StatefulSets → Manage stateful applications with stable identities.

>        DaemonSets → Run one pod per node for background tasks.

>        Jobs & CronJobs → Run one-time or scheduled tasks.

>        Static Pods → Run directly on nodes, independent of the API server.

>        Custom Controllers → Extend Kubernetes with custom logic.