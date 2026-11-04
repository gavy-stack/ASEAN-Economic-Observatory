
import requests

url = "https://api.worldbank.org/v2/country/IDN/indicator/GOV_WGI_RQ.EST"

params = {
    "date": "1996:2024",
    "format": "json",
    "per_page": 100,
    "source": 3
}

response = requests.get(url, params=params, timeout=30)

print("Status code:", response.status_code)

response.raise_for_status()

data = response.json()

print("\n--- API METADATA ---")
print(data[0])

print("\n--- FIRST OBSERVATION ---")
print(data[1][0])

print("\n--- TOTAL OBSERVATIONS ---")
print(len(data[1]))

# Checking for missing years in the data

expected_years = set(range(1996, 2025))

available_years = {
    int(observation["date"])
    for observation in data[1]
}

missing_years = sorted(expected_years - available_years)

print("\n--- YEAR COVERAGE ---")
print("Expected years:", len(expected_years))
print("Available years:", len(available_years))
print("Missing years:", missing_years)