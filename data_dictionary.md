# Mutual Fund Analytics Data Dictionary

## this is for 1 st data set datasets.

| Column | Data Type | Description |
|----------|----------|----------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Mutual fund company |
| scheme_name | Text | Name of scheme |
| category | Text | Fund category |
| sub_category | Text | Fund sub-category |
| plan | Text | Direct or Regular |
| launch_date | Date | Scheme launch date |
| benchmark | Text | Benchmark index |
| expense_ratio_pct | Float | Expense ratio percentage |
| exit_load_pct | Float | Exit load percentage |
| min_sip_amount | Integer | Minimum SIP amount |
| min_lumpsum_amount | Integer | Minimum lump sum investment |
| fund_manager | Text | Fund manager |
| risk_category | Text | Risk category |
| sebi_category_code | Text | SEBI classification code |

## for 2nd data set (02_nav_history.csv)
Column,Data Type,Description
amfi_code,Integer,Unique identifier for the fund
scheme_name,Text,Full name of the mutual fund scheme
fund_house,Text,The Asset Management Company (AMC)
category,Text,"SEBI-defined category (e.g., Large Cap)"
sub_category,Text,Specific sub-classification
plan,Text,"Growth/Dividend, Direct/Regular"
...,...,...