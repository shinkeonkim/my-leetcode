# Write your MySQL query statement below
WITH RECURSIVE gen AS (
    SELECT task_id, subtasks_count, 1 AS subtask_id
    FROM Tasks
    UNION ALL
    SELECT task_id, subtasks_count, subtask_id + 1 AS subtask_id
    FROM gen
    WHERE subtask_id < subtasks_count
)

SELECT g.task_id, g.subtask_id
FROM  Executed e
RIGHT JOIN gen g 
ON e.subtask_id = g.subtask_id AND e.task_id = g.task_id
WHERE e.subtask_id IS NULL