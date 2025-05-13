## Route Tables in AWS VPC

Route tables define **how traffic flows in and out of subnets** within a VPC. Each subnet must be associated with one route table.

---

### Key Concepts

- **Main Route Table**: Automatically created with the VPC. Used by subnets that are not explicitly associated with a custom route table.
- **Custom Route Table**: User-created route tables that can be associated with specific subnets for custom routing behavior.

---

### Subnet Communication

- **All subnets within a VPC can communicate with each other by default**.
- This is because of an **immutable local route** present in every route table:
  - **Destination**: VPC CIDR Block  
  - **Target**: local
- This local route ensures internal connectivity and **cannot be removed**.

---

### Can Instances Block Each Other?

- Yes, even though routing allows communication, instances can be isolated using:
  - **Security Groups** (work at the instance level)
  - **Network ACLs** (work at the subnet level)

---

### Can an Instance Access the Internet?

By default, **instances cannot access the internet**. To enable internet access, you need:

1. **Internet Gateway (IGW)**  
   - Must be attached to the VPC.

2. **Route Table Entry**  
   - A route must exist in the subnet’s route table:
     - **Destination**: 0.0.0.0/0  
     - **Target**: Internet Gateway (IGW)

3. **Public IP Address**  
   - The instance must have a **public IP** or an **Elastic IP** assigned.

Without all three, **internet access will not work**.

---

### Route Table Behavior

- If the **main route table** is updated to route through an Internet Gateway:
  - **All subnets using the main table** will gain internet access.
- **Custom route tables are isolated**:
  - Subnets using a custom table will **not be affected** by changes to the main route table.
  - They will only follow rules defined in their own table.

---

### Best Practices

- Use **custom route tables** to:
  - Separate public and private subnets
  - Control traffic paths precisely
- Keep the **main route table** for general use or private subnet traffic control.
