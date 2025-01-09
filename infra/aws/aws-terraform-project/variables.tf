variable "region" {
  description = "The AWS region to deploy resources"
  default     = "ap-northeast-2"
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for the public subnets"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnet_cidrs" {
  description = "CIDR blocks for the private subnets"
  type        = list(string)
  default     = ["10.0.3.0/24", "10.0.4.0/24"]
}

variable "ecr_repository_name" {
  description = "The name of the ECR repository"
  default     = "blackout-toowoomba"
}

variable "ecs_cluster_name" {
  description = "The name of the ECS cluster"
  default     = "25-blackout-toowoomba-ecs-cluster"
}

variable "ecs_service_name" {
  description = "The name of the ECS service"
  default     = "25-blackout-toowoomba-ecs-service"
}

variable "s3_bucket_name" {
  description = "The name of the S3 bucket for front-end deployment"
  default     = "25-blackout-toowoomba-public-s3-bucket"
}