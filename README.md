# Pytest Plugin for DBT

This pytest plugin for dbt allows you to write unit tests for your dbt models. It makes testing your dbt models straightforward and efficient.

## Installation

Install the plugin using pip:

```sh
pip install pytest-dbt
```

## Usage

Follow these steps to use the plugin:

1. Create a dbt model as you normally would.
2. Run `dbt compile`.
3. Update or create a `pytest.ini` file, and set the `dbt_manifest_file_path` to point to the correct manifest file. For example:
```ini
[pytest]
dbt_manifest_file_path = target/manifest.json
```
4. Create tests using pytest. For instance, if we have a model [order_size](jaffle_shop/models/order_size.sql) and we want to confirm it has three columns, we can create a test file [test_order_size.py](jaffle_shop/tests/test_order_size.py) and add the following test:

```python
customer_no_order = [
    {'order_id': 1 , "order_size": 'small'},
    {'order_id': 2 , "order_size": 'large'},
    {'order_id': 3 , "order_size": 'medium'},
    {'order_id': 4 , "order_size": 'large'},
    {'order_id': 5 , "order_size": 'large'},
]

tables = {
    'orders': orders,
}

def test_customers_no_order():
    result = run_model('order_size', tables)
    assert assert_frame_equal(result, pd.DataFrame(customer_no_order)) == None
```
5. Run the tests using the command `pytest`:
```sh
pytest
```

## Why Not Use DBT Test?

While DBT Test is excellent for integration tests, it is less suited for unit testing.

## Why Pytest?

`pytest` is a mature testing framework with a wide range of plugins and strong community support. 

## Future Improvements

Here are the planned enhancements for the plugin:

- [ ] Add support for User-Defined Functions (UDFs).
- [ ] Implement a cyclic redundancy check (CRC) to monitor changes in the model.
- [ ] Incorporate a coverage report for SQL files.
- [ ] Add a command line option for passing in the test configuration. This will be especially helpful for Continuous Integration (CI) scenarios.
- [ ] Address issues related to missing files in `test_dbt_manifest_file_path = dbt_manifest.json`.
- [ ] Resolve the `AssertionError: File does not exist at path: dbt_manifest.json` error.