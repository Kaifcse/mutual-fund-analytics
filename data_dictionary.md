# Mutual Fund Analytics Data Dictionary

## Source
Bluestock Capstone Project – Mutual Fund Analytics

---

# 01_fund_master.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique AMFI scheme identifier |
| fund_house | Text | Mutual fund company |
| scheme_name | Text | Scheme name |
| category | Text | Fund category |
| sub_category | Text | Fund sub-category |
| plan | Text | Direct or Regular plan |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Expense ratio percentage |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Integer | Minimum SIP investment amount |
| min_lumpsum_amount | Integer | Minimum lump sum investment |
| fund_manager | Text | Fund manager name |
| risk_category | Text | Risk classification |
| sebi_category_code | Text | SEBI category code |

---

# 02_nav_history.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Scheme AMFI code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

---

# 03_aum_by_fund_house.csv

| Column | Data Type | Description |
|----------|----------|----------|
| date | Date | Reporting date |
| fund_house | Text | Mutual fund company |
| aum_lakh_crore | Float | Assets under management in lakh crore |
| aum_crore | Float | Assets under management in crore |
| num_schemes | Integer | Number of schemes managed |

---

# 04_monthly_sip_inflows.csv

| Column | Data Type | Description |
|----------|----------|----------|
| month | Date | Reporting month |
| sip_inflow_crore | Float | SIP inflow amount in crore |
| active_sip_accounts_crore | Float | Active SIP accounts in crore |
| new_sip_accounts_lakh | Float | Newly registered SIP accounts |
| sip_aum_lakh_crore | Float | SIP assets under management |
| yoy_growth_pct | Float | Year-over-year growth percentage |

---

# 05_category_inflows.csv

| Column | Data Type | Description |
|----------|----------|----------|
| month | Date | Reporting month |
| category | Text | Mutual fund category |
| net_inflow_crore | Float | Net inflow amount in crore |

---

# 06_industry_folio_count.csv

| Column | Data Type | Description |
|----------|----------|----------|
| month | Date | Reporting month |
| total_folios_crore | Float | Total investor folios |
| equity_folios_crore | Float | Equity fund folios |
| debt_folios_crore | Float | Debt fund folios |
| hybrid_folios_crore | Float | Hybrid fund folios |
| others_folios_crore | Float | Other category folios |

---

# 07_scheme_performance.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Scheme AMFI code |
| scheme_name | Text | Scheme name |
| fund_house | Text | Mutual fund company |
| category | Text | Fund category |
| plan | Text | Direct or Regular plan |
| return_1yr_pct | Float | 1-year return percentage |
| return_3yr_pct | Float | 3-year return percentage |
| return_5yr_pct | Float | 5-year return percentage |
| benchmark_3yr_pct | Float | Benchmark return percentage |
| alpha | Float | Alpha metric |
| beta | Float | Beta metric |
| sharpe_ratio | Float | Sharpe ratio |
| sortino_ratio | Float | Sortino ratio |
| std_dev_ann_pct | Float | Annualized standard deviation |
| max_drawdown_pct | Float | Maximum drawdown |
| aum_crore | Float | Assets under management |
| expense_ratio_pct | Float | Expense ratio |
| morningstar_rating | Integer | Morningstar rating |
| risk_grade | Text | Risk grade |

---

# 08_investor_transactions.csv

| Column | Data Type | Description |
|----------|----------|----------|
| investor_id | Text | Unique investor identifier |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Scheme AMFI code |
| transaction_type | Text | SIP, Lumpsum, Redemption |
| amount_inr | Float | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | City classification |
| age_group | Text | Investor age group |
| gender | Text | Investor gender |
| annual_income_lakh | Float | Annual income in lakh |
| payment_mode | Text | Payment method |
| kyc_status | Text | KYC verification status |

---

# 09_portfolio_holdings.csv

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Scheme AMFI code |
| stock_symbol | Text | Stock ticker symbol |
| stock_name | Text | Company name |
| sector | Text | Industry sector |
| weight_pct | Float | Portfolio allocation percentage |
| market_value_cr | Float | Market value in crore |
| current_price_inr | Float | Current stock price |
| portfolio_date | Date | Portfolio reporting date |

---

# 10_benchmark_indices.csv

| Column | Data Type | Description |
|----------|----------|----------|
| date | Date | Trading date |
| index_name | Text | Benchmark index name |
| close_value | Float | Closing index value |

---

# Data Quality Notes

1. All datasets successfully loaded.
2. No duplicate records found.
3. AMFI code validation passed.
4. NAV values validated (> 0).
5. Investor transaction amounts validated (> 0).
6. Expense ratio validation passed (0.1%–2.5%).
7. SIP dataset missing values cleaned successfully.
8. SQLite database loaded successfully.
