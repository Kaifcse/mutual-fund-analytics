import pandas as pd

df = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

print("Missing Values Before:")
print(df.isnull().sum())

df["yoy_growth_pct"] = df["yoy_growth_pct"].fillna(0)

print("\nMissing Values After:")
print(df.isnull().sum())

df.to_csv(
    "data/processed/clean_monthly_sip_inflows.csv",
    index=False
)

print("\nFile Saved Successfully")