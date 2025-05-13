# **NAT Gateway (Network Address Translation)**

Used to enable **instances in private subnets** to **access the internet** for outbound traffic (e.g., installing updates, accessing APIs), while still being unreachable from the internet.

---

## **Key Characteristics**

- **Scope**: AZ (Availability Zone) level  
- **Placement**: Must be launched in a **Public Subnet**
- **Elastic IP**: Required for communication with the internet
- **Managed Service**: Fully managed by AWS, **highly available**, **automatically scalable**, **no monitoring or scaling needed**
- **Protocols Supported**: **TCP**, **UDP**, **ICMP**
- **Security Group**: **Not required**; governed by **Network ACLs**

---


## **How it Works**

1. An **instance in a private subnet** wants to connect to the internet (e.g., to access `google.com`).
2. The **route table** of the private subnet has a rule to forward outbound traffic (e.g., `0.0.0.0/0`) to the **NAT Gateway**.
3. The instance sends a packet to the NAT Gateway with:
   - **Source IP**: Private IP of the instance
   - **Destination IP**: Internet address (e.g., Google)
4. The **NAT Gateway** performs **Source NAT (SNAT)**:
   - Replaces the source IP with its own **public IP (Elastic IP)**
   - Keeps the destination IP unchanged
5. The packet reaches the destination (e.g., Google).
6. The response is sent back to the **NAT Gateway**.
7. The NAT Gateway checks its internal mapping to identify the original source instance and **forwards the response**.

---

## **Why NAT Gateway Must Be in Public Subnet**

- It **requires direct internet access**, so it must be in a subnet that has a **route to the Internet Gateway**.
- It uses an **Elastic IP** for outgoing traffic.

---

## **High Availability Best Practice**

To avoid a **single point of failure**, especially if one AZ becomes unavailable:

- **Create one NAT Gateway per Availability Zone** where you have private subnets.
- **Update each private subnet's route table** to point to the NAT Gateway in the **same AZ**.
- This ensures **zonal redundancy** and prevents **cross-AZ data transfer charges**.

__

## **NAT Gateway vs NAT Instance**

| **Feature**         | **NAT Gateway**                    | **NAT Instance**                        |
|---------------------|------------------------------------|------------------------------------------|
| **Managed by AWS**  | Yes                                | No (you manage scaling and health)       |
| **Elastic IP**      | Required                           | Optional                                 |
| **Availability**    | Highly available and scalable      | Single instance, needs manual scaling    |
| **Cost**            | More expensive                     | Cost-effective for dev/test              |
| **Security Groups** | Not supported                      | Required                                 |
