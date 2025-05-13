## VPC Core Components

1. **Region**  
   - A VPC is **regional**, meaning it exists within a single AWS region.

2. **CIDR Range (Classless Inter-Domain Routing)**  
   - You assign **IPv4 and/or IPv6 address ranges** to the VPC.
   - Defines the IP address space for the entire VPC.

3. **Subnets**  
   - The VPC address range is **divided into subnets**.
   - Subnets are mapped to **Availability Zones (AZs)**.

4. **Route Tables**  
   - Define **how traffic flows** within the VPC.
   - Can have **custom route tables** at the subnet level to control routing behavior.

5. **Internet Gateway (IGW)**  
   - Enables **internet access** for resources in the VPC.
   - Must be attached to the VPC and routed via route tables for public access.

---

## Security of the Network (2 Firewalls)

1. **Security Groups**  
   - Act as **virtual firewalls at the instance level**.
   - Control **inbound and outbound traffic** for **EC2 instances**.
   - **Stateful:** Return traffic is automatically allowed.

2. **Network ACLs (Access Control Lists)**  
   - Operate at the **subnet level**.
   - Apply rules to **all resources** within the subnet.
   - **Stateless:** Return traffic must be explicitly allowed.

---

## DNS in VPC

- **Route 53 Resolver**  
  - Handles **DNS resolution for EC2 instances** inside the VPC.
  - Automatically resolves domain names (e.g., AWS service endpoints or external domains).
