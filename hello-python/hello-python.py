#!/usr/bin/env python3
import os

def main():
    # Get input variables from environment or use defaults
    first_string = os.getenv('first_string', 'Hello')
    second_string = os.getenv('second_string', 'World')
    
    # Print the two strings
    print(first_string)
    print(second_string)

if __name__ == "__main__":
    main()