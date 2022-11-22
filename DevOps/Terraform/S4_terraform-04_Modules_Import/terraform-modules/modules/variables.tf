variable "environment" {
  default = "clarusway"
}

variable "vpc_cidr_block" {
  default = "10.0.0.0/16"
  description = "This is our VPC cidr-block"
}

variable "public_subnet_cidr" {
  default = "10.0.1.0/24"
  description = "This is our Public Subnet cidr-block"
}

variable "private_subnet_cidr" {
  default = "10.0.2.0/24"
  description = "This is our Private Subnet cidr-block"
}