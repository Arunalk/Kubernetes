## **<span style="color:#A7C7E7;">Pulling Conatiner image from private registries</span>**

> When deploying a Pod on `Amazon EKS` that pulls images from ECR, you need to authenticate Kubernetes to ECR.

This authentication can be handled in three ways:

- `Secrets` (ImagePullSecrets) → Manual authentication
- `IAM Role` (Node IAM Role) → Node-level authentication
- `IAM Roles for Service Accounts`(IRSA) → Pod-level authentication


### 1. `Using Secrets (imagePullSecrets)`

> 🔹 `When to Use?`</br>
You are running Kubernetes outside AWS (e.g., Minikube, GKE, AKS).Your EKS worker nodes don’t have IAM permissions to access ECR.You need a quick workaround without modifying IAM roles.

> 🔹 `How It Works?`</br>
A Docker registry secret stores AWS credentials to authenticate with ECR. The pod references this secret when pulling images.

`Why docker command/registry`
- Kubernetes uses the Docker credential format for private registry authentication, even when dealing with ECR, GHCR, or other registries.
> `Kubernetes Follows Docker’s Authentication Format`
> - Kubernetes does not have a built-in ECR authentication mechanism, so it relies on the standard Docker - credential format (.dockerconfigjson).
> - The kubectl create secret docker-registry command stores credentials in the same format as Docker's config.json file.


**`Step 1: Create the Kubernetes Secret`**

Run the following command to create a secret that stores ECR credentials:

```
kubectl create secret docker-registry ecr-secret \
  --docker-server=<AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com \
  --docker-username=AWS \
  --docker-password=$(aws ecr get-login-password --region <AWS_REGION>) \
  --namespace default
```

**`Step 2: Modify pod.yaml to Use the Secret`**

```
apiVersion: v1
kind: Pod
metadata:
  name: welcome
spec:
  containers:
    - name: greetings
      image: <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/greetings:latest
      imagePullPolicy: Always
  imagePullSecrets:
    - name: ecr-secret
```

### 2. `Using IAM Role for EKS Nodes (Default for EC2-based EKS)`

> 🔹 `When to Use?`</br>
Your EKS worker nodes run on EC2 instances.
You want all pods on a node to pull images without secrets.
You are okay with sharing permissions across all pods on a node.

> 🔹 `How It Works?`</br>
Each EKS worker node (EC2 instance) has an IAM role attached.
This IAM role automatically grants permission to pull ECR images.

**`Step 1:`** `Attach an IAM Policy to the Node`

> `Identify the IAM role used by your EKS worker nodes:`

```
aws eks describe-nodegroup --cluster-name <EKS_CLUSTER_NAME> --nodegroup-name <NODE_GROUP_NAME> --query "nodegroup.iamRoleArn"
```
> `Attach this IAM policy to the role:`
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken",
                "ecr:BatchCheckLayerAvailability",
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage"
            ],
            "Resource": "*"
        }
    ]
}
```
> **`Step 2:`** `Deploy the Pod (No Secret Needed)`
```
apiVersion: v1
kind: Pod
metadata:
  name: welcome
spec:
  containers:
    - name: greetings
      image: <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/greetings:latest
      imagePullPolicy: Always

```

### `Using IAM Roles for Service Accounts (IRSA)`

> **🔹 `When to Use?`**
You want pod-level permissions (not node-wide access). You need fine-grained access control for ECR authentication.

> **🔹 `How It Works?`**
Each Kubernetes ServiceAccount is linked to an IAM role. Only pods using that ServiceAccount get ECR access.

**`Step 1:`** **`Create an IAM Role for the ServiceAccount`**

```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: {{ .Release.Name }}
  annotations:
    eks.amazonaws.com/role-arn: {{ .Values.serviceAccount.roleArn }}   ## Role arn: which has ECR policy attached
```

**`Step 2:`** **`Modify pod/deployment yaml with ServiceAccount`**

```
apiVersion: v1
kind: Pod
metadata:
  name: welcome
spec:
  serviceAccountName: ecr-serviceaccount
  containers:
    - name: greetings
      image: <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/greetings:latest
      imagePullPolicy: Always
```

- IRSA (IAM Roles for Service Accounts) allows Kubernetes pods to assume an IAM role directly.Instead of storing Docker credentials in a Kubernetes Secret, IRSA allows EKS pods to authenticate with AWS services (like ECR) natively using IAM permissions.
- IRSA have many use-cases, it's most likely to grant granular permissions such as what if the applications needs to store/retrieve files in Amazon S3, dynamodb, redis etc

## 🔹 Summary: Choosing the Best Approach

| **Method**                       | **When to Use?**                                   | **Pros**                                          | **Cons**                                      |
|----------------------------------|--------------------------------------------------|--------------------------------------------------|----------------------------------------------|
| **Secrets (`imagePullSecrets`)**  | Kubernetes outside AWS or without IAM access    | ✅ Works anywhere                               | ❌ Credentials expire, manual updates needed |
| **IAM Role for EKS Node**         | Default for EC2-based EKS                        | ✅ No secrets required, automatic for all pods | ❌ All pods on a node share the IAM role     |
| **IAM Roles for Service Accounts (IRSA)** | Best for Fargate & security-sensitive workloads[each pod gets its own IAM permissions] | ✅ Pod-level IAM access (best security)        | ❌ Requires extra IAM setup                  |


## 🔹 Authentication Methods for Different Registries

| **Registry**                  | **Recommended Authentication Method**                                    |
|--------------------------------|------------------------------------------------------------------------|
| **Amazon ECR (AWS)**          | ✅ IAM Role for Nodes (EKS EC2-based clusters) <br> ✅ IRSA (for pod-level access) <br> ❌ ImagePullSecret (only if outside AWS) |
| **GitHub Container Registry (GHCR)** | ✅ ImagePullSecret (GitHub PAT token required)                         |
| **Docker Hub (Private Repos)** | ✅ ImagePullSecret (Docker Hub credentials required)                    |
| **Google Container Registry (GCR)** | ✅ ImagePullSecret (Google Service Account JSON Key required) <br> ✅ IAM Role (for GKE Workload Identity) |

> **<span style="color:orange;">Note:</span>** Fargate doesn't have IAM roles attached to nodes.
