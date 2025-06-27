terraform {
  backend "s3" {
    bucket         = "terraform-state-sangee2025"
    key            = "dev/terraform.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
