# Docker Internals: Namespaces, cgroups, and Images

## Namespacing

Namespaces in Linux provide **resource isolation** for containers. Each container gets its own:

- **PID namespace** – Isolated process IDs
- **Mount namespace** – Isolated filesystem view
- **Network namespace** – Virtual network stack
- **User namespace** – Isolated user/group IDs
- **UTS namespace** – Isolated hostname and domain name

> This isolation ensures containers don't see or interfere with each other's processes or resources.

---

## Control Groups (cgroups)

**cgroups** (Control Groups) allow the system to:

- **Limit** the amount of CPU, memory, I/O, and other resources used by containers.
- **Monitor** resource usage.
- **Prioritize** or **isolate** resource access between processes.

> This helps prevent a single container from consuming all system resources.

---

## Docker Image and Container Startup

- A **Docker image** is a layered, read-only **snapshot of a filesystem**.
- It contains:
  - Base OS files (e.g. from Ubuntu, Alpine, etc.)
  - Application code and dependencies
  - Metadata like environment variables and startup commands

### When You Run a Container:

1. Docker **assembles the image layers** into a unified filesystem.
2. An **isolated storage space** is created for the container.
3. The image's **startup command** is executed in a new, **isolated process** using namespaces and cgroups.
4. The container runs with its own:
   - Filesystem
   - Network interface
   - Process list

> The result is a lightweight, isolated environment that behaves like a small, self-contained Linux system.