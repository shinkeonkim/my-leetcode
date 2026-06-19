# Write your MySQL query statement below
WITH product AS (
    SELECT DISTINCT(product_id)
    FROM Products
), store1 AS (
    SELECT
        product_id,
        price as store1
    FROM Products
    WHERE store = 'store1'
),  store2 AS (
    SELECT
        product_id,
        price as store2
    FROM Products
    WHERE store = 'store2'
),  store3 AS (
    SELECT
        product_id,
        price as store3
    FROM Products
    WHERE store = 'store3'
)

SELECT 
    p.product_id,
    store1,
    store2,
    store3
FROM product p
LEFT OUTER JOIN store1 ON p.product_id = store1.product_id
LEFT OUTER JOIN store2 ON p.product_id = store2.product_id
LEFT OUTER JOIN store3 ON p.product_id = store3.product_id
