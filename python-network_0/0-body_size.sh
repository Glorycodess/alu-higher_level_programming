#!/bin/bash
# This script fetches the size of the response body from a given URL
SIZE=$(curl -s -o /dev/null -w '%{size_download}' "$1")
echo "$SIZE"
