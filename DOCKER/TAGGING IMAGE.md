---

## Tagging a Docker Image

- When building a Docker image, you can assign it a **tag** to identify:
  - The **project name** or **repository**.
  - A specific **version** of the image (e.g., `v1`, `latest`).
- Tags help you **organize** and **manage** images, especially when:
  - Pushing to Docker Hub or a private registry.
  - Running or referencing specific versions later.

---

## Tag Format

- A tag generally follows this format:

- **docker-username**: Your Docker Hub username.
- **repository-name**: A meaningful name for your project.
- **version**: The version label for the image (e.g., `1.0`, `latest`).

---

## Benefits of Tagging

- Helps identify and manage **multiple versions** of the same image.
- Enables easy **version control** for deployments.
- Makes it clear which image you're **pushing, pulling, or running**.
