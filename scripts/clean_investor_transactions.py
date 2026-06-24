import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Before Cleaning")
print(df.shape)

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.strip()
    .str.upper()
)

df["transaction_type"] = df["transaction_type"].replace({
    "SYSTEMATIC INVESTMENT PLAN": "SIP",
    "LUMP SUM": "LUMPSUM"
})

df = df[df["amount_inr"] > 0]

print("\nKYC Status Values:")
print(df["kyc_status"].unique())

print("\nAfter Cleaning")
print(df.shape)

df.to_csv(
    "data/processed/clean_investor_transactions.csv",
    index=False
)

print("\nFile Saved")