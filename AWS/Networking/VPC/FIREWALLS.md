## Firewall in AWS VPC

In AWS, firewalls help manage and control traffic at different levels of the VPC using **Security Groups** and **Network Access Control Lists (NACLs)**.

---

### Security Groups

- **Associated with EC2 instances**
- Function as **virtual firewalls** to control **inbound and outbound traffic**
- Rules can be configured for:
  - Specific **IP addresses**
  - **Port numbers**
  - **Protocols**

#### Key Characteristics:

- **Stateful**: 
  - If a request is allowed in, the response is automatically allowed out—no need to create a separate outbound rule.
- **Only supports "Allow" rules**
- Rules are not evaluated as per order
- You can reference another **security group** in rules, useful in layered architectures:
  - Example: Web tier instances can reference app tier's security group to allow communication.
- Can be **attached to multiple EC2 instances**
- Exists **outside of the instance**, so traffic blocked by security groups **never reaches the EC2**.
- By default:
  - **All inbound traffic is blocked**
  - **All outbound traffic is allowed**

#### Troubleshooting Tip:
- **Timeout errors** can indicate a **Security Group misconfiguration**.
  - "Not accessible" or "timeout 503" = security group misconfiguration possible blocked port
  - "Connection refused" = security group has allowed, but application is not accepting the traffic.

---

### Network ACL (NACL)

- Applied at the **subnet level**, affecting **all instances** within the subnet
- Controls both **inbound and outbound traffic**

#### Key Characteristics:

- **Stateless**:
  - If you allow inbound traffic, you must **explicitly allow outbound traffic** for return communication.
- Supports both **Allow** and **Deny** rules
- Rules are **evaluated in order**, based on the **rule number**
- Default NACL:
  - Allows **all inbound and outbound traffic**
- Useful to:
  - Block traffic from **specific IPs**
  - Enforce **broader subnet-level restrictions**

#### Example Scenario:
- If a local machine reaches EC2 using a dynamic (ephemeral) port (e.g., 32765), you must allow the **outbound ephemeral port range**.
- Missing outbound rule can prevent the response from being sent, causing connection issues.

---

### Security Group vs Network ACL

| Feature                     | Security Group                      | Network ACL                       |
|----------------------------|-------------------------------------|-----------------------------------|
| Applied To                 | EC2 Instance                        | Subnet                            |
| Stateful                   | Yes                                 | No (Stateless)                    |
| Supports Deny Rules        | No                                  | Yes                               |
| Default Behavior           | Inbound: Deny, Outbound: Allow      | Inbound & Outbound: Allow         |
| Rule Evaluation            | All rules evaluated                 | Rules evaluated in number order   |
| Common Use Cases           | Fine-grained EC2 access control     | Broad subnet-level restrictions   |

