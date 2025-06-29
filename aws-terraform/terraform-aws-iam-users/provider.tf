# Configure AWS provider with region from variable

provider "aws" {
  region  = var.aws_region
  profile = "my-profile"
}

