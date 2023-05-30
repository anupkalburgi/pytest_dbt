select customer_id
from {{ ref('customers') }}
where number_of_orders is null