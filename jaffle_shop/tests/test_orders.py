from test_customers import stg_orders, stg_payments
import pandas as pd
from pytest_dbt.pytest_dbt import run_model
from pandas.testing import assert_frame_equal

customer_no_order = [
    {'customer_id': 4 }
]

tables = {
    'stg_orders':stg_orders ,
    'stg_payments': stg_payments,
}

orders = [
    {'order_id': 1, 'customer_id': 1, 'order_date': '2020-01-01' ,'status': 'returned',  'credit_card_amount': 0, 'coupon_amount': 0, 'bank_transfer_amount': 0, 'gift_card_amount': 0, 'amount': 10},
    {'order_id': 2, 'customer_id': 1, 'order_date': '2020-01-02', 'status': 'completed', 'credit_card_amount': 0, 'coupon_amount': 0, 'bank_transfer_amount': 0, 'gift_card_amount': 0, 'amount': 190},
    {'order_id': 3, 'customer_id': 2, 'order_date': '2020-01-01', 'status': 'completed', 'credit_card_amount': 0, 'coupon_amount': 0, 'bank_transfer_amount': 0, 'gift_card_amount': 0, 'amount': 50},
    {'order_id': 4, 'customer_id': 2, 'order_date': '2020-01-04', 'status': 'completed', 'credit_card_amount': 0, 'coupon_amount': 0, 'bank_transfer_amount': 0, 'gift_card_amount': 0, 'amount': 250},
    {'order_id': 5, 'customer_id': 3, 'order_date': '2020-01-05', 'status': 'completed', 'credit_card_amount': 0, 'coupon_amount': 0, 'bank_transfer_amount': 0, 'gift_card_amount': 0, 'amount': 100},
]

def test_customers_no_order():
    result = run_model('orders', tables)
    assert assert_frame_equal(result, pd.DataFrame(orders)) == None