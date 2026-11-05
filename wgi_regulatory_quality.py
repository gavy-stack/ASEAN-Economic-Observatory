
import requests
import pandas as pd

# WGI dictionaries for country codes
countries = {
    "BRN": "Brunei Darussalam",
    "KHM": "Cambodia",
    "IDN": "Indonesia",
    "LAO": "Lao PDR",
    "MYS": "Malaysia",
    "MMR": "Myanmar",
    "PHL": "Philippines",
    "SGP": "Singapore",
    "THA": "Thailand",
    "TLS": "Timor-Leste",
    "VNM": "Vietnam"
}

# WGI Regulatory Quality indicators
indicators = {
    "RQ Estimate": "GOV_WGI_RQ.EST",
    "RQ Score": "GOV_WGI_RQ.SC",
    "RQ Score Lower Bound": "GOV_WGI_RQ.SC_LB",
    "RQ Score Upper Bound": "GOV_WGI_RQ.SC_UB",
    "RQ Standard Error": "GOV_WGI_RQ.SE",
    "RQ Number of Sources": "GOV_WGI_RQ.SR"
}

year_sets = {}
all_data = []

for country_code, country_name in countries.items():

    print(f"\nCollecting data for {country_name}...")

    for name, indicator_code in indicators.items():

        url = (
            f"https://api.worldbank.org/v2/country/{country_code}/"
            f"indicator/{indicator_code}"
        )

        params = {
            "date": "1996:2024",
            "format": "json",
            "per_page": 100,
            "source": 3
        }

        response = requests.get(url, params=params, timeout=30)
        response.raise_for_status()

        data = response.json()

        if len(data) < 2 or not isinstance(data[1], list):
            print(f"API ERROR: {country_name} - {name}")
            continue

        for item in data[1]:

            observation = {
                "Country": country_name,
                "Country Code": country_code,
                "Year": int(item["date"]),
                name: item["value"]
            }

            all_data.append(observation)

print("\nData collection completed!")
print("Total observations collected:", len(all_data))

df = pd.DataFrame(all_data)

# Combine indicators belonging to the same country and year
df_final = (
    df.groupby(["Country", "Country Code", "Year"])
    .first()
    .reset_index()
)

# Sort chronologically
df_final = df_final.sort_values(
    by=["Country Code", "Year"]
)

print("\n--- FINAL DATAFRAME ---")
print(df_final.info())

print("\n--- FIRST 10 ROWS ---")
print(df_final.head(10))

print("\n--- MISSING VALUES BY INDICATOR ---")
print(df_final.isnull().sum())

print("\n--- COUNTRY-YEAR RECORDS WITH MISSING DATA ---")

missing_rows = df_final[
    df_final.isnull().any(axis=1)
]

print(missing_rows.to_string(index=False))

print("\n--- FINAL DATA QUALITY VALIDATION ---")

# 1. Check duplicate country-year records
duplicates = df_final.duplicated(
    subset=["Country Code", "Year"]
).sum()

print("Duplicate country-year records:", duplicates)

# 2. Check country coverage
print("\nNumber of countries:", df_final["Country Code"].nunique())

print("\nRecords by country:")
print(
    df_final.groupby("Country")["Year"].count()
)

# 3. Check reporting periods by country
print("\nReporting periods by country:")
print(
    df_final.groupby("Country")["Year"].nunique()
)

# 4. Validate confidence intervals
valid_intervals = df_final.dropna(
    subset=[
        "RQ Score",
        "RQ Score Lower Bound",
        "RQ Score Upper Bound"
    ]
)

invalid_intervals = valid_intervals[
    (valid_intervals["RQ Score Lower Bound"] > valid_intervals["RQ Score"]) |
    (valid_intervals["RQ Score"] > valid_intervals["RQ Score Upper Bound"])
]

print("\nInvalid confidence intervals:", len(invalid_intervals))

# Export final dataset
output_path = "data/processed/asean_wgi_regulatory_quality_1996_2024.csv"

df_final.to_csv(output_path, index=False)

print("\nDataset exported successfully!")
print("File:", output_path)
