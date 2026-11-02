-- Write your query below
SELECT employee_id,
case
    when employee_id % 2 != 0 AND LEFT(name,1) != 'M' THEN salary
    else 0
end as bonus 
from employees
order by employee_id