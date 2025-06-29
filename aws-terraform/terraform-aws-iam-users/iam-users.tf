resource "aws_iam_user" "this" {
  for_each = toset(var.iam_users)

  name = each.value
  tags = var.tags
}

resource "aws_iam_access_key" "this" {
  for_each = var.create_access_keys ? toset(var.iam_users) : []

  user       = each.value
  depends_on = [aws_iam_user.this]
}
