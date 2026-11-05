import requests
import pandas as pd
from pathlib import Path

# ASEAN countries
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

# WGI Regulatory Quality indicators
indicators = {
    "RQ Estimate": "GOV_WGI_RQ.EST",
    "RQ Score": "GOV_WGI_RQ.SC",
    "RQ Score Lower Bound": "GOV_WGI_RQ.SC_LB",
    "RQ Score Upper Bound": "GOV_WGI_RQ.SC_UB",
    "RQ Standard Error": "GOV_WGI_RQ.SE",
    "RQ Number of Sources": "GOV_WGI_RQ.SR"
}

all_data = []

# Collect API observations
for country_name, country_code in countries.items():

    print(f"\nCollecting {country_name}...")

    for indicator_name, indicator_code in indicators.items():

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

        if not isinstance(data, list) or len(data) < 2:
            raise ValueError(
                f"Invalid API response: {country_code}, {indicator_code}"
            )

        observations = data[1]

        for item in observations:

            all_data.append({
                "Country": country_name,
                "Country Code": country_code,
                "Year": int(item["date"]),
                "Indicator": indicator_name,
                "Indicator Code": indicator_code,
                "Value": item["value"]
            })

        print(f"  {indicator_name}: {len(observations)} observations")

# Create DataFrame
df = pd.DataFrame(all_data)

# Save raw observations
output_path = Path("data/raw/wgi_regulatory_quality.csv")

df.to_csv(output_path, index=False)

print("\n========== COLLECTION SUMMARY ==========")
print("Total observations:", len(df))
print("Countries:", df["Country Code"].nunique())
print("Indicators:", df["Indicator Code"].nunique())
print("Saved to:", output_path)