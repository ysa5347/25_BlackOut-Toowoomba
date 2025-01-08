resource "aws_s3_bucket" "frontend_bucket" {
  bucket = var.bucket_name
  acl    = "public-read"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.frontend_bucket.bucket
}

output "bucket_url" {
  value = aws_s3_bucket.frontend_bucket.website_endpoint
}