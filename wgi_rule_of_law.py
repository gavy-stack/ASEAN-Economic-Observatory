
import requests

# 1. Define the API address
url = (
    "https://api.worldbank.org/v2/country/IDN/"
    "indicator/GOV_WGI_RL_SC"
)

# 2. Define the request parameters
params = {
    "date": "1996:2024",
    "format": "json",
    "per_page": 100
}

# 3. Send the request
response = requests.get(url, params=params, timeout=30)

# 4. Check whether the request succeeded
response.raise_for_status()

# 5. Convert the response into Python data
data = response.json()

# 6. Inspect the response
print("--- API METADATA ---")
print(data[0])

print("\n--- FIRST OBSERVATION ---")
print(data[1][0])
