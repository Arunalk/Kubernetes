# Base Image and Docker Image Build Process

## Base Image (e.g., Alpine)

- A **base image** is the starting point for building a Docker image.
- In our case, we used **Alpine Linux**, which is:
  - Lightweight and minimal.
  - Fast to download and run.
  - Comes with the `apk` package manager.

---

## Installing Software

- In the Dockerfile, a command is used to install Redis using `apk`.
- **`apk`** is Alpine's built-in package manager.
- Docker creates a **temporary container** to execute this step.
- Redis is installed inside this container, and the **resulting filesystem is saved** as a new image layer.

---

## Image Layering and Snapshots

- Each line in a Dockerfile creates a **new layer** on top of the previous image.
- For each instruction:
  - Docker creates a **temporary container** from the current image state.
  - Executes the instruction (e.g., installing Redis).
  - After execution, the container is **shut down**.
  - A **snapshot** of the updated filesystem is taken.
  - This snapshot becomes a **new image layer**.
- This process is repeated for each instruction in the Dockerfile.

---

## Final Image Creation

- After all instructions are processed:
  - Docker combines all the layers.
  - It stores **startup metadata** such as:
    - Exposed ports
    - Environment variables
    - The command to run when a container starts
- This metadata is **not executed during build**, only saved.

---

## Final Result

- The final Docker image includes:
  - The base system (Alpine).
  - Redis and any other installed programs.
  - The full set of **layered filesystem snapshots**.
  - Metadata including the default runtime command.
- This image can be used to create containers that execute a **primary command**, such as starting a Redis server.

---

## Why This Process Works Well

- **Caching**: Each image layer is cached. If unchanged, it is reused in future builds.
- **Immutability**: Every layer is read-only and layered on top of the previous one.
- **Efficiency**: Rebuilding is faster because only modified steps are re-executed.
