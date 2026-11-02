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

    # 7. Calculate average GDP growth for each country
    growth_ranking = df.groupby("Country")["GDP Growth"].mean()

    # 8. Sort the countries from highest to lowest average growth
    growth_ranking = growth_ranking.sort_values(ascending=False)

    # 9. Display the ranking
    print("\n--- AVERAGE GDP GROWTH RANKING ---")
    print(growth_ranking.round(2))

    # 10. Analyse GDP growth patterns for each ASEAN country
    growth_analysis = df.groupby("Country")["GDP Growth"].agg(
    ["mean", "median", "std", "min", "max", "count"]
    )

    # 11. Sort by average GDP growth
    growth_analysis = growth_analysis.sort_values(
    by="mean",
    ascending=False
    )

    # 12. Display the analysis
    print("\n--- ASEAN GDP GROWTH ANALYSIS ---")
    print(growth_analysis.round(2))

    # 13. Country Coverage
    print("\n--- COUNTRY COVERAGE ---")
    print(df["Country"].nunique(), "countries found")

    # 14. Observations per country
    print("\n--- OBSERVATIONS PER COUNTRY ---")
    print(df["Country"].value_counts())

    # 15. Sort the DataFrame by Country and Year
    df = df.sort_values(by=["Country", "Year"])

    # 16. calculate overall average GDP growth
    asean_average = df["GDP Growth"].mean()
    
    print("\n--- OVERALL ASEAN GDP GROWTH ---")
    print("Average GDP Growth:", round(asean_average, 2), "%")

    # 17. Inspect missing values
    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    # 18. Check for duplicates
    print("\n--- CHECK FOR DUPLICATE RECORDS ---")
    print(df.duplicated().sum())

    # 19. Check for duplicate country-year pairs
    print("\n--- DUPLICATE COUNTRY-YEAR PAIRS ---")
    print(df.duplicated(subset=["Country", "Year"]).sum())
    
    # 20. Display descriptive statistics
    print("\n--- GDP GROWTH STATISTICS ---")
    print(df["GDP Growth"].describe())

    # 21. Display the cleaned dataset
    print("\n--- DATASET INFORMATION ---")
    df.info()

    # 22. Export the dataset to CSV
    df.to_csv("data/processed/asean_gdp_growth.csv", index=False)

    print("\nDataset successfully saved!")

else:
    print("Something went wrong!")
    print("Status code:", response.status_code)