### Liveness Probe

Liveness probes in Kubernetes are used to determine whether a container is still running and healthy. If a liveness probe fails, Kubernetes will automatically restart the container to recover from any failure.

#### Key Configuration Parameters:
- **httpGet**: Kubernetes sends an HTTP request to check the container’s health endpoint.
- **initialDelaySeconds**: Time to wait after container starts before the first probe.
- **periodSeconds**: Time interval between consecutive liveness checks.
- **timeoutSeconds**: Maximum time Kubernetes waits for a response.
- **failureThreshold**: Number of consecutive failures required before restarting the container.

#### Example:
```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 5
  periodSeconds: 10
  timeoutSeconds: 2
  failureThreshold: 3
```

### Use Cases for Liveness Probe

- **Detecting and recovering from application failures**: Liveness probes can help identify issues such as deadlocks, unresponsiveness, or other types of failure that make the application unresponsive.
  
- **Ensuring long-running applications stay alive**: By periodically checking the container's health, liveness probes ensure that the application continues to function without needing manual intervention.
  
Liveness probes help ensure that problematic containers are automatically restarted, preventing downtime and maintaining the stability of the application.
