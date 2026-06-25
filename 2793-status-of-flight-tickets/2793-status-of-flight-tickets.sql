# Write your MySQL query statement below
SELECT 
    passenger_id,
    (CASE WHEN rn <= capacity THEN 'Confirmed' ELSE 'Waitlist' END) as Status
FROM (
    SELECT 
        passenger_id,
        capacity,
        ROW_NUMBER() OVER (PARTITION BY p.flight_id ORDER BY booking_time) as rn
    FROM Passengers p
    JOIN Flights f
    ON p.flight_id = f.flight_id
) a
ORDER BY passenger_id
