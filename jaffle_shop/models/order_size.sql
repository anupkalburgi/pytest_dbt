select order_id,
case
	when amount <= 20 then 'small'
    when amount > 20 and amount <= 50 then 'medium'
    when amount > 50 then 'large'
end as order_size
from {{ ref("orders")}}