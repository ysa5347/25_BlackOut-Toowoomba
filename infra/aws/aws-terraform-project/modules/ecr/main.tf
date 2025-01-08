resource "aws_ecr_repository" "25_blackout_toowoomba" {
  name                 = var.repository_name
  image_tag_mutability = "MUTABLE"
  lifecycle_policy {
    rule {
      rule_priority = 1
      description  = "Expire untagged images"
      selection {
        tag_status = "UNTAGGED"
        count_type = "LIFETIME"
        count_unit = "DAYS"
        count_number = 30
      }
      action {
        type = "EXPIRY"
      }
    }
  }
}

output "repository_uri" {
  value = aws_ecr_repository.backend.repository_url
}