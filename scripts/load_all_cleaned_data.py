import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

datasets = {
    "clean_nav_history":
        "data/processed/clean_nav_history.csv",

    "clean_investor_transactions":
        "data/processed/clean_investor_transactions.csv",

    "clean_scheme_performance":
        "data/processed/clean_scheme_performance.csv",

    "clean_monthly_sip_inflows":
        "data/processed/clean_monthly_sip_inflows.csv"
}

for table_name, file_path in datasets.items():

    df = pd.read_csv(file_path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(
        f"{table_name}: {len(df)} rows loaded"
    )

print("\nAll cleaned datasets loaded successfully")