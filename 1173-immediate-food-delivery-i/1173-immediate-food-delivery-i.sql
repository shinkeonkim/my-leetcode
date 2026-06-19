SELECT 
    ROUND(100 * SUM(IF(order_date=customer_pref_delivery_date, 1, 0)) / COUNT(order_date), 2) as immediate_percentage
FROM Delivery