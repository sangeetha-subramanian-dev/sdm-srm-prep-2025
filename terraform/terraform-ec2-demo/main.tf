provider "aws" {
  region = var.region
}

resource "aws_instance" "web" {
  count         = 2
  ami           = var.ami_id
  instance_type = var.instance_type

  tags = {
    Name = "TF-Instance-ZealStyle"
  }
}
