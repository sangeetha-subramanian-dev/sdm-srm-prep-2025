provider "aws" {
  region = "ap-south-1"  # or your desired AWS region
}

module "ec2" {
  source         = "./terraform-modules/ec2-instance"  # not ../
  ami_id         = "ami-03f4878755434977f"
  instance_type  = "t2.micro"
  instance_count = 2
}
