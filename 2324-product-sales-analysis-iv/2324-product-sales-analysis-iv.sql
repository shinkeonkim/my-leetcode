# Write your MySQL query statement below
WITH cum_sales AS (
    SELECT product_id, user_id, SUM(quantity) as quantity
    FROM Sales
    GROUP BY product_id, user_id
)
SELECT user_id, product_id
FROM (
    SELECT
        user_id,
        cum_sales.product_id,
        RANK() OVER (PARTITION BY user_id ORDER BY price * quantity DESC) as rn
    FROM cum_sales 
    JOIN Product
    ON cum_sales.product_id = Product.product_id
) t
WHERE rn = 1;
