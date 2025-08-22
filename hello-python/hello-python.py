#!/usr/bin/env python3
import os
import sys
from datetime import datetime

def main():
    # Get optional input variables from environment or use defaults
    message = os.getenv('MESSAGE', 'Hello World!')
    user_name = os.getenv('USER_NAME', 'World')
    environment = os.getenv('ENVIRONMENT', 'development')
    repeat_count = int(os.getenv('REPEAT_COUNT', '1'))
    enable_timestamp = os.getenv('ENABLE_TIMESTAMP', 'false').lower() in ('true', '1', 'yes')
    output_format = os.getenv('OUTPUT_FORMAT', 'text')  # text or json
    
    # Build the final message
    if enable_timestamp:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        final_message = f"{message}, {user_name}! Running in {environment} at {timestamp}"
    else:
        final_message = f"{message}, {user_name}! Running in {environment}"
    
    # Output based on format
    if output_format.lower() == 'json':
        import json
        output = {
            "message": final_message,
            "user_name": user_name,
            "environment": environment,
            "repeat_count": repeat_count,
            "timestamp": datetime.now().isoformat() if enable_timestamp else None
        }
        print(json.dumps(output, indent=2))
    else:
        # Text format
        for i in range(repeat_count):
            iteration_msg = f"{final_message} (iteration {i + 1})" if repeat_count > 1 else final_message
            print(iteration_msg)

if __name__ == "__main__":
    main()