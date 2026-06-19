SELECT 
    ROUND(100 * AVG(IF(order_date=customer_pref_delivery_date, 1, 0)), 2) as immediate_percentage
FROM Delivery