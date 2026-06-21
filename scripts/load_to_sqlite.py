import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")
transactions = pd.read_csv("data/raw/08_investor_transactions.csv")
performance = pd.read_csv("data/raw/07_scheme_performance.csv")

fund_master.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav_history.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Database Loaded Successfully")