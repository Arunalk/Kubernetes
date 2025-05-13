# **Elastic Network Interface (ENI)**

## **What is an ENI?**

An **ENI (Elastic Network Interface)** is the fundamental networking component in AWS that provides **IP addressing** and enables communication over a network.  
It acts as a **virtual network card** for EC2 instances inside a VPC.

---

## **Key Concepts**

- Every EC2 instance gets its **IP address** via an ENI.
- ENIs are **logical components** of the VPC.
- An **instance can have multiple ENIs**, depending on the instance type.
- ENIs are **bound to an Availability Zone (AZ)**.
  - An ENI in one AZ **cannot** be attached to an instance in another AZ.

---

## **ENI Properties**

- **Primary private IPv4 address** from the VPC CIDR.
- Optional **IPv6 address**, if VPC supports IPv6.
- Can have **multiple secondary IP addresses**.
- Can be assigned **Elastic IPs**.
- Attached **Security Groups** — the ones we attach to EC2 are actually tied to the ENI.
- A fixed **MAC address** — useful for licensing and identity.
- Has a **Source/Destination Check flag**:
  - **Disabled** for NAT instances, can be managed via the ENI.

---

## **Primary vs Secondary ENIs**

- **Primary ENI**:  
  Cannot be detached. Assigned at instance launch.

- **Secondary ENIs**:  
  Can be **detached and reattached** to other instances in the same AZ.  
  Useful for failover or high-availability scenarios.

---

## **How ENI Works**

1. **Attachment and IP Assignment**  
   - When an EC2 instance is launched, a **primary ENI** is automatically attached.
   - It receives:
     - A **private IP address** (mandatory)
     - An optional **public IP** (if enabled at launch)
     - Optional **Elastic IP** (if manually associated)

2. **Traffic Routing**  
   - All **network traffic** to/from the instance goes through the ENI.
   - Works with **VPC route tables** to determine path.
   - ENIs in public subnets can reach the internet if the **Internet Gateway** is configured and the route exists.

3. **Security**  
   - **Security groups** attached to the ENI control allowed traffic.
   - Since ENIs carry these rules, they **go with the interface** — not just the instance.

4. **Detach and Move**  
   - **Secondary ENIs** can be detached from one instance and attached to another (in the same AZ).
   - Useful in **failover**, **migration**, or **disaster recovery** use cases.

5. **Multiple ENIs per Instance**  
   - Depending on the EC2 type, you can have multiple ENIs to **segregate traffic**, support **different subnets**, or add **redundancy**.

---

## **Instance Type and ENI Limits**

- The **number of ENIs and IPs** per ENI depends on the **EC2 instance type**.  
  For example, **t3.medium** can support up to **3 ENIs** and **17 IP addresses**.

---

## **Use Cases**

1. **AWS-Managed Services (Requester Managed ENIs)**:
   - Services like **RDS** and **EKS** create ENIs inside your VPC to communicate with AWS-managed infrastructure.

2. **Dual-homed Instances**:
   - For communication between **public and private subnets**, or **on-premise networks via VPN**, by using:
     - One ENI in a **public subnet**
     - One ENI in a **private subnet**

3. **High Availability**:
   - If an instance fails:
     - Detach the ENI
     - Attach it to a **standby instance**
     - The IP address and MAC remain the same, minimizing client impact

4. **Secondary IPs for Pods (e.g., in EKS)**:
   - **Kubernetes Pods** running in AWS (e.g., via EKS) are often assigned **secondary IPs** from the ENI.

---

## **Summary**

ENIs provide flexibility and modularity in AWS networking.  
They are critical for advanced configurations like **multi-homed instances**, **HA failovers**, and **AWS service integration**.
