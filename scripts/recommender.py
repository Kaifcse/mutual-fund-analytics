import pandas as pd

performance = pd.read_csv("../data/raw/07_scheme_performance.csv")

risk = input("Enter Risk Appetite (Low / Moderate / High): ").strip().title()

result = (
    performance[
        performance["risk_grade"].str.contains(risk, case=False)
    ]
    .sort_values("sharpe_ratio", ascending=False)
    [
        [
            "scheme_name",
            "fund_house",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct",
            "expense_ratio_pct"
        ]
    ]
    .head(3)
)

print("\nTop 3 Recommended Funds\n")
print(result)

result.to_csv("../reports/fund_recommendations.csv", index=False)

print("\nRecommendation saved successfully.")