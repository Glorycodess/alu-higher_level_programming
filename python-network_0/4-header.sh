#!/bin/bash
# Send a GET request to the URL with a custom header
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
