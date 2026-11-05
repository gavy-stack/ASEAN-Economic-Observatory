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

# 4. Standard error validation
# To establish that:
# - No standard error is negative.
# - Every available RQ Estimate has a corresponding standard error.
# - Every available standard error has a corresponding RQ Estimate.
# (damn chatgpt is smart)

print("\n--- STANDARD ERROR VALIDATION ---")

# 4a. Check for negative standard errors
negative_se = df[df["RQ Standard Error"] < 0]

print("Negative standard errors:", len(negative_se))

# 4b. Check for estimates without standard errors
missing_se = df[
    df["RQ Estimate"].notna() &
    df["RQ Standard Error"].isna()
]

print("Estimates without standard errors:", len(missing_se))

# 4c. Check for standard errors without estimates
missing_estimate = df[
    df["RQ Standard Error"].notna() &
    df["RQ Estimate"].isna()
]

print("Standard errors without estimates:", len(missing_estimate))

# 5. Number of sources validation

print("\n--- NUMBER OF SOURCES VALIDATION ---")

# 5a. Check for negative source counts
negative_sources = df[df["RQ Number of Sources"] < 0]

print("Negative source counts:", len(negative_sources))

# 5b. Check for zero source counts
zero_sources = df[df["RQ Number of Sources"] == 0]

print("Zero source counts:", len(zero_sources))

# 5c. Check for estimates without source counts
missing_sources = df[
    df["RQ Estimate"].notna() &
    df["RQ Number of Sources"].isna()
]

print("Estimates without source counts:", len(missing_sources))

# 5d. Check for source counts without estimates
missing_estimates = df[
    df["RQ Number of Sources"].notna() &
    df["RQ Estimate"].isna()
]

print("Source counts without estimates:", len(missing_estimates))

# Missing-data consistency validation

print("\n--- MISSING-DATA CONSISTENCY VALIDATION ---")

indicator_columns = [
    "RQ Estimate",
    "RQ Score",
    "RQ Score Lower Bound",
    "RQ Score Upper Bound",
    "RQ Standard Error",
    "RQ Number of Sources"
]

# 6. Check whether all six indicators have identical missing patterns
missing_patterns = df[indicator_columns].isna()

consistent_missingness = (
    missing_patterns.nunique(axis=1) == 1
)

print(
    "Country-years with consistent missingness:",
    consistent_missingness.sum()
)

print(
    "Country-years with inconsistent missingness:",
    (~consistent_missingness).sum()
)

# Count country-years where all six indicators are missing
fully_missing = missing_patterns.all(axis=1)

print(
    "Country-years with all six indicators missing:",
    fully_missing.sum()
)