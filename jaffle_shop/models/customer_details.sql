select customer_id, full_name(first_name, last_name) as full_name
from {{ ref('stg_customers') }}