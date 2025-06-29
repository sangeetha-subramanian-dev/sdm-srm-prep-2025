# Output IAM access keys only if they are created
# Uses ternary operator instead of invalid `condition = ...`

output "access_keys" {
  description = "Access keys for IAM users (only if created)"

  value = var.create_access_keys ? {
    for user, key in aws_iam_access_key.this :
    user => {
      access_key_id     = key.id
      secret_access_key = key.secret
    }
  } : {}

  sensitive = true # Prevents showing secrets in CLI output
}
