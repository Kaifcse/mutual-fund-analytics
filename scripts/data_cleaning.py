import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):

        df = pd.read_csv(os.path.join(folder, file))

        print("\n" + "="*60)
        print(file)

        print("\nShape:")
        print(df.shape)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())