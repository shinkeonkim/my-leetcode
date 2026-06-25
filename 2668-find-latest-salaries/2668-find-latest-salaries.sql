# Write your MySQL query statement below
SELECT 
    emp_id, firstname, lastname, salary, department_id
FROM (
    SELECT 
        *,
        ROW_NUMBER() OVER (PARTITION BY emp_id ORDER BY salary DESC) as rn
    FROM 
        Salary
) t
WHERE rn = 1
ORDER BY emp_id;