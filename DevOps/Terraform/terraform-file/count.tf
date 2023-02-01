variable "num_of_buckets" {
  default = 2
}
resource "aws_s3_bucket" "tf-s3" {
  bucket = "${var.s3_bucket_name}-${count.index}"
  count = var.num_of_buckets
}
output "tf-example-s3" {
  value = aws_s3_bucket.tf-s3[*]
}