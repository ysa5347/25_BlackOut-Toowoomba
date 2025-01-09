resource "aws_s3_bucket" "blackout_toowoomba_bucket" {
  bucket = var.bucket_name
  acl    = "public-read"

  website {
    index_document = "index.html"
    error_document = "error.html"
  }

  tags = {
    Name        = var.bucket_name
    Environment = "production"
  }
}

resource "aws_s3_bucket_policy" "blackout_toowoomba_bucket_policy" {
  bucket = aws_s3_bucket.blackout_toowoomba_bucket.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = "*"
        Action = "s3:GetObject"
        Resource = "${aws_s3_bucket.blackout_toowoomba_bucket.arn}/*"
      }
    ]
  })
}