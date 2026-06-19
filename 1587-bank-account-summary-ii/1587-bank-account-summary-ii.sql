WITH accounts as (
    SELECT 
        account,
        SUM(amount) as balance
    FROM Transactions
    GROUP BY account
)
SELECT name, balance
FROM Users
JOIN accounts 
ON accounts.account = Users.account
WHERE balance > 10000