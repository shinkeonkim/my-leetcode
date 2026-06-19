# Write your MySQL query statement below
WITH CTE as (
    SELECT date, state 
    FROM (
        SELECT fail_date as date, 'failed' as state FROM Failed
        UNION ALL
        SELECT success_date as date, 'succeeded' as state FROM Succeeded
    ) a
    WHERE a.date BETWEEN '2019-01-01' AND '2019-12-31'
)

SELECT 
    state AS period_state, 
    MIN(date) AS start_date,
    MAX(date) AS end_date
FROM (
    SELECT 
        date,
        state,
        ROW_NUMBER() OVER (PARTITION BY state ORDER BY date) as rn
    FROM CTE
) a
GROUP BY period_state, DATE_SUB(date, INTERVAL rn DAY)
ORDER BY start_date
