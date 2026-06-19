WITH red_orders AS (
    SELECT sales_id
    FROM Orders
    WHERE com_id = (
        SELECT MIN(com_id) 
        FROM Company
        WHERE name = 'RED'
    )
)
SELECT name FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id FROM red_orders
)