output "bucket_name" {
  value = aws_s3_bucket.blackout_toowoomba_bucket.bucket
}

output "bucket_url" {
  value = aws_s3_bucket.blackout_toowoomba_bucket.website_endpoint
}