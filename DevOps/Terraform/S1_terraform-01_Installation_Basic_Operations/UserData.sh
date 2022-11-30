# Wenn man irgendwo Terraform-Tools installieren will,klicke auf https://developer.hashicorp.com/terraform/downloads 

#! /bin/bash

yum update -y
yum install -y yum-utils
yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
yum -y install terraform




