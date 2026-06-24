import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Before Cleaning")
print(df.shape)

df["date"] = pd.to_datetime(df["date"])

df = df.sort_values(
    by=["amfi_code", "date"]
)

df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

df = df.drop_duplicates()

df = df[df["nav"] > 0]

print("\nAfter Cleaning")
print(df.shape)

print("\nMissing Values")
print(df.isnull().sum())

df.to_csv(
    "data/processed/clean_nav_history.csv",
    index=False
)

print("\nFile Saved")