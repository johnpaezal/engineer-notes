# Infrastructure as Code – Terraform
*Managing infrastructure with code*

## Infrastructure as Code (IaC)
*Define and provision infrastructure using code files*

**IaC** – Managing servers, networks, databases via code instead of manual clicks  
**Terraform** – Most popular IaC tool, works with AWS, GCP, Azure and more  
**Provider** – Plugin that lets Terraform talk to a cloud platform

### Why IaC

```
❌ Manual (ClickOps):           ✅ IaC:
- Inconsistent environments     - Same config every time
- No history of changes         - Git history of all changes
- Hard to reproduce             - Recreate with one command
- Error-prone                   - Reviewed and tested
```

---

## Terraform Core Concepts
*Key building blocks*

**Resource** – Infrastructure component (EC2, S3 bucket, database)  
**Provider** – API interface to a cloud (aws, google, azurerm)  
**State** – File tracking real infrastructure vs config  
**Plan** – Preview of changes before applying  
**Module** – Reusable group of resources

---

## Basic Workflow
*Standard Terraform commands*

```bash
terraform init      # download providers and modules
terraform plan      # preview what will change
terraform apply     # create/update infrastructure
terraform destroy   # delete all managed infrastructure
```

---

## HCL Syntax
*HashiCorp Configuration Language*

```hcl
# Configure provider
provider "aws" {
  region = "us-east-1"
}

# Create a resource
resource "aws_s3_bucket" "my_bucket" {
  bucket = "my-app-uploads-2025"
}

# Variables
variable "environment" {
  type    = string
  default = "dev"
}

# Outputs
output "bucket_name" {
  value = aws_s3_bucket.my_bucket.id
}
```

---

## Resources
*Defining infrastructure components*

```hcl
# EC2 Instance
resource "aws_instance" "web_server" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t3.micro"

  tags = {
    Name        = "web-server"
    Environment = var.environment
  }
}

# S3 Bucket
resource "aws_s3_bucket" "uploads" {
  bucket = "my-app-uploads"
}

# Security Group
resource "aws_security_group" "allow_http" {
  name = "allow_http"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

---

## Variables & Outputs
*Parameterize and expose values*

```hcl
# variables.tf
variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  default     = "t3.micro"
}

variable "environment" {
  type = string  # passed via CLI or .tfvars
}

# outputs.tf
output "instance_ip" {
  description = "Public IP of the web server"
  value       = aws_instance.web_server.public_ip
}
```

```bash
# Pass variables
terraform apply -var="environment=prod"

# Or use a file
terraform apply -var-file="prod.tfvars"
```

---

## State
*Terraform tracks what it created*

**terraform.tfstate** – JSON file mapping config to real infrastructure  
**Remote state** – Store state in S3 + DynamoDB (required for teams)

```hcl
# Remote state in S3 (recommended for teams)
terraform {
  backend "s3" {
    bucket         = "my-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    dynamodb_table = "terraform-locks"
  }
}
```

---

## Modules
*Reusable infrastructure components*

```hcl
# Call a module
module "vpc" {
  source = "./modules/vpc"

  cidr_block  = "10.0.0.0/16"
  environment = var.environment
}

# Use module outputs
resource "aws_instance" "app" {
  subnet_id = module.vpc.public_subnet_id
}
```

```
project/
├── main.tf
├── variables.tf
├── outputs.tf
└── modules/
    ├── vpc/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    └── ec2/
        ├── main.tf
        └── variables.tf
```

---

## File Structure
*Standard Terraform project layout*

```
├── main.tf          # main resources
├── variables.tf     # input variables
├── outputs.tf       # output values
├── providers.tf     # provider config
├── versions.tf      # terraform + provider versions
└── terraform.tfvars # variable values (not in git if secrets)
```

---

## Best Practices

- Always run `terraform plan` before `apply`
- Store state remotely (S3 + DynamoDB for AWS)
- Never store secrets in `.tf` files — use AWS Secrets Manager or env vars
- Use modules for repeated patterns
- Tag all resources with `environment`, `project`, `owner`
- Lock provider versions in `versions.tf`
- One environment per state file (dev, staging, prod separated)
