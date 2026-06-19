# Write your MySQL query statement below

SELECT DISTINCT(title)
FROM TVProgram p
JOIN Content c ON p.content_id = c.content_id
WHERE YEAR(program_date) = 2020
    AND MONTH(program_date) = 6
    AND Kids_content = 'Y'
    AND content_type = 'Movies'
