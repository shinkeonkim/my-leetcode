SELECT user_id, MAX(time_stamp) as last_stamp
FROM (
    SELECT *
    FROM Logins
    WHERE YEAR(time_stamp) = 2020
) a
GROUP BY user_id
