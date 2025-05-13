## 🧩 Sharding in RDS

### 🔷 What Is Sharding?

**Sharding** is the process of **splitting a single database into multiple smaller databases (shards)**, each responsible for a **subset of the data**.  
It is a form of **horizontal scaling** and is useful when a single RDS instance can no longer handle the workload due to:

- High query volume
- Large data size
- Application complexity

---

### ⚙️ How It Works

- The application is responsible for **routing queries** to the correct shard (RDS instance).
- Shards may be created by **promoting read replicas** into independent databases.
- Example sharding strategy:
  - Users A–M in one database
  - Users N–Z in another
- You can use **read replicas as a starting point**, then **promote and isolate them** to form shards.

---

### 🧠 Key Points

| Aspect              | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Type                | Horizontal scaling                                                          |
| Use of Read Replicas| ✅ Can be used to bootstrap shards by promoting them                         |
| Query Routing       | ❗ Must be handled at the **application level**                              |
| Benefits            | Scalability, isolation, fault containment                                   |
| Downsides           | Increased application complexity, risk of data fragmentation                |

---

### 🔁 Sharding vs Read Replicas

| Feature         | Read Replica                        | Sharding                              |
|------------------|--------------------------------------|----------------------------------------|
| Purpose          | Read traffic offloading             | Horizontal data partitioning           |
| Write Operations | Only on primary                     | ✅ Allowed on each shard                |
| Scaling Type     | Vertical (read scaling)             | Horizontal (data + workload scaling)   |
| Failover Support | Managed by RDS (Multi-AZ)           | ❌ Must be implemented manually         |

---

> 🧠 Sharding is **not natively supported** by RDS — the logic and routing must be handled by your **application** or a **custom middleware layer**.