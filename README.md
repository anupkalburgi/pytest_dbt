Not a replacement for `dbt test` 

## Instructions
```
poetry install
poetry run pytest

```


## Test cases
- [ ] add command line option to pass in the test config or else it would be hard to do in CI
- [ ] test_dbt_manifest_file_path = dbt_manifest.json missing files
- [ ] AssertionError: File does not exist at path: dbt_manifest.json