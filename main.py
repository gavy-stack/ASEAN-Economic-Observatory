import requests
import pandas as pd

# 1. Connect to the World Bank API
url = "https://api.worldbank.org/v2/country/BRN;KHM;IDN;LAO;MYS;MMR;PHL;SGP;THA;TLS;VNM/indicator/NY.GDP.MKTP.KD.ZG?date=1996:2024&format=json&per_page=1000"
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
    "Country": observation["country"]["value"],
    "Country Code": observation["countryiso3code"],
    "Year": int(observation["date"]),
    "GDP Growth": observation["value"]
}
        records.append(record)

    # 6. Convert records into a DataFrame
    df = pd.DataFrame(records)

    # 7. Country Coverage
    print("\n--- COUNTRY COVERAGE ---")
    print(df["Country"].nunique(), "countries found")

    # 8. Observations per country
    print("\n--- OBSERVATIONS PER COUNTRY ---")
    print(df["Country"].value_counts())

    # 7. Sort the DataFrame by Country and Year
    df = df.sort_values(by=["Country", "Year"])

    # 8. Inspect missing values
    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    # 9. Check for duplicates
    print("\n--- CHECK FOR DUPLICATE RECORDS ---")
    print(df.duplicated().sum())

    # 10. Check for duplicate country-year pairs
    print("\n--- DUPLICATE COUNTRY-YEAR PAIRS ---")
    print(df.duplicated(subset=["Country", "Year"]).sum())
    
    # 11. Display descriptive statistics
    print("\n--- GDP GROWTH STATISTICS ---")
    print(df["GDP Growth"].describe())

    # 12. Display the cleaned dataset
    print("\n--- DATASET INFORMATION ---")
    df.info()

    # 13. Export the dataset to CSV
    df.to_csv("data/processed/asean_gdp_growth.csv", index=False)

    print("\nDataset successfully saved!")

else:
    print("Something went wrong!")
    print("Status code:", response.status_code)