provider "aws" {
  region = "ap-northeast-2"
  
}

module "vpc" {
  source = "./modules/vpc"
  vpc_cidr = var.vpc_cidr
  public_subnet_cidrs = var.public_subnet_cidrs
  private_subnet_cidrs = var.private_subnet_cidrs
  availability_zones = var.availability_zones
}

module "ecr" {
  source = "./modules/ecr"
  repository_name = var.ecr_repository_name
}

module "ecs" {
  source = "./modules/ecs"
  cluster_name = var.ecs_cluster_name
  task_definition = module.ecr.repository_uri
  public_subnet_ids = module.vpc.public_subnet_ids
}

module "s3" {
  source = "./modules/s3"
  bucket_name = var.s3_bucket_name
}