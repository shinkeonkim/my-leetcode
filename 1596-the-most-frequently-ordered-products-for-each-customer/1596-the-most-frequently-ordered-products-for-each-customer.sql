# Write your MySQL query statement below
WITH order_counts AS (
    SELECT customer_id, product_id, COUNT(*) as cnt
    FROM Orders
    GROUP BY customer_id, product_id
)

SELECT customer_id, a.product_id, product_name
FROM (
    SELECT customer_id, product_id, DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY cnt DESC) as rn
    FROM order_counts
) a
JOIN Products p ON p.product_id = a.product_id
WHERE rn = 1 
