# 1. import the proccessed dataset of wgi rq

import pandas as pd

df = pd.read_csv(
    "data/processed/asean_wgi_regulatory_quality_1996_2024.csv"
)

# 2. Display basic information

print("--- DATASET LOADED ---")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\n--- DATASET PREVIEW ---")
print(df.head())

# 3. Confidence interval validation

print("\n--- CONFIDENCE INTERVAL VALIDATION ---")

# 3a. Check whether lower bounds exceed upper bounds
invalid_bounds = df[
    df["RQ Score Lower Bound"] >
    df["RQ Score Upper Bound"]
]

print("Invalid confidence intervals:", len(invalid_bounds))

# 3b. Check whether scores fall outside their confidence intervals
outside_bounds = df[
    (df["RQ Score"] < df["RQ Score Lower Bound"]) |
    (df["RQ Score"] > df["RQ Score Upper Bound"])
]

print("Scores outside confidence intervals:", len(outside_bounds))