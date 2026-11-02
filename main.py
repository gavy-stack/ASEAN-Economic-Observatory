import requests
import pandas as pd

# 1. Connect to the World Bank API
url = "https://api.worldbank.org/v2/country/IDN/indicator/NY.GDP.MKTP.KD.ZG?date=1996:2024&format=json"

response = requests.get(url)

if response.status_code == 200:

    print("Successfully connected to World Bank!")

    # 2. Convert API response into Python data
    data = response.json()

    # 3. Check how many observations we received
    print("Total observations:", len(data[1]))

    # 4. Create an empty list
    records = []

    # 5. Extract every observation
    for observation in data[1]:

        record = {
            "Country": "Indonesia",
            "Year": int(observation["date"]),
            "GDP Growth": observation["value"]
        }

        records.append(record)

    # 6. Convert records into a DataFrame
    df = pd.DataFrame(records)

    # 7. Sort the DataFrame by Year
    df = df.sort_values(by="Year")

    # 8. Display the dataset
    print("\n--- INDONESIA GDP GROWTH DATASET ---")
    print(df)

    # 9. Inspect the dataset
    print("\n--- DATASET INFORMATION ---")
    df.info()

    # 10. Inspect missing values
    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    # 11. Check for duplicates
    print("\n--- CHECK FOR DUPLICATE RECORDS ---")
    print(df.duplicated().sum())

    # 12. Check for duplicate country-year pairs
    print("\n--- DUPLICATE COUNTRY-YEAR PAIRS ---")
    print(df.duplicated(subset=["Country", "Year"]).sum())

    # 13. Display descriptive statistics
    print("\n--- GDP GROWTH STATISTICS ---")
    print(df["GDP Growth"].describe())

else:
    print("Something went wrong!")
    print("Status code:", response.status_code)