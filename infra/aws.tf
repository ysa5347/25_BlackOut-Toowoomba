# Terraform Code for AWS Web Project

# Provider settings
provider "aws" {
  region = "us-east-1"
}

# create S3 bucket (streamlit deploy)
resource "aws_s3_bucket" "frontend_bucket" {
  bucket = "my-frontend-bucket"
  acl    = "public-read"
}

resource "aws_s3_bucket_website_configuration" "frontend_website" {
  bucket = aws_s3_bucket.frontend_bucket.id
  index_document {
    suffix = "index.html"
  }
}

# CloudFront 배포
resource "aws_cloudfront_distribution" "frontend_distribution" {
  origin {
    domain_name = aws_s3_bucket.frontend_bucket.bucket_regional_domain_name
    origin_id   = "frontendS3Origin"
  }

  enabled             = true
  default_root_object = "index.html"

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "frontendS3Origin"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }
}

# EKS 클러스터 생성 (Django Backend 배포)
resource "aws_eks_cluster" "backend_cluster" {
  name     = "backend-cluster"
  role_arn = aws_iam_role.eks_cluster_role.arn

  vpc_config {
    subnet_ids = [aws_subnet.public_subnet_1.id, aws_subnet.public_subnet_2.id]
  }
}

# API Gateway 생성
resource "aws_api_gateway_rest_api" "backend_api" {
  name        = "backend-api"
  description = "API Gateway for Django Backend"
}

resource "aws_api_gateway_resource" "proxy" {
  rest_api_id = aws_api_gateway_rest_api.backend_api.id
  parent_id   = aws_api_gateway_rest_api.backend_api.root_resource_id
  path_part   = "{proxy+}"
}

resource "aws_api_gateway_method" "proxy_method" {
  rest_api_id   = aws_api_gateway_rest_api.backend_api.id
  resource_id   = aws_api_gateway_resource.proxy.id
  http_method   = "ANY"
  authorization = "NONE"
}

# EC2 인스턴스 생성 (DB 서버)
resource "aws_instance" "database_instance" {
  ami           = "ami-12345678"
  instance_type = "t3.medium"
  subnet_id     = aws_subnet.public_subnet_1.id
  key_name      = "my-key-pair"

  tags = {
    Name = "DatabaseInstance"
  }
}

# VPC 및 서브넷 생성
resource "aws_vpc" "main_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public_subnet_1" {
  vpc_id                  = aws_vpc.main_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true
}

resource "aws_subnet" "public_subnet_2" {
  vpc_id                  = aws_vpc.main_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "us-east-1b"
  map_public_ip_on_launch = true
}

resource "aws_internet_gateway" "main_gw" {
  vpc_id = aws_vpc.main_vpc.id
}

resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.main_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main_gw.id
  }
}

resource "aws_route_table_association" "public_assoc_1" {
  subnet_id      = aws_subnet.public_subnet_1.id
  route_table_id = aws_route_table.public_rt.id
}

resource "aws_route_table_association" "public_assoc_2" {
  subnet_id      = aws_subnet.public_subnet_2.id
  route_table_id = aws_route_table.public_rt.id
}

output "frontend_url" {
  value = aws_cloudfront_distribution.frontend_distribution.domain_name
}

output "database_ip" {
  value = aws_instance.database_instance.public_ip
} 
