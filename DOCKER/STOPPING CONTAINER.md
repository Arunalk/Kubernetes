# Difference Between `docker stop` and `docker kill`

## `docker stop`

- Sends the **SIGTERM** signal to the container's main process, requesting it to gracefully shut down.
- By default, Docker gives the container **10 seconds** to shut down properly.
- If the container does not stop within this time frame, **SIGKILL** is sent to forcefully terminate it.
- This allows the container to finish processes, clean up, and shut down gracefully before being killed.

---

## `docker kill`

- Sends the **SIGKILL** signal immediately, terminating the container without any grace period.
- The container is stopped instantly, and no opportunity is given for clean-up or graceful shutdown.

---

## Summary

- **`docker stop`**: Graceful shutdown (SIGTERM) with a 10-second timeout before forcing a kill (SIGKILL).
- **`docker kill`**: Immediate termination (SIGKILL) with no grace period.
