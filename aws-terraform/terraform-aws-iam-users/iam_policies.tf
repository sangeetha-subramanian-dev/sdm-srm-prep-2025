# Attach AWS-managed or custom IAM policies to IAM users
# This dynamically attaches multiple policies to multiple users
resource "aws_iam_user_policy_attachment" "user_policy_attachments" {
  for_each = {
    /*flattening to obtain key name and then correspoding each key with the user, policy_arn
    {
  "sangeetha-arn_aws_iam_aws_policy_AmazonS3ReadOnlyAccess" = {
    user       = "sangeetha"
    policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
  },
  "chandler-arn_aws_iam_aws_policy_AmazonEC2ReadOnlyAccess" = {
    user       = "chandler"
    policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess"
  }
}
*/
    for pair in flatten([
      for user, policies in var.iam_user_policy_map : [
        for policy_arn in policies : {
          key        = "${user}-${replace(policy_arn, ":", "_")}"
          user       = user
          policy_arn = policy_arn
        }
      ]
      ]) : pair.key => {
      user       = pair.user
      policy_arn = pair.policy_arn
    }
  }

  user       = each.value.user
  policy_arn = each.value.policy_arn
  # ✅ This tells Terraform to wait until IAM users are created
  depends_on = [aws_iam_user.this]
}


# Optional: Custom IAM policy creation (for fine-grained access)
# You can attach this policy to users by referencing aws_iam_policy.custom_readonly_policy.arn

resource "aws_iam_policy" "custom_readonly_policy" {
  name        = "CustomReadOnlyPolicy"
  description = "Custom policy allowing EC2 and S3 read-only access"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Action = [
          "ec2:Describe*",
          "s3:Get*",
          "s3:List*"
        ],
        Effect   = "Allow",
        Resource = "*"
      }
    ]
  })
}