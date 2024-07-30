#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

SIZE=$(curl -s -o /dev/null -w '%{size_download}' "$URL")

echo "$SIZE"
