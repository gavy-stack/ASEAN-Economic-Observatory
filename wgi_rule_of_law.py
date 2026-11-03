
from numpy import rint
import requests

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

# WGI Rule of Law indicators
indicators = {
    "RL Estimate": "GOV_WGI_RL.EST",
    "RL Score": "GOV_WGI_RL.SC",
    "RL Score Lower Bound": "GOV_WGI_RL.SC_LB",
    "RL Score Upper Bound": "GOV_WGI_RL.SC_UB",
    "RL Standard Error": "GOV_WGI_RL.SE",
    "RL Number of Sources": "GOV_WGI_RL.SR"
}

country_code = "IDN"

year_sets = {}
all_data = []   

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

print("\n--- YEAR COVERAGE VALIDATION ---")

reference_years = year_sets["RL Estimate"]

for name, years in year_sets.items():
    if years == reference_years:
        print(f"{name}: MATCH")
    else:
        print(f"{name}: MISMATCH")
        print("Missing years:", sorted(reference_years - years))
        print("Additional years:", sorted(years - reference_years))