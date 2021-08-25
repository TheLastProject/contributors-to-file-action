#!/bin/sh -l

file_in_repo="$1"
git_name="$2"
git_email="$3"

mkdir -p "$(dirname "$file_in_repo")"
python3 /retrieve_contributors.py "$file_in_repo"

git config user.name "$git_name"
git config user.email "$git_email"

git add "$file_in_repo"
git commit -m "Update contributor list"
git push
