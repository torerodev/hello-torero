variable "message" {
  description = "Custom message to display"
  type        = string
  default     = "Hello World"
}

variable "environment" {
  description = "Environment name (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "user_name" {
  description = "Name of the user running the plan"
  type        = string
  default     = "User"
}

variable "repeat_count" {
  description = "Number of times to repeat the message"
  type        = number
  default     = 1
}

variable "enable_timestamp" {
  description = "Whether to include timestamp in output"
  type        = bool
  default     = false
}

locals {
  timestamp = var.enable_timestamp ? timestamp() : ""
  final_message = var.enable_timestamp ? "${var.message} from ${var.user_name} in ${var.environment} at ${local.timestamp}" : "${var.message} from ${var.user_name} in ${var.environment}"
}

resource "null_resource" "this" {
  count = var.repeat_count
  
  provisioner "local-exec" {
    command = "echo '${local.final_message} (iteration ${count.index + 1})'"
  }
}

output "message" {
  description = "The message that was displayed"
  value       = local.final_message
}

output "environment" {
  description = "The environment this was run in"
  value       = var.environment
}

output "repeat_count" {
  description = "Number of times the message was repeated"
  value       = var.repeat_count
}