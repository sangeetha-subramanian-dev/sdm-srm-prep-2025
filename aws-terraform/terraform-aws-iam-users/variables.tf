# Input variables used across the config

# Region to deploy the IAM users
variable "aws_region" {
  description = "The AWS region to use"
  type        = string
  default     = "ap-south-1"
}

# List of IAM user names to be created
variable "iam_users" {
  description = "List of IAM user names to create"
  type        = list(string)
}


# IAM policy attachments: map of user → list of policy ARNs
variable "iam_user_policy_map" {
  description = "Map of user with the iam policy arn"
  type        = map(list(string))
  default = {
  }
}

# Flag to determine if access keys should be created
variable "create_access_keys" {
  description = "Whether to create access keys for the users"
  type        = bool
  default     = false
}

# Tags to apply to resources
variable "tags" {
  description = "Common tags for all resources"
  type        = map(string)
  default = {
    Owner       = "Sangeetha"
    Environment = "dev"
  }
}

# IAM Groups
variable "iam_groups" {
  description = "List of IAM groups"
  type        = list(string)
  default     = []
}

# IAM Group Memberships
variable "iam_group_membership" {
  description = "Map of group memberships"
  type = map(object({
    group = string
    users = list(string)
  }))
  default = {}
}

# IAM Group Policy Attachments
variable "iam_group_policy_attachments" {
  description = "Map of group → list of policy ARNs"
  type        = map(list(string))
  default     = {}
}


