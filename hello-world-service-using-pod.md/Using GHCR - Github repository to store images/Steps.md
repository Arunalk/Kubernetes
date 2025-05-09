1. Build a image
```
docker build -t welcome-to-solaria .
```

3. Authenticate with GitHub:

```
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
```
```
echo "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" | docker login ghcr.io -u arunalk --password-stdin
```

4. Tag your image:
```
docker tag welcome-to-solaria ghcr.io/arunalk/welcome-to-solaria:latest
```

5. Push to GitHub Container Registry:
```
docker push ghcr.io/arunalk/welcome-to-solaria:latest
```
- `Verification:`
    Under packages your image should be present 

6. Create a secret:

```
kubectl create secret docker-registry ghcr-secret \
  --docker-server=ghcr.io \
  --docker-username=arunalk \
  --docker-password=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 \
  --docker-email=arunalk832@gmail.com
```

7. Deploy a pod
```
kubectl apply -f <file-name>
```