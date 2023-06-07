import pandas as pd
from pytest_dbt.pytest_dbt import run_model
from pandas.testing import assert_frame_equal

stg_customers = [
    {"customer_id": 1, "first_name": "Alice", "last_name": "Henderson"},
    {"customer_id": 2, "first_name": "Bob", "last_name": "Doe"},
    {"customer_id": 3, "first_name": "Charlie", "last_name": "Krick"},
    {"customer_id": 4, "first_name": "Dennis", "last_name": "Smith"},
]
stg_orders = [
    {"order_id": 1, "customer_id": 1, "order_date": "2020-01-01", "status": "returned"},
    {
        "order_id": 2,
        "customer_id": 1,
        "order_date": "2020-01-02",
        "status": "completed",
    },
    {
        "order_id": 3,
        "customer_id": 2,
        "order_date": "2020-01-01",
        "status": "completed",
    },
    {
        "order_id": 4,
        "customer_id": 2,
        "order_date": "2020-01-04",
        "status": "completed",
    },
    {
        "order_id": 5,
        "customer_id": 3,
        "order_date": "2020-01-05",
        "status": "completed",
    },
]

stg_payments = [
    {"payment_id": 1, "order_id": 1, "payment_method": "card", "amount": 10},
    {"payment_id": 2, "order_id": 2, "payment_method": "card", "amount": 190},
    {"payment_id": 3, "order_id": 3, "payment_method": "card", "amount": 50},
    {"payment_id": 4, "order_id": 4, "payment_method": "card", "amount": 250},
    {"payment_id": 5, "order_id": 5, "payment_method": "card", "amount": 100},
]

# expected output
customers = [
    {
        "customer_id": 1,
        "first_name": "Alice",
        "last_name": "Henderson",
        "first_order": "2020-01-01",
        "most_recent_order": "2020-01-02",
        "number_of_orders": 2,
        "customer_lifetime_value": 200,
    },
    {
        "customer_id": 2,
        "first_name": "Bob",
        "last_name": "Doe",
        "first_order": "2020-01-01",
        "most_recent_order": "2020-01-04",
        "number_of_orders": 2,
        "customer_lifetime_value": 300,
    },
    {
        "customer_id": 3,
        "first_name": "Charlie",
        "last_name": "Krick",
        "first_order": "2020-01-05",
        "most_recent_order": "2020-01-05",
        "number_of_orders": 1,
        "customer_lifetime_value": 100,
    },
    {
        "customer_id": 4,
        "first_name": "Dennis",
        "last_name": "Smith",
        "first_order": None,
        "most_recent_order": None,
        "number_of_orders": None,
        "customer_lifetime_value": None,
    },
]

tables = {
    "stg_customers": stg_customers,
    "stg_orders": stg_orders,
    "stg_payments": stg_payments,
}


def test_customers():
    result = run_model("customers", tables)
    assert assert_frame_equal(result, pd.DataFrame(customers)) == None
