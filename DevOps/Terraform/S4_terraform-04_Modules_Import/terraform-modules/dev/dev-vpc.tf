module "tf-vpc" {
    source = "../modules"
    environment = "DEV"
}

output "vpc_cidr_block" {
  value = module.tf-vpc.vpc_cidr
}