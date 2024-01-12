#!/bin/sh -l

file_in_repo="$1"
min_commit_count="$2"

mkdir -p "$(dirname "$file_in_repo")"
python3 /retrieve_contributors.py "$file_in_repo" "$min_commit_count"
