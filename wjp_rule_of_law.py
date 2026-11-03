import pandas as pd

# 1. Load the historical WJP dataset
file_path = "data/raw/wjp_historical.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Historical Data",
    header=1
)

# 2. Inspect the dataset
print("--- ORIGINAL DATASET ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n--- FIRST FIVE ROWS ---")
print(df.head())

print("\n--- COLUMN NAMES ---")
for column in df.columns:
    print(column)

# 3. Select indicators for Rule of Law analysis

selected_columns = [
    # Metadata
    "Country",
    "Year",
    "Country Code",
    "Region",

    # Group 1: Civil Justice
    "Factor 7: Civil Justice",
    "7.1 People can access and afford civil justice",
    "7.2 Civil justice is free of discrimination",
    "7.3 Civil justice is free of corruption",
    "7.4 Civil justice is free of improper government influence",
    "7.5 Civil justice is not subject to unreasonable delay",
    "7.6. Civil justice is effectively enforced",
    "7.7 Alternative dispute resolution mechanisms are accessible, impartial, and effective",

    # Group 2: Criminal Justice
    "Factor 8: Criminal Justice",
    "8.1 Criminal investigation system is effective",
    "8.2 Criminal adjudication system is timely and effective",
    "8.3 Correctional system is effective in reducing criminal behavior",
    "8.4 Criminal system is impartial",
    "8.5 Criminal system is free of corruption",
    "8.6 Criminal system is free of improper government influence",
    "8.7. Due process of the law and rights of the accused",

    # Group 3: Judicial checks and public security
    "1.2 Government powers are effectively limited by the judiciary",
    "5.1 Crime is effectively controlled",
    "5.2 Civil conflict is effectively limited"
]

# 4. Create a new DataFrame containing only selected columns
rule_of_law_df = df[selected_columns].copy()

# 5. Inspect the selected dataset
print("\n--- SELECTED RULE OF LAW DATASET ---")
print("Rows:", rule_of_law_df.shape[0])
print("Columns:", rule_of_law_df.shape[1])

print("\n--- SELECTED COLUMN NAMES ---")
print(rule_of_law_df.columns.tolist())

# 6. Define ASEAN countries available in WJP

asean_wjp_codes = [
    "BRN",  # Brunei Darussalam
    "KHM",  # Cambodia
    "IDN",  # Indonesia
    "LAO",  # Lao PDR
    "MYS",  # Malaysia
    "MMR",  # Myanmar
    "PHL",  # Philippines
    "SGP",  # Singapore
    "THA",  # Thailand
    "TLS",  # Timor-Leste
    "VNM"   # Vietnam
]

# 7. Filter the dataset
asean_rule_of_law_df = rule_of_law_df[
    rule_of_law_df["Country Code"].isin(asean_wjp_codes)
].copy()

# 8. Inspect country coverage
print("\n--- ASEAN COUNTRIES IN WJP DATASET ---")

print(
    asean_rule_of_law_df[
        ["Country", "Country Code"]
    ].drop_duplicates().sort_values("Country")
)

print("\nNumber of countries:", 
      asean_rule_of_law_df["Country Code"].nunique())

print("Number of observations:", 
      len(asean_rule_of_law_df))

# 9. Define the observation periods for our research

selected_periods = [
    "2012-2013",
    "2014",
    "2015",
    "2016",
    "2017-2018",
    "2019",
    "2020",
    "2021",
    "2022",
    "2023",
    "2024"
]

# 10. Convert Year values to strings
asean_rule_of_law_df["Year"] = (
    asean_rule_of_law_df["Year"].astype(str)
)

# 11. Filter the selected periods
asean_rule_of_law_df = asean_rule_of_law_df[
    asean_rule_of_law_df["Year"].isin(selected_periods)
].copy()

# 12. Inspect the filtered dataset
print("\n--- WJP RULE OF LAW: 2012–2024 ---")

print("Countries:",
      asean_rule_of_law_df["Country Code"].nunique())

print("Observations:",
      len(asean_rule_of_law_df))

print("\n--- PERIOD DISTRIBUTION ---")
print(
    asean_rule_of_law_df["Year"]
    .value_counts()
    .reindex(selected_periods)
)

print("\n--- COUNTRY DISTRIBUTION ---")
print(
    asean_rule_of_law_df.groupby("Country")["Year"]
    .count()
    .sort_index()
)

# 13. Check missing values in selected indicators

metadata_columns = [
    "Country",
    "Year",
    "Country Code",
    "Region"
]

indicator_columns = [
    column
    for column in asean_rule_of_law_df.columns
    if column not in metadata_columns
]

# Count missing values for each indicator
missing_summary = (
    asean_rule_of_law_df[indicator_columns]
    .isna()
    .sum()
    .sort_values(ascending=False)
)

print("\n--- MISSING VALUES BY INDICATOR ---")
print(missing_summary)

print("\n--- TOTAL MISSING VALUES ---")
print("Missing cells:", missing_summary.sum())

print("\n--- AVAILABLE SCORES ---")
print(
    "Total possible scores:",
    len(asean_rule_of_law_df) * len(indicator_columns)
)

print(
    "Available scores:",
    asean_rule_of_law_df[indicator_columns].notna().sum().sum()
)

# Display observations with at least one missing indicator
print("\n--- OBSERVATIONS WITH MISSING SCORES ---")

print(
    asean_rule_of_law_df[
        asean_rule_of_law_df[indicator_columns].isna().any(axis=1)
    ][["Country", "Year", "Country Code"] + indicator_columns]
)