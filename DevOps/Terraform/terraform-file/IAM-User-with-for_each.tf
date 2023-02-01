# IAMFullAccess`` policy lazim
variable "users" {
  default = ["santino", "michael", "fredo"]
}
locals {
  mytags= "mehmet"
}
resource "aws_s3_bucket" "tf-s3" {
  # bucket = "var.s3_bucket_name.${count.index}"
  # count = var.num_of_buckets
  # count = var.num_of_buckets != 0 ? var.num_of_buckets : 1
  for_each = toset(var.users)
  bucket   = "${local.mytags}-example-tf-s3-bucket-${each.value}"
}

resource "aws_iam_user" "new_users" {
  for_each = toset(var.users)  #set'e donusturuyor
  name = each.value
}

output "uppercase_users" {
  value = [for user in var.users : upper(user) if length(user) > 6]
}
output "bucket-1" {
  value = aws_s3_bucket.tf-s3["fredo"].bucket 
}
output "bucket-2" {
  value = aws_s3_bucket.tf-s3["michael"].bucket 
}