-- Write your query below
SELECT name from customers
where id not in (select customer_id from customers
join orders on customers.id = orders.customer_id
)