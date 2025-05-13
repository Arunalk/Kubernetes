## Build Cache

- Docker uses **layer caching** to speed up image builds.
- Each instruction in the Dockerfile creates a **snapshot layer**.
- If no changes are detected in an instruction:
  - Docker uses the **cached version** of the layer from a previous build.
  - This avoids re-running the command, making the build much faster.

---

## When Cache Is Used vs. Invalidated

- Docker reuses a cached layer **only if**:
  - The instruction is **identical** to the previous build.
  - No associated files (e.g., copied source files) have changed.
- If you **modify or add** an instruction:
  - Docker **invalidates the cache** from that point onward.
  - All instructions **after** the change are **rebuilt**, even if unchanged.

---

## Order of Instructions Matters

- Since Docker caches each instruction **in order**, the **sequence of steps** in your Dockerfile is important.
- If an early instruction (like `COPY . .`) changes frequently:
  - It can **invalidate the cache** for all subsequent steps.
- Best practice:
  - Place commands that **change the least** (e.g., installing system packages) **higher up** in the Dockerfile.
  - Place frequently changing steps (e.g., copying source code) **later** to maximize cache reuse.

---

## Benefit

- **Faster incremental builds**.
- **Efficient use of storage and bandwidth**.
- **Minimal rebuild time** by leveraging previously cached layers.
