# def fixture_model():
#     return "Sample model"

# def fixture_stg_customers():
#     return [
#         {'customer_id': 1, 'first_name': 'Alice', 'last_name': 'Henderson'},
#         {'customer_id': 2, 'first_name': 'Bob', 'last_name': 'Doe'},
#         {'customer_id': 3, 'first_name': 'Charlie', 'last_name': 'Krick'},
#         {'customer_id': 4, 'first_name': 'Dennis', 'last_name': 'Smith'},
#     ]

# def fixture_stg_orders():
#     return [
#         {'order_id': 1, 'customer_id': 1, 'order_date': '2020-01-01', 'status': 'returned'},
#         {'order_id': 2, 'customer_id': 1, 'order_date': '2020-01-02', 'status': 'completed'}    ,
#         {'order_id': 3, 'customer_id': 2, 'order_date': '2020-01-01', 'status': 'completed'},
#         {'order_id': 4, 'customer_id': 2, 'order_date': '2020-01-04', 'status': 'completed'},
#         {'order_id': 5, 'customer_id': 3, 'order_date': '2020-01-05', 'status': 'completed'},
#     ]

# def fixture_stg_payments():
#     return [
#         {'payment_id': 1, 'order_id': 1, 'payment_method': 'card', 'amount': 100},
#         {'payment_id': 2, 'order_id': 2, 'payment_method': 'card', 'amount': 100},
#         {'payment_id': 3, 'order_id': 3, 'payment_method': 'card', 'amount': 100},
#         {'payment_id': 4, 'order_id': 4, 'payment_method': 'card', 'amount': 100},
#         {'payment_id': 5, 'order_id': 5, 'payment_method': 'card', 'amount': 100},
#     ]


# def test_customers(stg_customers, stg_orders, stg_payments):
#     model = fixture_model() # path to the model file
#     tables = {
#         'stg_customers':stg_customers,
#         'stg_orders':stg_orders ,
#         'stg_payments': stg_payments,
#     }
#     expected_output = "Expected output"
#     assert model == "Sample model"
#     assert tables == ["table1", "table2"]
#     assert expected_output == "Expected output"
