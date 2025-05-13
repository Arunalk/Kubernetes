# **Bring Your Own IP (BYOIP) to AWS**

## **Why Bring Your Own IP?**

- **IP Reputation**:  
  Your existing IPs may have a **good reputation** — important for applications like email, API access, or external integrations.

- **Avoid Whitelisting Hassles**:  
  Clients or partners might have **hardcoded or whitelisted** your current public IPs in firewalls or security devices.

- **Zero-Change Migration**:  
  Move applications to AWS **without changing public IPs**, reducing client-side changes or reconfiguration.

- **Disaster Recovery & Hot Standby**:  
  If you're running in an on-premises environment and need to **fail over to AWS**, BYOIP enables continuity using your **existing IPs**.

---

## **Prerequisites**

1. **Ownership**:
   - The IP range must be **registered to you** via a Regional Internet Registry (RIR):
     - **ARIN** – North America
     - **RIPE NCC** – Europe, Middle East
     - **APNIC** – Asia-Pacific

2. **IP Health**:
   - The IP address range must have a **clean history**:
     - Not associated with **spam**, **malware**, or **blacklists**.
     - AWS may **reject** ranges with bad reputation.

3. **ROA (Route Origin Authorization)**:
   - Create a **Route Origin Authorization** to prove you're authorized to advertise that IP prefix.
   - This gives AWS permission to **advertise your IP** on the internet via BGP.

---

## **IP Range Requirements**

| IP Version | Minimum CIDR Block | Notes                                      |
|------------|--------------------|--------------------------------------------|
| IPv4       | /24                | Smallest block allowed                     |
| IPv6       | /48                | If public; /56 if not publicly advertised  |

---

## **How It Works**

- You retain **ownership** of the IP.
- AWS **advertises** it on your behalf.
- The IP becomes part of your account’s **Elastic IP pool**.
- You can **assign it** to:
  - EC2 instances
  - NAT Gateways
  - Network Load Balancers (NLBs)

> ⚠️ BYOIP does **not** mean AWS owns the IP — you still manage and control it.

---

## **Limits**

- You can bring:
  - Up to **5 IPv4** address ranges
  - Up to **5 IPv6** address ranges  
    **per AWS account**

---

## **Summary**

**BYOIP** is ideal when:
- You want to maintain a **consistent external IP**.
- You’re migrating from **on-premises** to AWS.
- You care about **IP reputation**, client trust, or avoiding firewall changes.

AWS makes it possible to **seamlessly transition** with minimal impact to external systems.
