1. Build a image
    ```
    docker build -t <iamge-name> .
    ```

2. Save a Docker Image as a Tar File
    ```
    docker save -o hello-solaria.tar hello-solaria:latest
    ```

3. Transfer the Image to the Kubernetes Node
    ```
    scp hello-solaria.tar <node>:~/
    ```
4. Import the Image into containerd (Used by Kubernetes)

    ```
    ctr -n=k8s.io images import hello-solaria.tar
    ```

5. Verify

    ```
    crictl images | grep hello-solaria
    ```


**`With Docker`**

1. Build a image
    ```
    docker build -t <image-name> .
    ```

2. Run a container[Testing]
    ```
    docker run -d -p 8080:80 my-html-site
    ```
3. Push the Image to Docker Hub or a Private Registry
    ```
    docker tag my-html-site <your-dockerhub-username>/my-html-site
    docker push <your-dockerhub-username>/my-html-site
    ```