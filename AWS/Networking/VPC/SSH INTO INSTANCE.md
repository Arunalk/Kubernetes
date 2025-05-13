# Step-by-Step SSH into AWS EC2

## Prerequisites
- You have an EC2 instance running.

- You have the private key file (.pem) from when you launched the instance.

- Your instance's IP address (found in the EC2 Dashboard).

- The .pem file has correct permissions.

1. Ensure Correct Permissions on PEM File
Run the following command to ensure that your .pem file has the correct permissions:

```
chmod 400 path/to/your-key.pem
```

2. Connect Using SSH
Run the command below (replace placeholders with your actual values):

```
ssh -i path/to/your-key.pem ec2-user@<private-ip>
```


3. Troubleshooting Tips
- Make sure the instance’s security group allows inbound SSH (port 22).

- Use the public IP, not the private IP.

- Ensure the .pem file matches the key pair used to launch the instance.