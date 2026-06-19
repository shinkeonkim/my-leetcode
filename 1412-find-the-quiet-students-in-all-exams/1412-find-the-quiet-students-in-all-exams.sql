# Write your MySQL query statement below
WITH CTE AS (
    SELECT 
        student_id,
        DENSE_RANK() OVER (PARTITION BY exam_id ORDER BY score) as rn1,
        DENSE_RANK() OVER (PARTITION BY exam_id ORDER BY score DESC) as rn2
    FROM Exam
)
SELECT student_id, student_name
FROM Student
WHERE student_id NOT IN (SELECT student_id FROM CTE WHERE rn1 = 1 OR rn2 = 1)
    AND student_id IN (SELECT DISTINCT(student_id) FROM Exam)