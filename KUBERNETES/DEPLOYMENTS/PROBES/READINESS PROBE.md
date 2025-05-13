# Kubernetes Readiness Probe

In Kubernetes, the **Readiness Probe** is used to determine if a container is ready to start accepting traffic. If the probe fails, the container will be considered "not ready" and will be removed from the service's load balancing pool. This helps prevent traffic from being sent to an application that is not yet fully initialized or unable to handle requests.

## Purpose of Readiness Probe

- **Control Traffic Flow:** The Readiness Probe ensures that Kubernetes only routes traffic to containers that are fully initialized and ready to handle requests. 
- **Graceful Traffic Management:** Helps in controlling when the application should be exposed to users. For example, if the app is undergoing initialization or a database is still being set up, traffic should not be routed to it prematurely.

## How It Works

Kubernetes periodically checks the **Readiness Probe** using the specified configuration (HTTP request, TCP socket check, or command). If the probe fails (i.e., the application isn't ready), Kubernetes removes the container from the pool of endpoints used by services. Once the container is ready (i.e., the probe succeeds), it is added back to the pool, and traffic can be routed to it again.

## When to Use Readiness Probe

Use the Readiness Probe when:

- The application is initializing and requires time to load resources or make connections before it can handle traffic (e.g., loading a large dataset or waiting for an external service like a database to be available).
- The application might need to handle certain background tasks or processes before it is ready to serve user requests.
- Your container might fail if it gets traffic too soon, such as when it's still in the startup phase or waiting for dependencies.

## Example Configuration

### Basic Readiness Probe Using HTTP

In this example, we configure a simple HTTP check to the `/health` endpoint. The readiness check will return a success status (HTTP `200 OK`) if the app is ready to accept traffic.

```yaml
readinessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 5  # Time to wait before the first probe
  periodSeconds: 3        # Time interval between subsequent probes
  timeoutSeconds: 2       # How long to wait for a response
  successThreshold: 1     # Number of successes before the probe is considered successful
  failureThreshold: 3     # Number of failures before marking the container as "unready"
```

In this configuration, Kubernetes will send an HTTP GET request to the `/health` endpoint on port `8080` to check if the container is ready to serve traffic. The following settings define how Kubernetes interacts with the probe:

- **httpGet**: Kubernetes sends an HTTP GET request to the `/health` endpoint on port `8080`. This is used to check if the container is ready to handle traffic.

- **initialDelaySeconds**: This setting specifies the time Kubernetes will wait after the container starts before it begins checking the readiness probe. For example, `5` seconds means Kubernetes will start checking readiness 5 seconds after the container starts.

- **periodSeconds**: This defines how often Kubernetes will check the readiness probe. A value of `3` seconds means Kubernetes will check every 3 seconds to verify the application's readiness.

- **timeoutSeconds**: This is the maximum time Kubernetes will wait for a response from the container. If the container doesn't respond within `2` seconds, the probe will be considered failed.

- **successThreshold**: This defines how many successful probe checks Kubernetes needs to consider the container "ready." By default, it's `1`, meaning the container only needs one successful response to be considered ready.

- **failureThreshold**: This defines how many failed checks are required for the container to be marked as "not ready." In this case, if there are `3` failed checks, Kubernetes will stop routing traffic to this container.

### 2. Readiness Probe Using TCP Socket

If your application does not have an HTTP health check endpoint, you can use a TCP socket check instead. Kubernetes will attempt to establish a TCP connection to the specified port inside the container to check if the application is ready to accept traffic.

- **tcpSocket**: Kubernetes attempts to establish a TCP connection to the specified port (in this case, `8080`). If the connection is successful, Kubernetes considers the container ready to serve traffic.
  
- **initialDelaySeconds**: This specifies the amount of time Kubernetes will wait after the container starts before it begins checking the readiness probe. This is useful when your application needs some time to initialize before accepting traffic. For example, a value of `5` means Kubernetes will start checking readiness 5 seconds after the container starts.

- **periodSeconds**: This defines how often Kubernetes will check the readiness probe. A value of `3` seconds means Kubernetes will check every 3 seconds to verify the application's readiness.

- **timeoutSeconds**: This is the maximum amount of time Kubernetes will wait for a connection to be established. If the container does not respond within this time, the probe is considered failed.

- **successThreshold**: This defines how many successful probe checks are needed to mark the container as "ready." By default, it is `1`, meaning one successful TCP connection will mark the container as ready.

- **failureThreshold**: This defines how many failed attempts are allowed before the container is considered "not ready." If there are `3` failed attempts, Kubernetes will remove the container from the service endpoint.

```yaml
readinessProbe:
  tcpSocket:
    port: 8080            # The port on which the container should be accepting connections
  initialDelaySeconds: 5      # Wait 5 seconds after the container starts before checking readiness
  periodSeconds: 3           # Check readiness every 3 seconds
  timeoutSeconds: 2          # Wait 2 seconds for a successful connection
  successThreshold: 1        # Only one successful connection needed to mark container as "ready"
  failureThreshold: 3        # If there are 3 failed checks, mark container as "not ready"
```

### 3. Readiness Probe Using a Command

If your application requires custom validation or logic to determine if it is ready to accept traffic, you can use a **command-based readiness probe**. In this approach, Kubernetes runs a command inside the container and expects the command to return a zero exit code (indicating success). If the command exits with a non-zero status, Kubernetes considers the probe to have failed.

- **exec**: This section specifies a command to run inside the container. Kubernetes will execute this command periodically to check the application's readiness.

- **initialDelaySeconds**: Specifies the amount of time Kubernetes will wait after the container starts before initiating the first readiness check. This is useful if the application needs a delay before it can start responding to commands.

- **periodSeconds**: Defines how often Kubernetes will run the readiness probe command. This allows Kubernetes to periodically check the application's readiness state.

- **timeoutSeconds**: The amount of time Kubernetes will wait for the command to complete. If the command doesn't finish within this time, the probe will be considered a failure.

- **successThreshold**: The number of consecutive successful probes required to mark the container as "ready." By default, this is set to `1`, meaning only one successful command execution is required to mark the container as ready.

- **failureThreshold**: The number of failed checks required to mark the container as "not ready." If the command fails repeatedly, Kubernetes will mark the container as not ready after the specified number of failed attempts.

#### Example: Readiness Probe Using a Command (HTTP Check)

In this example, the readiness probe runs a `curl` command to check the `/health` endpoint of the application. If the HTTP request fails (e.g., returns a non-2xx status code), the probe will fail.

```yaml
readinessProbe:
  exec:
    command:
      - "/bin/sh"
      - "-c"
      - "curl -f http://localhost:8080/health || exit 1"
  initialDelaySeconds: 5      # Wait 5 seconds after the container starts before checking readiness
  periodSeconds: 3           # Check readiness every 3 seconds
  timeoutSeconds: 2          # Wait 2 seconds for a successful response from curl
  successThreshold: 1        # Only one successful command needed to mark container as "ready"
  failureThreshold: 3        # If there are 3 failed checks, mark container as "not ready"
```

### Explanation of the Configuration:
- **command**: The command executes a `curl -f` request to check the `/health` endpoint of the application on `localhost:8080`. The `-f` flag ensures that `curl` fails (with a non-zero exit code) if the HTTP request does not return a successful status code.
  
- **initialDelaySeconds**: This ensures that Kubernetes waits 5 seconds after the container starts before checking its readiness, which gives the application time to initialize.

- **periodSeconds**: Kubernetes checks the readiness every 3 seconds by running the command.

- **timeoutSeconds**: Kubernetes waits 2 seconds for the `curl` command to complete before considering it a failure.

- **successThreshold**: Only one successful execution of the command is required to mark the container as ready.

- **failureThreshold**: If the command fails 3 times consecutively, Kubernetes will mark the container as "not ready" and remove it from the service.

### When to Use Command-Based Readiness Probes
Command-based readiness probes are particularly useful in the following scenarios:

- **When you need more complex checks** beyond simple HTTP/TCP checks, such as checking multiple services, executing scripts, or validating application logic.

- **If you have custom health check logic** or need to validate external dependencies (like databases, APIs, or other services) before considering the container ready.

This flexibility allows for a deeper level of application validation and ensures that only fully ready containers will receive traffic, improving the overall stability of your application in a Kubernetes environment.

### Conclusion

Readiness probes in Kubernetes are essential for ensuring that your application is fully initialized and ready to handle traffic before it is exposed to users. By configuring appropriate readiness probes—whether using HTTP, TCP, or custom commands—you can improve the reliability and stability of your application, especially in a dynamic environment like Kubernetes.

Each type of probe has its use case:

- **HTTP probes** are suitable for applications with dedicated health check endpoints.
- **TCP probes** are useful for applications without an HTTP health check but that still require verification of network availability.
- **Command-based probes** offer the most flexibility, allowing for complex validation logic and checks on external dependencies.

Using these probes effectively helps prevent service disruption, ensures that only healthy containers handle traffic, and minimizes the impact of slow starts or dependency issues during deployment.

Proper configuration of initial delays, check intervals, and success/failure thresholds ensures a smooth and stable application lifecycle in Kubernetes, reducing the chances of downtime or failures in production environments.
