import pandas as pd

files = {
    "01_fund_master.csv": "clean_fund_master.csv",
    "03_aum_by_fund_house.csv": "clean_aum_by_fund_house.csv",
    "05_category_inflows.csv": "clean_category_inflows.csv",
    "06_industry_folio_count.csv": "clean_industry_folio_count.csv",
    "09_portfolio_holdings.csv": "clean_portfolio_holdings.csv",
    "10_benchmark_indices.csv": "clean_benchmark_indices.csv"
}

for source, target in files.items():
    df = pd.read_csv(f"data/raw/{source}")

    df = df.drop_duplicates()

    df.to_csv(
        f"data/processed/{target}",
        index=False
    )

    print(f"{target} created")
