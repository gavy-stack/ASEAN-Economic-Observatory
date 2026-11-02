
import requests

# 1. Define our API URL
url = "https://api.worldbank.org/v2/country/IDN/indicator/NY.GDP.MKTP.KD.ZG?date=1996:2024&format=json"

# 2. Send a request to the World Bank
response = requests.get(url)

# 3. Check whether the request was successful
if response.status_code == 200:
    print("Successfully connected to World Bank!")

    # 4. Convert the response into Python data
    data = response.json()

    # Display metadata
    print("\n--- METADATA ---")
    print(data[0])

    # Display economic observations
    print("\n--- OBSERVATIONS ---")
    print(data[1])

   # Display the first observation only
    print("\n--- FIRST OBSERVATION ---")

    for observation in data[1]:
        print(observation["date"], observation["value"])

else:
    print("Something went wrong!")
    print("Status code:", response.status_code)
