# Write your MySQL query statement below
WITH team_sizes AS (
    SELECT team_id, COUNT(*) as team_size
    FROM Employee
    GROUP BY team_id
)
SELECT employee_id, team_size
FROM Employee
JOIN team_sizes
ON team_sizes.team_id = Employee.team_id