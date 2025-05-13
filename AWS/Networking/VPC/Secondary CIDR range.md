# **Extending VPC Address Space with Secondary CIDR Blocks**

## **Why Extend a VPC CIDR?**

1. **IP Exhaustion**:  
   You initially created a VPC with a small CIDR block and are now running out of IP addresses.

2. **CIDR Overlap with On-Premise Network**:  
   You have existing instances in the current CIDR range, but your on-premise network has overlapping IP ranges.  
   Since AWS VPC peering or VPN cannot work with overlapping CIDRs, extending the VPC with a non-overlapping secondary CIDR solves this.

---

## **Points to Keep in Mind When Adding Secondary CIDR**

- ✅ **Can be added** to an existing VPC at any time.
- ❌ **Must not overlap** with the primary CIDR or any other secondary CIDR blocks.
- ❗ **Must not be larger** than the smallest CIDR range associated with any route table.
- 🔒 **RFC1918 compliance**:  
  Secondary IPv4 CIDR blocks **cannot** be from **RFC1918 reserved ranges** if your primary CIDR is already from that range.
  
---

## **CIDR Block Limits**

- ✅ A VPC can have up to:
  - **5 IPv4** CIDR blocks
  - **1 IPv6** CIDR block

---

## **Example**

- **Primary CIDR**: `10.0.0.0/16`  
- **Secondary CIDR (valid)**: `10.1.0.0/16`  
- **Secondary CIDR (invalid)**: `10.0.1.0/24` (overlaps with the primary)

---

## **Use Cases**

- Extending subnets across new CIDR blocks.
- Avoiding re-architecture when scaling IP needs.
- Enabling connectivity with external networks or hybrid architectures.
