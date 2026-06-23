# Write your MySQL query statement below
SELECT q.id, q.year, COALESCE(npv, 0) as npv
FROM Queries q
LEFT OUTER JOIN NPV n ON q.id = n.id AND q.year = n.year
ORDER BY q.id, q.year