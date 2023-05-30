from test_orders import orders
import pandas as pd
from pandas.testing import assert_frame_equal
from pytest_dbt.pytest_dbt import run_model

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