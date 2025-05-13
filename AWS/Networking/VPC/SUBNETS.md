## Subnets in AWS VPC

Subnets are **logical subdivisions of a VPC's CIDR block**. They define **which Availability Zone (AZ)** your AWS resources reside in and help structure the network layout.

---

### Types of Subnets

#### **Public Subnet**

- A subnet is considered **public** if its route table has a route to the **Internet Gateway (IGW)**.
- **Instances with public IP addresses** in this subnet can communicate with the internet.
- Used for resources that require internet access, such as:
  - **Load balancers**
  - **Web servers**
  - **NAT Gateways**

#### **Private Subnet**

- A subnet without a route to the Internet Gateway is **private**.
- Instances here **do not have direct access** to the internet.
- Ideal for resources that must not be publicly accessible, such as:
  - **Databases**
  - **Application servers**
- These instances can still **access the internet indirectly** using a **NAT Gateway** or **NAT Instance** in a public subnet.

---

### AWS Reserved IP Addresses per Subnet

Whenever a subnet is created, **5 IP addresses are reserved by AWS**:

- **.0** – Network address
- **.1** – Reserved for VPC router
- **.2** – Reserved for AWS DNS
- **.3** – Reserved for future use
- **.255** – Network broadcast address

This means the **usable IPs = total IPs - 5**.

**Example**:  
If you need **at least 29 usable IPs**, choose a **/27 CIDR block**, which provides **32 total IPs**, of which **27 are usable**.

---

### Summary

- Subnets are mapped to **Availability Zones**.
- **Public subnets** require:
  - Route to **Internet Gateway**
  - **Public IP** assigned to instance
- **Private subnets** use **NAT Gateway** for internet-bound traffic.
- Plan subnet size keeping **AWS's 5 IP reservation** in mind.
