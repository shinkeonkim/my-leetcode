SELECT name, COALESCE(SUM(distance), 0) as travelled_distance
FROM Users
LEFT OUTER JOIN Rides ON Users.id = Rides.user_id
GROUP BY user_id
ORDER BY 2 DESC, 1 ASC