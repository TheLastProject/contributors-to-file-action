# Contributors To File Docker action

This action retrieves your repo's list of contributors and writes it to a requested file.

## Inputs

### `file_in_repo`

**Required** The location of the file in the repository to write the contributor list to.

### `git_user`

The name to commit under. Default: 'thelastproject/contributors-to-file'.

### `git_email`

The email to commit under. Default: 'no-reply@github.com'.

## Example usage

Put the following in `.github/workflows/main.yml`:
```
jobs:
  contributors_to_file:
    runs-on: ubuntu-latest
    name: Write contributors to file
    steps:
    - name: Checkout repo
      id: checkout
      uses: actions/checkout@v2
    - name: Update contributors
      id: update_contributors
      uses: TheLastProject/contributors-to-file-action@v1
      with:
        file_in_repo: example/index.html
on:
  schedule:
    - cron: '0 0 * * *'
```

## License
Creative Commons Zero 1.0 Universal
