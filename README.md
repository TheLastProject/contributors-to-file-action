# Contributors To File Docker action

This action retrieves your repo's list of contributors and writes it to a requested file.

## Inputs

### `file_in_repo`

**Required** The location of the file in the repository to write the contributor list to.

## Example usage

Put the following in `.github/workflows/main.yml`:

```yaml
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
      uses: TheLastProject/contributors-to-file-action@v2
      with:
        file_in_repo: example/index.txt
    - name: Create Pull Request
      uses: peter-evans/create-pull-request@v3
      with:
        title: "Update contributors"
        commit-message: "Update contributors"
on:
  schedule:
    - cron: '0 0 * * *'
```

## API token

To avoid being rate limited, you can give the action access to the GitHub API token:

```yaml
    - name: Update contributors
      id: update_contributors
      uses: TheLastProject/contributors-to-file-action@v2
      with:
        file_in_repo: example/index.txt
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

## License
Creative Commons Zero 1.0 Universal
