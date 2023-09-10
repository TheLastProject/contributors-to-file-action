#!/bin/sh -l

token="$1"
file_in_repo="$2"

mkdir -p "$(dirname "$file_in_repo")"
python3 /retrieve_contributors.py "$token" "$file_in_repo"
