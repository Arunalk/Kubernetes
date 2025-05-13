## VPC CIDR and IP Addressing

### Why IP?

- An **IP address** is the **identity of a host** in a network.
- Without an IP address, one host **cannot connect** to another.

---

### IPv4 vs IPv6

- **IPv4**
  - **32-bit** address format.
  - Written as **four octets**, each ranging from 0 to 255.
  - Example: `199.162.56.10`
  - In binary: `11000111.10100010.00111000.00001010`
  - IPv4 addresses are **limited** and are being exhausted due to rapid internet growth.

- **IPv6**
  - **128-bit** address format.
  - Created to solve the **IP address exhaustion** problem.
  - Allows for a **much larger address space** than IPv4.

---

## CIDR (Classless Inter-Domain Routing)

- **CIDR** is an IP addressing scheme that **replaced the old class-based system** (Class A, B, C).
- CIDR notation is written as:  
  `IP_address/prefix_length`  
  Example: `199.162.0.0/16`

### What Does the Prefix Mean?

- The **prefix length** (e.g., `/16`) indicates how many bits are used for the **network portion** of the address.
  - The remaining bits are used for **host addresses**.
- Example:
  - `199.162.0.0/16` →  
    - **First 16 bits**: network address (`199.162`)
    - **Remaining 16 bits**: host addresses (`0.0` to `255.255`)

### Network vs Host Address

- **Network address**: identifies the network segment (e.g., `199.162` in a `/16`).
- **Host address**: identifies individual devices within the network.

### How to Calculate Number of Hosts

- Formula: `2^(total host bits)`
- For `/16`:  
  - Total bits = 32  
  - Host bits = 32 - 16 = 16  
  - Number of addresses = `2^16 = 65,536`

---

## CIDR and Subnetting

- **Subnets** are created by reserving more bits for the network.
- Examples:
  - `/28` subnet → 32 - 28 = 4 bits for hosts  
    - `2^4 = 16` IP addresses per subnet
  - `/32` → only **1 IP address** (used to represent a single host)
  - `/0` → **all IPs available** (not used in practice within AWS VPC)

### In AWS VPC

- When designing your VPC:
  - Choose a CIDR block (e.g., `/16` or `/20`) based on expected number of subnets and instances.

---

## AWS Reserved IP Addresses in a Subnet

AWS reserves **5 IP addresses in every subnet**, so the actual number of usable IPs is:

**total - 5**


### 🔒 Reserved IPs Explained

| **IP Address**               | **Purpose**                                                                 |
|-----------------------------|------------------------------------------------------------------------------|
| **.0 (first IP)**            | **Network address** — identifies the subnet.                                |
| **.1 (second IP)**           | **VPC router address** — used as the default gateway.                       |
| **.2 (third IP)**            | Reserved for AWS **DNS service**.                                           |
| **.3 (fourth IP)**           | Reserved by AWS for **future use**.                                         |
| **.255 (last IP)**           | **Broadcast address** — reserved (not used, but reserved for consistency).  |

### Example:

For a subnet with CIDR block `10.0.0.0/24`:

- **Total IPs**: `2^(32-24) = 256`
- **Reserved by AWS**: 5
- **Usable IPs**: `256 - 5 = 251`
