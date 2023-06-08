# DBT Unit Testing with Pytest Plugin

The Pytest plugin for DBT simplifies the task of writing unit tests for your DBT models, offering a straightforward and efficient testing procedure.

## How to Install

Install this plugin by utilizing pip. Simply run the following command:

```sh
pip install pytest-dbt
```

## Steps for Use

To use this plugin, follow these instructions:

1. Begin by creating a DBT model in your usual manner.
2. Next, execute `dbt compile`.
3. Now, either create a new `pytest.ini` file or modify an existing one. In this file, set the `dbt_manifest_file_path` to point towards the appropriate manifest file. See the example below:

```ini
[pytest]
dbt_manifest_file_path = target/manifest.json
```
4. The next step is to create your tests using pytest. As an example, let's assume you have a model called [order_size](jaffle_shop/models/order_size.sql) and you want to verify it has three columns. You can create a test file [test_order_size.py](jaffle_shop/tests/test_order_size.py) and add the following test:

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

### Incorporating User-Defined Functions (UDFs)
If your databases have defined functions, you can incorporate them into the execution. For instance, if there's a model [customer_details](jaffle_shop/models/customer_details.sql) which employs a UDF `full_name`, you can design a test file [test_customer_details.py](jaffle_shop/tests/test_udf_customer_details.py) and append the following test:

```python
udfs = {"full_name": lambda name, last_name: f"{name} {last_name}"}

def test_customer_details():
    result = run_model("customer_details", tables=tables, udfs=udfs)
    assert assert_frame_equal(result, pd.DataFrame(customer_details)) == None
```

5. Finally, execute the tests with the command `pytest`:

```sh
➜  jaffle_shop git$ ✗ pytest
============================================================= test session starts =============================================================
platform darwin -- Python 3.8.6, pytest-7.3.1, pluggy-1.0.0
rootdir: /Users/anupkalburgi/projects/pytest-dbt/jaffle_shop
configfile: pytest.ini
plugins: dbt-0.1.1
collected 5 items

tests/test_customers.py .                                                                                                               [ 20%]
tests/test_customers_no_order.py .                                                                                                      [ 40%]
tests/test_order_size.py .                                                                                                              [ 60%]
tests/test_orders.py .                                                                                                                  [ 80%]
tests/test_udf_customer_details.py .                                                                                                    [100%]

============================================================== 5 passed in 0.15s ==============================================================
```


## Why Not Utilize DBT Test?

While DBT Test excels in conducting integration tests, it falls short when applied to unit testing.

## The Advantage of Pytest

Pytest is a robust testing framework with a wide variety of plugins, backed by strong community support.

## Anticipated Updates

The following enhancements are being planned for the plugin:

- [x] Inclusion of support for User-Defined Functions (UDFs).
- [ ] Incorporation of a cyclic redundancy check (CRC) for tracking model changes.
- [ ] Integration of a coverage report for SQL files.
- [ ] Addition of a command-line option for test configuration input, which will be particularly beneficial for Continuous Integration (CI) scenarios.
- [ ] Rectification of issues concerning missing files in `test_dbt_manifest_file_path = dbt_manifest.json`.
- [ ] Resolution of the `AssertionError: File does not exist at path: dbt_manifest.json` error.
