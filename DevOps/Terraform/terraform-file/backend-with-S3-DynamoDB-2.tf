terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.8.0"
    }
  }
  backend "s3" {
    bucket = "tf-remote-s3-bucket-mehmet"
    key = "env/dev/tf-remote-backend.tfstate"
    region = "us-east-1"
    dynamodb_table = "tf-s3-app-lock"
    encrypt = true
  }
}
provider "aws" {
  region  = "us-east-1"
}

locals {
  mytag = "my-local-name"
}

data "aws_ami" "tf_ami" {
  most_recent      = true
  owners           = ["self"]
  # owners           = ["amazon"]
  # filter {
  #   name = "name"                           Burada amazondaki en guncel image'i cekiyorum.automatik hale getirdik image'i . hep en guncel halini kullaniyoruz
  #   values = ["amzn2-ami-kernel-5.10*"]
  # }

  filter {
    name = "virtualization-type"
    values = ["hvm"]
  }
}

variable "ec2_type" {
  default = "t2.micro"
}

resource "aws_instance" "tf-ec2" {
  ami           = data.aws_ami.tf_ami.id
  instance_type = var.ec2_type
  key_name      = "First_Key"
  tags = {
    Name = "${local.mytag}-this is from my-ami"
  }
}