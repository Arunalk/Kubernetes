# Creating a Docker Image

## Step 1: Dockerfile

- A **Dockerfile** is a plain text file that contains instructions on how to build a Docker image.
- It defines:
  - The **base image** to start from (e.g., Ubuntu, Node, Python).
  - Software and dependencies to install.
  - Files to copy into the image.
  - Ports to expose.
  - The command to run when the container starts.

---

## Step 2: Docker Client and Server

- The Dockerfile is passed to the **Docker client (CLI)**.
- The Docker client sends it to the **Docker server (daemon)**.
- The server processes each line of the Dockerfile and performs the following:
  - Downloads the necessary base images.
  - Installs dependencies and configures the environment.
  - Builds and assembles everything into a **Docker image**.

---

## Result: Docker Image

- The output is a **Docker image** — a packaged snapshot of your application environment.
- This image can be used to launch containers that behave exactly as defined in the Dockerfile.
