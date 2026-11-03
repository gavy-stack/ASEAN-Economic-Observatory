
import requests

url = (
    "https://api.worldbank.org/v2/country/IDN/"
    "indicator/GOV_WGI_RL.SE"
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
    print("--- API ERROR ---")
    print(data[0])
else:
    print("--- API METADATA ---")
    print(data[0])

    print("\n--- FIRST OBSERVATION ---")
    print(data[1][0])
