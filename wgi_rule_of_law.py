
from numpy import rint
import requests

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

    print(f"\n--- {name} ---")

    if len(data) < 2 or not isinstance(data[1], list):
        print("API ERROR:", data[0])
    else:
        print("Observations:", data[0]["total"])
        print("Latest observation:", data[1][0])
        year_sets[name] = {
            item["date"] for item in data[1]
        }

        print("Available years:", sorted(year_sets[name]))

print("\n--- YEAR COVERAGE VALIDATION ---")

reference_years = year_sets["RL Estimate"]

for name, years in year_sets.items():
    if years == reference_years:
        print(f"{name}: MATCH")
    else:
        print(f"{name}: MISMATCH")
        print("Missing years:", sorted(reference_years - years))
        print("Additional years:", sorted(years - reference_years))