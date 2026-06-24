-- Top 5 Funds by AUM
/*SELECT scheme_name, aum_crore
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
LIMIT 10;*/

-- 1. Top 5 Funds by AUM
SELECT scheme_name,aum_crore
FROM clean_scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav)
FROM clean_nav_history;

-- 3. Average 3 Year Return
SELECT AVG(return_3yr_pct)
FROM clean_scheme_performance;

-- 4. Total Transactions
SELECT COUNT(*)
FROM clean_investor_transactions;

-- 5. Total Investment Amount
SELECT SUM(amount_inr)
FROM clean_investor_transactions;

-- 6. Transactions by State
SELECT state,
       COUNT(*) AS total_transactions
FROM clean_investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 7. Funds with Expense Ratio < 1%
SELECT scheme_name,
       expense_ratio_pct
FROM clean_scheme_performance
WHERE expense_ratio_pct < 1;

-- 8. Highest Return Funds
SELECT scheme_name,
       return_5yr_pct
FROM clean_scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 9. Fund House Wise Count
SELECT fund_house,
       COUNT(*) AS total_funds
FROM clean_scheme_performance
GROUP BY fund_house
ORDER BY total_funds DESC;

-- 10. Risk Grade Distribution
SELECT risk_grade,
       COUNT(*) AS total_funds
FROM clean_scheme_performance
GROUP BY risk_grade;