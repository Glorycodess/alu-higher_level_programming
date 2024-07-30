#!/bin/bash

# Check if a URL was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Use curl to get the size of the response body
# -s: Silent mode (don't show progress or error messages)
# -o /dev/null: Discard the response body
# -w '%{size_download}': Output the size of the response body in bytes
SIZE=$(curl -s -o /dev/null -w '%{size_download}' "$URL")

# Output the size without additional text
echo "$SIZE"
