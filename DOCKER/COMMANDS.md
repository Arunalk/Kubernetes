## DOCKER COMMANDS

1. List containers
```
docker ps
docker ps --all
```

2. To see logs for debugging
```
docker logs <container-id>
```

3. Run a container
```
docker run <image-name>
```

4. Stop a container - SIGTERM
```
docker stop <container-id>
```

5. Kill a container - SIGKILL
```
docker kill <container>
```

6. Connect to a container

```
docker exec -it <container-id> <command>
```

7. Shell access or terminal access for the container

```
docker exec -it <container-id> sh
```

8. Build an Image

```
docker build .
```

9. Tagging an image

```
docker build -t <dockerusername/project:verison>

or without rebuilding
docker tag <image-name>
```