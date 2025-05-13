---

## Replicating Dockerfile Steps Manually (Without Dockerfile)

While Dockerfiles are the standard way to build images, the same process can be replicated manually using Docker CLI commands.

---

### Example Dockerfile

To replicate the following Dockerfile:

```
FROM alpine
RUN apk add --update redis
CMD ["redis-server"]
```


You would follow these manual steps:

---

### Step-by-Step Manual Process

1. **Run a Base Container**
   - Start a container from the base image (e.g., Alpine).
   - Access its shell to perform operations.

2. **Install the Required Software**
   - Inside the container, run installation commands manually (e.g., install Redis using `apk`).
   - This modifies the container's filesystem.

3. **Exit the Container**
   - Once setup is complete, exit the container.

4. **Commit the Container to Create a New Image**
   - Use the `docker commit` command to create a new image from the modified container.
   - Set the default command using the `-c` flag.

   Example:
```
docker commit -c 'CMD ["redis-server"]' <container-id> <username/repo:tag>
```

> ⚠️ Make sure the `CMD` is passed as a **valid JSON array**.

5. **Result**
- You now have a new image with:
  - Redis installed.
  - A default command (`redis-server`) set.
- You can run new containers from this image without needing a Dockerfile.


