output "vpc_id" {
  value = module.vpc.vpc_id
}

output "public_subnet_ids" {
  value = module.vpc.public_subnet_ids
}

output "private_subnet_ids" {
  value = module.vpc.private_subnet_ids
}

output "ecr_repository_uri" {
  value = module.ecr.repository_uri
}

output "ecs_service_name" {
  value = module.ecs.service_name
}

output "ecs_task_definition_arn" {
  value = module.ecs.task_definition_arn
}

output "s3_bucket_name" {
  value = module.s3.bucket_name
}

output "s3_bucket_url" {
  value = module.s3.bucket_url
}