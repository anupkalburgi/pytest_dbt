import pandas as pd
from pytest_dbt.pytest_dbt import run_model
from pandas.testing import assert_frame_equal
from test_customers import stg_customers


tables = {
    "stg_customers": stg_customers,
}

customer_details = [
    {"customer_id": 1, "full_name": "Alice Henderson"},
    {"customer_id": 2, "full_name": "Bob Doe"},
    {"customer_id": 3, "full_name": "Charlie Krick"},
    {"customer_id": 4, "full_name": "Dennis Smith"},
]


def full_name(fname, lastname):
    return fname + " " + lastname


udfs = {"full_name":full_name }


def test_customer_details():
    result = run_model("customer_details", tables=tables, udfs=udfs)
    assert assert_frame_equal(result, pd.DataFrame(customer_details)) == None
