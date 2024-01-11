# Contributors To File Docker action

This action retrieves your repo's list of contributors and writes it to a requested file.

## Inputs

### `repository`

GitHub repository to retrieve contributors of.

Defaults to the current repository.

### `token`

GitHub token to use, increases rate limit and thus reduces action runtime.

To not use a token, set value to an empty string.

Defaults to [automatically generated temporary GITHUB_TOKEN](https://docs.github.com/en/actions/security-guides/automatic-token-authentication).

### `file_in_repo`

**Required** The location of the file in the repository to write the contributor list to.

## Example usage

Put the following in `.github/workflows/contributors-to-file.yml`:

```yaml
jobs:
  contributors_to_file:
    runs-on: ubuntu-latest
    name: Write contributors to file
    steps:
    - name: Checkout repo
      id: checkout
      uses: actions/checkout@v3
    - name: Update contributors
      id: update_contributors
      uses: TheLastProject/contributors-to-file-action@v3
      with:
        file_in_repo: example/index.txt
    - name: Create Pull Request
      uses: peter-evans/create-pull-request@v5
      with:
        title: "Update contributors"
        commit-message: "Update contributors"
        branch-suffix: timestamp
on:
  schedule:
    - cron: '0 0 * * *'
```

## License
Creative Commons Zero 1.0 Universal
