data "aws_ami" "amazon-linux-2" {
  owners      = ["amazon"]
  most_recent = true

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }

  filter {
    name   = "owner-alias"
    values = ["amazon"]
  }
# https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html
  filter {
    name   = "name"
    values = ["amzn2-ami-kernel-5.10-hvm*"]
  }
}

data "template_file" "userdata" {
  template = file("${abspath(path.module)}/userdata.sh") # ${abspath(path.module)} ./ demek
  vars = {
    server-name = var.server_name # server_name degiskenini alacak 
  }
}

resource "aws_instance" "tfmyec2" {
  ami = data.aws_ami.amazon-linux-2.id
  instance_type = var.instance_type
  count = var.num_of_instance
  key_name = var.key_name
  vpc_security_group_ids = [aws_security_group.tf-sec-gr.id]
  ##vpc_security_group_ids hepsinde kullanabiliriz. birde security_groups var o da sadece default VPC'de kullanilir. koseli parantezde tanimlanmali.
  user_data = data.template_file.userdata.rendered #rendered demek 'islemek' demek. bunu userdata.sh'a isler
  # Normalde file function'uyla yapiyorduk.external bir script'e variable gondermenin yolu
  tags = {
    Name = var.tag
  }
}

resource "aws_security_group" "tf-sec-gr" {
  name = "${var.tag}-terraform-sec-grp"
  tags = {
    Name = var.tag
  }

  dynamic "ingress" {
    for_each = var.docker-instance-ports
    iterator = port # iterator kullanmazsak default olarak ingress ismine degerleri tanimlar. orn ingress.value 
    content {
      from_port = port.value
      to_port = port.value
      protocol = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port =0
    protocol = "-1"
    to_port =0
    cidr_blocks = ["0.0.0.0/0"]
  }
}