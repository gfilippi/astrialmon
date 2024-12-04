#!/bin/bash

# Function to display help message
show_help() {
    echo "Usage: $0 <input_string>"
    echo "Description: change Name for the current user login."
    echo ""
    echo "Options:"
    echo "  -h, --help    Show this help message and exit."
}

# Check if the user provided exactly one argument
if [[ "$#" -ne 1 ]]; then
    echo "Error: Invalid number of arguments."
    echo "Use '$0 --help' for usage information."
    exit 1
fi

# Check if the user requested help
case "$1" in
    -h|--help)
        show_help
        exit 0
        ;;
esac

# Validate that the input is non-empty and contains no invalid characters
if [[ -z "$1" || "$1" =~ ^-.* ]]; then
    echo "Error: Invalid input string."
    echo "Use '$0 --help' for usage information."
    exit 1
fi

# If all checks pass, print the message
MYUSER=`whoami`

sudo chfn -f $1 $MYUSER

echo
echo "hello $MYUSER: your name is now $1"
echo
