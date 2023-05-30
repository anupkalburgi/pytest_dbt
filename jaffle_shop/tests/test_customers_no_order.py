from test_customers import customers
from pytest_dbt.pytest_dbt import run_model
import pandas as pd
from pandas.testing import assert_frame_equal

customer_no_order = [
    {'customer_id': 4 }
]

tables = {
    'customers': customers,
}

def test_customers_no_order():
    result = run_model('customer_no_orders', tables)
    assert assert_frame_equal(result, pd.DataFrame(customer_no_order)) == None