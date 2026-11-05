import pandas as pd

# 1. Read the original raw dataset
raw_df = pd.read_csv("data/raw/wgi_regulatory_quality.csv")

print("\n--- TIMOR-LESTE RAW OBSERVATIONS (1996–2001) ---")

print(
    raw_df[
        (raw_df["Country Code"] == "TLS") &
        (raw_df["Year"].between(1996, 2001))
    ].to_string(index=False)
)

# 2. Reshape the data: one row per country-year,
# with six separate indicator columns
wide_df = raw_df.pivot(
    index=["Country", "Country Code", "Year"],
    columns="Indicator Code",
    values="Value"
).reset_index()

wide_df.columns.name = None

# 3. Rename the indicator columns for readability
wide_df = wide_df.rename(columns={
    "GOV_WGI_RQ.EST": "RQ Estimate",
    "GOV_WGI_RQ.SC": "RQ Score",
    "GOV_WGI_RQ.SC_LB": "RQ Score Lower Bound",
    "GOV_WGI_RQ.SC_UB": "RQ Score Upper Bound",
    "GOV_WGI_RQ.SE": "RQ Standard Error",
    "GOV_WGI_RQ.SR": "RQ Number of Sources"
})

# 4. Create a complete country-year panel
countries = {
    "Brunei Darussalam": "BRN",
    "Cambodia": "KHM",
    "Indonesia": "IDN",
    "Lao PDR": "LAO",
    "Malaysia": "MYS",
    "Myanmar": "MMR",
    "Philippines": "PHL",
    "Singapore": "SGP",
    "Thailand": "THA",
    "Timor-Leste": "TLS",
    "Vietnam": "VNM"
}

panel = pd.DataFrame([
    {
        "Country": country,
        "Country Code": country_code,
        "Year": year
    }
    for country, country_code in countries.items()
    for year in range(1996, 2025)
])

# 5. Merge the observations into the complete panel
final_df = panel.merge(
    wide_df,
    on=["Country", "Country Code", "Year"],
    how="left"
)

# 7. Investigate missing observations
indicator_columns = [
    "RQ Estimate",
    "RQ Score",
    "RQ Score Lower Bound",
    "RQ Score Upper Bound",
    "RQ Standard Error",
    "RQ Number of Sources"
]

missing_rows = final_df[
    final_df[indicator_columns].isna().any(axis=1)
]

print("\n--- COUNTRY-YEARS WITH MISSING OBSERVATIONS ---")
print(missing_rows.to_string(index=False))

print("\n--- MISSING VALUES BY COUNTRY ---")
print(
    final_df.groupby("Country")[indicator_columns]
    .apply(lambda group: group.isna().sum())
)

# 6. Inspect the resulting dataset
print("\n--- DATASET OVERVIEW ---")
print("Rows:", len(final_df))
print("Columns:", len(final_df.columns))

print("\n--- MISSING VALUES ---")
print(final_df.isna().sum())

print("\n--- FIRST FIVE ROWS ---")
print(final_df.head())

print("\n--- LAST FIVE ROWS ---")
print(final_df.tail())

# 8. Final structural validation

print("\n--- FINAL VALIDATION ---")

print("Expected rows:", 11 * 29)
print("Actual rows:", len(final_df))

print("Duplicate country-years:",
      final_df.duplicated(
          subset=["Country Code", "Year"]
      ).sum())

print("Countries:", final_df["Country Code"].nunique())

print("Year range:",
      final_df["Year"].min(),
      "-",
      final_df["Year"].max())

print("Missing values per indicator:")
print(final_df[indicator_columns].isna().sum())

# 9. Save the processed dataset

output_path = "data/processed/asean_wgi_regulatory_quality_1996_2024.csv"

final_df.to_csv(output_path, index=False)

print("\nProcessed dataset saved successfully!")
print("Location:", output_path)