import requests
import pandas as pd

# 1. Connect to the World Bank API
url = "https://api.worldbank.org/v2/country/BRN;KHM;IDN;LAO;MYS;MMR;PHL;SGP;THA;TLS;VNM/indicator/FS.AST.PRVT.GD.ZS?date=1996:2024&format=json&per_page=1000"

response = requests.get(url, timeout=30)

if response.status_code == 200:

    print("Successfully connected to World Bank!")

    # 2. Convert API response into Python data
    data = response.json()

    # 3. Create an empty list
    records = []

    # 4. Extract every observation
    for observation in data[1]:

        record = {
            "Country": observation["country"]["value"],
            "Country Code": observation["countryiso3code"],
            "Year": int(observation["date"]),
            "Domestic Credit (% of GDP)": observation["value"]
        }

        records.append(record)

    # 5. Convert records into a DataFrame
    df = pd.DataFrame(records)

    # 6. Sort the dataset
    df = df.sort_values(by=["Country", "Year"])

    # 7. Check how many observations we received
    print("Total observations:", len(data[1]))

    # 8. Inspect country coverage
    print("\n--- COUNTRY COVERAGE ---")
    print(df["Country"].nunique(), "countries found")

    # 9. Count observations per country
    print("\n--- OBSERVATIONS PER COUNTRY ---")
    print(df["Country"].value_counts())

    # 10. Check missing values
    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())

    # 11. Check duplicate country-year pairs
    print("\n--- DUPLICATE COUNTRY-YEAR PAIRS ---")
    print(df.duplicated(subset=["Country Code", "Year"]).sum())

    # 12. Display dataset information
    print("\n--- DATASET INFORMATION ---")
    df.info()

    # 13. Export the dataset
    df.to_csv(
        "data/processed/asean_private_credit.csv",
        index=False
    )

    print("\nFinancial dataset successfully saved!")

    # 14. Investigate missing values by country

    missing_by_country = (
        df["Domestic Credit (% of GDP)"]
        .isna()
        .groupby(df["Country"])
        .sum()
    )

    print("\n--- MISSING VALUES BY COUNTRY ---")
    print(missing_by_country)

    # 15. Display country-years with missing credit data

    missing_rows = df[
        df["Domestic Credit (% of GDP)"].isna()
    ]

    print("\n--- MISSING COUNTRY-YEAR OBSERVATIONS ---")
    print(missing_rows[["Country", "Year"]].to_string(index=False))

    # 16. Count missing observations by year

    missing_by_year = (
        df["Domestic Credit (% of GDP)"]
        .isna()
        .groupby(df["Year"])
        .sum()
    )

    print("\n--- MISSING VALUES BY YEAR ---")
    print(missing_by_year[missing_by_year > 0])

    # 17. Create a table showing missing observations by country and year

    missing_pivot = df.pivot(
        index="Country",
        columns="Year",
        values="Domestic Credit (% of GDP)"
    )

    print("\n--- MISSING DATA MAP ---")
    print(missing_pivot.isna().astype(int).to_string())

    # 18. Display exact missing years for each country

    print("\n--- EXACT MISSING YEARS BY COUNTRY ---")

    for country in df["Country"].unique():

        missing_years = df.loc[
        (df["Country"] == country) &
        (df["Domestic Credit (% of GDP)"].isna()),
        "Year"
        ].tolist()

        if missing_years:
            print(f"{country}: {missing_years}")

else:
    print("Something went wrong!")
    print("Status code:", response.status_code)