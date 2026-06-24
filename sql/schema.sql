CREATE TABLE dim_fund(
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    fund_manager TEXT
);

CREATE TABLE dim_date(
    date_id INTEGER PRIMARY KEY,
    full_date DATE,
    year INTEGER,
    quarter INTEGER,
    month INTEGER,
    month_name TEXT
);

CREATE TABLE fact_nav(
    amfi_code INTEGER,
    date_id INTEGER,
    nav REAL,
    PRIMARY KEY(amfi_code,date_id),
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_transactions(
    investor_id TEXT,
    amfi_code INTEGER,
    date_id INTEGER,
    amount_inr REAL,
    transaction_type TEXT,
    PRIMARY KEY(investor_id,amfi_code,date_id),
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code),
    FOREIGN KEY(date_id) REFERENCES dim_date(date_id)
);

CREATE TABLE fact_performance(
    amfi_code INTEGER PRIMARY KEY,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    expense_ratio_pct REAL,
    sharpe_ratio REAL,
    alpha REAL,
    beta REAL,
    FOREIGN KEY(amfi_code) REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_aum(
    fund_house TEXT,
    date_id INTEGER,
    aum_crore REAL,
    PRIMARY KEY(fund_house,date_id),
    FOREIGN KEY(date_id) REFERENCES dim_date(date_id)
);