terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "4.8.0"
    }
  }
  backend "s3" {
  bucket = "mehmet-s3-depolama"
  key = "env/dev/tf-remote-backend.tfstate"
  region = "us-east-1"
  dynamodb_table = "olsunartik"
  encrypt = true
  }
}

provider "aws" {
  region  = "us-east-1"
}


locals {
  mytag = "mehmet-local-name"
}

data "aws_ami" "tf_ami" {
  most_recent      = true
  owners           = ["self"]

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