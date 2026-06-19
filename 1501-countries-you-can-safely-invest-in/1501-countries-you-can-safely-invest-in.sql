WITH call_durations AS (
    SELECT person_id, duration
    FROM (
        SELECT caller_id as person_id, duration FROM Calls
        UNION ALL
        SELECT callee_id as person_id, duration FROM Calls
    ) temp
), country_call_durations AS (
    SELECT
        C.name as country,
        call_durations.duration
    FROM Country C
    JOIN Person P ON C.country_code = SUBSTR(P.phone_number, 1, 3)
    JOIN call_durations ON call_durations.person_id = P.id
)

SELECT country
FROM country_call_durations
GROUP BY country
HAVING AVG(duration) > (SELECT AVG(duration) FROM country_call_durations)