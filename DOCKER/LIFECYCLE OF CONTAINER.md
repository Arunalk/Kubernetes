# Docker Container Lifecycle

## Lifecycle Overview

A Docker container goes through several key stages:

1. **Image**: A static, read-only template.
2. **Create**: The container is defined but not running.
3. **Start**: The container begins execution.
4. **Running**: The container is active and executing the defined command.
5. **Stopped/Exited**: The container finishes or is manually stopped.

---

## Common Lifecycle Commands

### `docker run`

```bash
docker run <image>
```
- This is equivalent to:
    - docker create <image> + docker start <container-id>

- It creates and then starts the container in one command.
### Clarified Explanation
**docker run = docker create + docker start**
It performs both steps: creates the container and then starts it immediately.

```
docker create
```

Only creates the container from an image. The container is not running yet.

```
docker start
```
Starts an already-created container.

```
-a or --attach
```
Attaches the container's STDOUT/STDERR to your terminal so you can see output from the container directly.


## RESTARTING A CONTAINER

**You cannot oveeride the default command once the process exists and you start the container again.**

## REMOVING STOPPED CONATINER

How to entirely delete them?

```
docker system prune
```

So that it removes the unwanted space in local which is still occupied by this stopped/unwanted container.