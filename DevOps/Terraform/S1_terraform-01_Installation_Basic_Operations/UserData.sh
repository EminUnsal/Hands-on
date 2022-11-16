# Wenn man irgendwo Terraform-Tools installieren will,klicke auf https://developer.hashicorp.com/terraform/downloads 
sudo yum update -y
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum -y install terraform