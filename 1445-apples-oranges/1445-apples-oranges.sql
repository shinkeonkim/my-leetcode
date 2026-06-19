SELECT
    sale_date,
    MAX(IF(fruit = 'apples', sold_num, NULL)) - MAX(IF(fruit = 'oranges', sold_num, NULL)) as diff
FROM Sales
GROUP BY sale_date