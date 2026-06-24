import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Before Cleaning")
print(df.shape)

returns_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in returns_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

expense_anomalies = df[
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
]

print("\nExpense Ratio Anomalies:")
print(expense_anomalies.shape)

print("\nMissing Values:")
print(df.isnull().sum())

df.to_csv(
    "data/processed/clean_scheme_performance.csv",
    index=False
)

print("\nFile Saved")