# Write your MySQL query statement below
WITH CTE AS (
    SELECT
        o.customer_id,
        o.product_id,
        product_name,
        RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(*) DESC) as r
    FROM Customers c
    JOIN Orders o ON c.customer_id=o.customer_id
    JOIN products p ON o.product_id=p.product_id
    GROUP BY o.customer_id, o.product_id
)
SELECT  customer_id, product_id, product_name
FROM CTE
WHERE r = 1