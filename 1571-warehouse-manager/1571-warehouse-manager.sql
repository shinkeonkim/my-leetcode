SELECT Warehouse.name as warehouse_name, SUM(Width * Length * Height * units) as volume
FROM Warehouse
LEFT JOIN Products ON Warehouse.product_id = Products.product_id
GROUP BY 1