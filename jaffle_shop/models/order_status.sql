
select status, customer_id, count(*)
from {{ref("stg_orders")}}
group by 1, 2
order by 2