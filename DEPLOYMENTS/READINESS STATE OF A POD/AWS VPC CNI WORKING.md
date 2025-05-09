# 🧩 Amazon VPC CNI Plugin – Components & Workflow

Amazon VPC CNI is a Kubernetes CNI plugin specifically built for Amazon EKS. It assigns **VPC-native IP addresses** to pods, enabling direct and low-latency communication with AWS services and other pods.

---

## 📦 Components

### 1. CNI Binary
- A lightweight binary that runs on the node’s **root file system**.
- **Invoked by the kubelet** whenever:
  - A new Pod is added.
  - An existing Pod is removed.
- Responsibilities:
  - Set up the **Pod's network namespace**.
  - Create **veth pairs** for connectivity.
  - Assign an **IP address** from a warm pool.

### 2. ipamd (IP Address Management Daemon)
- A **long-running daemon** on each node.
- Responsibilities:
  - Manage **ENIs (Elastic Network Interfaces)**.
  - Maintain a **warm pool of available IP addresses or prefixes**.
  - Pre-allocate resources to speed up Pod startup.

---

## 🔁 How It Works

### 1. Primary ENI
- When an EC2 instance (node) is launched, a **primary ENI** is automatically attached.
- It gets its IPs from a **primary subnet**, which can be public or private.
- Pods using `hostNetwork: true` will share the **primary ENI's IP** and network namespace.

### 2. Warm Pool Allocation
- ipamd automatically allocates a **warm pool** of:
  - IP addresses (default mode), or
  - Prefixes (when **prefix delegation** is enabled).
- These are pulled from the subnet associated with the ENI.
- Warm pool helps reduce **latency** by keeping IPs ready for fast assignment.

### 3. Secondary ENIs
- When the **primary ENI** runs out of available IPs:
  - ipamd attaches additional **secondary ENIs** to the node.
  - Each ENI supports a limited number of IP addresses or prefixes (depends on **instance type**).
- More ENIs are attached as needed, up to the **ENI limit** of the instance.

### 4. Pod IP Assignment
- When a new pod is scheduled:
  - kubelet calls the CNI plugin.
  - CNI plugin requests an IP from ipamd.
  - ipamd allocates an IP from the **warm pool**.
  - The pod is connected to the VPC via a veth pair and becomes network ready.

---

## ⚙️ Pod IP Allocation Flow

```text
Pod scheduled on Node
      ↓
kubelet invokes CNI binary
      ↓
CNI calls ipamd for available IP
      ↓
ipamd assigns IP from warm pool
      ↓
CNI sets up Pod's network namespace
      ↓
Pod is network-ready with VPC-native IP
```