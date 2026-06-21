-- Top 5 Funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average 3 Year Return
SELECT AVG(return_3yr_pct)
FROM fact_performance;

-- Total Transactions
SELECT COUNT(*)
FROM fact_transactions;

-- Total Investment Amount
SELECT SUM(amount_inr)
FROM fact_transactions;

-- Top 10 States by Investment
SELECT state,
       SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC
LIMIT 10;