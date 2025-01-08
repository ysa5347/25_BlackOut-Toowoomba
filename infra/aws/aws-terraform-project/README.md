# AWS Terraform Project

This project sets up a complete AWS infrastructure using Terraform. It includes a Virtual Private Cloud (VPC) with public and private subnets, an Amazon Elastic Container Registry (ECR) for storing Docker images, an Amazon Elastic Container Service (ECS) deployment using Fargate, and a public S3 bucket for front-end deployment.

## Project Structure

```
aws-terraform-project
├── modules
│   ├── vpc
│   │   ├── main.tf         # VPC configuration
│   │   ├── outputs.tf      # Outputs for VPC
│   │   ├── variables.tf    # Input variables for VPC
│   ├── ecr
│   │   ├── main.tf         # ECR configuration
│   │   ├── outputs.tf      # Outputs for ECR
│   │   ├── variables.tf    # Input variables for ECR
│   ├── ecs
│   │   ├── main.tf         # ECS configuration
│   │   ├── outputs.tf      # Outputs for ECS
│   │   ├── variables.tf    # Input variables for ECS
│   └── s3
│       ├── main.tf         # S3 configuration
│       ├── outputs.tf      # Outputs for S3
│       ├── variables.tf     # Input variables for S3
├── main.tf                 # Root Terraform configuration
├── outputs.tf              # Outputs from the root configuration
├── variables.tf            # Input variables for the root configuration
└── README.md               # Project documentation
```

## Setup Instructions

1. **Install Terraform**: Ensure you have Terraform installed on your machine. You can download it from the [Terraform website](https://www.terraform.io/downloads.html).

2. **Configure AWS Credentials**: Set up your AWS credentials using the AWS CLI or by creating a `~/.aws/credentials` file.

3. **Clone the Repository**: Clone this repository to your local machine.

4. **Navigate to the Project Directory**: Change into the project directory.

5. **Initialize Terraform**: Run the following command to initialize the Terraform configuration:
   ```
   terraform init
   ```

6. **Plan the Deployment**: Generate an execution plan with:
   ```
   terraform plan
   ```

7. **Apply the Configuration**: Deploy the infrastructure with:
   ```
   terraform apply
   ```

8. **Access Outputs**: After deployment, you can access the outputs defined in the `outputs.tf` files to get information about the created resources.

## Usage

This project is designed to be modular, allowing you to easily modify or extend the infrastructure as needed. You can customize the input variables in the `variables.tf` files to suit your requirements.

For more detailed information on each module, refer to the respective `README.md` files within each module directory.