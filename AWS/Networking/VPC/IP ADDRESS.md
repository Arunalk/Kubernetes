## IP Addresses in AWS VPC

In AWS, instances can be assigned both **IPv4** and **IPv6** addresses within a VPC. These addresses determine how instances communicate within the VPC and with the internet.

---

### IPv4 in VPC

#### **Private IP Address**
- Assigned automatically from the **VPC’s CIDR block**.
- **Does not change** across instance stops or restarts.
- Used for **internal communication** between resources (e.g., app servers, databases).
- Can be statically assigned or automatically allocated.

#### **Public IP Address**
- **Temporarily assigned** from AWS's pool of public IPs.
- Needed for communication with the **internet**.
- Must be used in conjunction with:
  - An **Internet Gateway**
  - Proper **route table entry** for internet access
- Assigned if:
  - You **enable the "Auto-assign Public IP"** setting at the subnet level.
  - Or explicitly enable it while **launching the instance**.
- **Cannot be chosen manually** – AWS automatically assigns one.
- **Lost** if the instance is stopped or terminated (unless Elastic IP is used).

#### **Elastic IP Address (EIP)**
- A **static public IPv4 address** allocated from AWS's pool.
- **Persists** across instance stops, starts, and reboots.
- Must be **explicitly allocated and associated** with the instance.
- Commonly used for:
  - **Web servers**
  - **Load balancers**
  - **External-facing applications**
- Helps avoid issues caused by changing public IPs.

---

### When to Use Each IP Type

- **Private IP** – Internal resources (databases, app servers)
- **Public IP** – Temporary external access (only persists while instance is running)
- **Elastic IP** – Persistent external access (static public IP)

---

### IPv6 in VPC

- All **IPv6 addresses are public and globally unique**.
- IPv6 support must be **explicitly enabled** in the VPC.
- **Persist across instance stop/start**, but are **released on instance termination**.
- DNS hostnames **are not supported** for IPv6 addresses in AWS.
- VPC can support **dual-stack** (both IPv4 and IPv6).

---

### VPC CIDR Ranges

- **IPv4 CIDR block**: Can range from **/16 to /28**
- **IPv6 CIDR block**: Can be up to **/56**
- Each instance with an IPv4 address is automatically assigned an **Amazon-provided DNS hostname** for both public and private IPs.
- **IPv6 instances do not receive DNS hostnames** by default.

