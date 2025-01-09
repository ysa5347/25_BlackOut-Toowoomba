variable "cluster_name" {
  description = "The name of the ECS cluster"
  type        = string
}

variable "service_name" {
  description = "The name of the ECS service"
  type        = string
}

variable "task_definition" {
  description = "The task definition for the ECS service"
  type        = string
}

variable "container_image" {
  description = "The Docker image to use for the container"
  type        = string
}

variable "desired_count" {
  description = "The desired number of instances of the service"
  type        = number
  default     = 1
}

variable "subnet_ids" {
  description = "The list of subnet IDs for the ECS service"
  type        = list(string)
}

variable "security_group_ids" {
  description = "The list of security group IDs for the ECS service"
  type        = list(string)
}