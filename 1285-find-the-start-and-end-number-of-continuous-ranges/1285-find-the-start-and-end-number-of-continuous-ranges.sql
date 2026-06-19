# Write your MySQL query statement below
WITH CTE as (
    SELECT
        log_id,
        log_id - RANK() OVER (ORDER BY log_id) as group_id
    FROM Logs
)

SELECT MIN(log_id) as start_id, MAX(log_id) as end_id
FROM CTE
GROUP BY group_id