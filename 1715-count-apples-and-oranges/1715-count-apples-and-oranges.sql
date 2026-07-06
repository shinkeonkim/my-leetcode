# Write your MySQL query statement below
SELECT 
    SUM(COALESCE(Boxes.apple_count, 0) + COALESCE(Chests.apple_count, 0)) as apple_count,
    SUM(COALESCE(Boxes.orange_count, 0) + COALESCE(Chests.orange_count, 0)) as orange_count
FROM Boxes
LEFT JOIN Chests
ON Boxes.chest_id = Chests.chest_id
