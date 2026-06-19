SELECT 
    IF(from_id < to_id, from_id, to_id) person1,
    IF(from_id >= to_id, from_id, to_id) person2,
    COUNT(*) AS call_count,
    SUM(duration) AS total_duration
FROM Calls
GROUP BY 1, 2