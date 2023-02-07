module "tf_vpc" {
  source      = "../modules"
  environment = "DEV"
}
output "vpc-cidr-block" {
  value = module.tf_vpc.vpc_cidr
}
output "public-subnet-cidr" {
  value = module.tf_vpc.public_subnet_cidr
}
output "private-subnet-cidr" {
  value = module.tf_vpc.private_subnet_cidr
}