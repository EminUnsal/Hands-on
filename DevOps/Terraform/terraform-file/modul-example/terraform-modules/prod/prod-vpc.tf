module "prod" {
    source = "../modules"
    environment = "PROD"
}
output "vpc-cidr-block" {
  value = module.prod.vpc_cidr
}
output "vpc-public_subnet_cidr" {
  value = module.prod.public_subnet_cidr
}