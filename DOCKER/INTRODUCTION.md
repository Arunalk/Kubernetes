# Why Docker?

Docker simplifies the process of installing and running software by packaging an application along with all its dependencies into a single, portable unit called a **container**. This ensures consistency across development, testing, and production environments.

---

# What is Docker?

Docker is a platform for developing, shipping, and running applications inside **containers**. A container is a lightweight, standalone, and executable unit that includes:

- Application code
- Dependencies (libraries, binaries)
- System tools and settings

---

# Key Concepts

- **Docker Image**: A read-only template containing the app and its environment. Think of it as a blueprint or snapshot.

- **Docker Container**: A runnable instance of a Docker image. It is isolated and runs the application defined in the image.

- **Docker Hub**: A cloud-based registry where Docker images are stored and shared. You can pull public images from here.

---

# How Docker Works (Example: `docker run hello-world`)

1. The Docker **client** sends a request to the Docker **daemon**.
2. The daemon checks if the `hello-world` image is available locally.
3. If not found, it pulls the image from **Docker Hub**.
4. Docker creates a container from the image.
5. The container runs a small program that prints:  
   `"Hello from Docker!"`

---

# Note on Containers and Hardware

> Containers **do not** have their own hardware.  
> Instead, they share the host system's OS kernel and use OS-level virtualization.  
> This makes containers more lightweight and efficient than virtual machines.