# -------------------------------
# 1. Create IAM Role for EC2
# -------------------------------

resource "aws_iam_role" "ec2_service_role" {
  name = var.ec2_role_name

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Principal = {
          Service = "ec2.amazonaws.com"
        },
        Action = "sts:AssumeRole"
      }
    ]
  })

  description = "IAM role for EC2 instances to access AWS services"
}

# -------------------------------
# 2. Attach AWS-Managed Policy (example: S3 read-only)
# -------------------------------

resource "aws_iam_role_policy_attachment" "s3_read_only_for_ec2" {
  for_each = toset(var.ec2_role_policy_arns)
   role       = aws_iam_role.ec2_service_role.name
   policy_arn = each.key

}

# -------------------------------
# 3. Create Instance Profile
# Required to attach this role to an EC2 instance
# -------------------------------

resource "aws_iam_instance_profile" "ec2_instance_profile" {
  name = var.ec2_instance_profile_name
  role = aws_iam_role.ec2_service_role.name
}
