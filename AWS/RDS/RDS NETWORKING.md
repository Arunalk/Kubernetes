# AWS RDS Networking & Deployment Best Practices

## RDS and VPC

- **Amazon RDS runs within a VPC** (Virtual Private Cloud) for network isolation and control.
- While RDS *can* be launched in the **default VPC**, it’s **not recommended** due to:
  - Default VPC often includes **public subnets**, making it less secure.
  - For security reasons, **databases should be placed in private subnets**, which are not accessible from the internet.

---

## VPC, Subnets, and CIDR

- **CIDR Range (Classless Inter-Domain Routing)** defines the range of IP addresses available in a VPC.
- **Subnets** are subdivisions of the CIDR range and help separate different types of workloads.
  - Example: App servers in public subnet, databases in private subnet.
- **Private Subnets**:
  - Not accessible from the public internet.
  - Ideal for databases like RDS.

---

## Availability and High Availability

- RDS can be deployed across **multiple Availability Zones (AZs)** to ensure **high availability**.
- To support multi-AZ deployments, we create **DB Subnet Groups** that span at least **two subnets in different AZs**.

---

## RDS Access from EC2

- An **EC2 instance** (such as one running a web application) often acts as the **database client**.
  - EC2 is typically placed in a **public subnet** to serve frontend traffic.
  - RDS resides in a **private subnet** for security.

### **Cost Optimization**
- Placing EC2 and RDS in the **same Availability Zone** minimizes **data transfer costs**.

---

## DNS vs IP Address for RDS Connection

- **Do not use IP addresses** to connect to RDS.
  - RDS instances can failover, and their **IP address may change**.
- **Use the DNS endpoint** provided by AWS:
  - It stays the same even if the underlying IP changes.
  - Ensures application reliability during failovers or maintenance events.

---

## Summary

| Component         | Placement             | Reason                                                                 |
|------------------|------------------------|------------------------------------------------------------------------|
| RDS              | Private Subnet         | Security — avoid public access                                         |
| EC2 (Web Server) | Public Subnet          | Needs internet access for frontend traffic                             |
| Subnet Groups    | Multiple AZs           | High availability for RDS                                              |
| Connection       | Use DNS, not IP        | IPs change on failover; DNS remains stable                             |
| Networking       | Avoid Default VPC      | It often includes public subnets — not ideal for private RDS setup     |
