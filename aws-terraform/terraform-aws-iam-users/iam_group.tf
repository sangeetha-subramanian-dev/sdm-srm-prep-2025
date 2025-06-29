# -------------------------------
# 1. Create IAM Groups
# -------------------------------
resource "aws_iam_group" "this" {
  for_each = toset(var.iam_groups)

  name = each.key
  path = "/"
}

# -------------------------------
# 2. Attach IAM Users to Groups
# -------------------------------
resource "aws_iam_group_membership" "this" {
  for_each = var.iam_group_membership

  name  = "${each.key}-membership"
  users = each.value.users   # List of IAM usernames
  group = aws_iam_group.this[each.value.group].name
}

# -------------------------------
# 3. Attach Policies to Groups
# -------------------------------
resource "aws_iam_group_policy_attachment" "this" {
  for_each = {
    for item in flatten([
      for group, policy_arns in var.iam_group_policy_attachments : [
        for policy_arn in policy_arns : {
          key        = "${group}-${replace(policy_arn, ":", "_")}"
          group      = group
          policy_arn = policy_arn
        }
      ]
    ]) : item.key => {
      group      = item.group
      policy_arn = item.policy_arn
    }
  }

  group      = aws_iam_group.this[each.value.group].name
  policy_arn = each.value.policy_arn

  depends_on = [aws_iam_group.this]
}
