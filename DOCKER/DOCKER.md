**Docker Ports**
```
docker run -p 50:5000 myapp
```
50 is the **host port** (not the container port).
5000 is the **container port** (not the host port).
So the correct interpretation is:

**Container port (5000**): This is the `port inside the Docker container where your application is running`. In your example, it’s likely that `your application is listening on port 5000` inside the container (such as a Flask or FastAPI app).

**Host port (50):** This is the port on your host machine that will be used to `access the containerized application from the outside world`. In your case, the application running on port 5000 inside the container will be accessible on port 50 of the host machine.

**Access the service:**
```
curl http://localhost:8080
```

**WHY PORT 8080?**

1. Port 8080 is often used as an alternative to the default HTTP port (port 80). It is a commonly accepted convention in web development and testing environments. When developers `don't want to interfere with the system's default port 80`, they use port 8080 for testing or local development purposes.

2. **Avoiding Permission Issues:**
On many systems, especially Linux or macOS, ports `below 1024 are privileged ports`. Only the root user (or superuser) can bind services to those ports. For example, port 80 requires administrative privileges.
Port 8080 is above 1024, so you don't need elevated permissions to run a service on this port. It's a common choice for development because it avoids these restrictions while still being associated with HTTP traffic.

3. **Compatibility with Web Frameworks:**
Many web frameworks or `HTTP server tools (like Python's http.server, Tomcat, or others) default to port 8080` for the server. This is just a widely used default for local web servers.

4. **Avoid Conflicts:**
If you’re running other services (like a web server such as Apache or NGINX) that listen on port 80 or 443, `using port 8080 for your application avoids conflicts with those services`. You can still access your web app at http://localhost:8080 while keeping the default ports reserved for system-wide services.