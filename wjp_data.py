
import pandas as pd

# 1. Read the historical dataset
file_path = "data/raw/wjp_historical.xlsx"

df = pd.read_excel(
    file_path,
    sheet_name="Historical Data",
    header=1
)

# 2. Inspect the dataset
print("--- DATASET DIMENSIONS ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- FIRST FIVE ROWS ---")
print(df.head())

print("\n--- DATASET INFORMATION ---")
df.info()

# 3. Inspect the first five columns
print("\n--- FIRST FIVE COLUMNS ---")
print(df.iloc[:, :5].head(10))


# 4. Investigate historical coverage

print("\n--- YEAR DISTRIBUTION ---")
print(df["Year"].value_counts())

print("\n--- UNIQUE YEARS ---")
print(df["Year"].unique())

print("\n--- YEAR DATA TYPES ---")
print(df["Year"].apply(type).value_counts())

# 5. Investigate country coverage

print("\n--- COUNTRY COVERAGE ---")
print("Number of countries:", df["Country"].nunique())

# 6. List ASEAN countries in the dataset

asean_countries = [
    "Singapore",
    "Malaysia",
    "Philippines",
    "Thailand",
    "Indonesia",
    "Vietnam",
    "Myanmar",
    "Cambodia"
]

asean_df = df[df["Country"].isin(asean_countries)]

print("\n--- ASEAN COUNTRY COVERAGE ---")
print(asean_df["Country"].value_counts())

# 7. Investigate the years available for each ASEAN country

print("\n--- ASEAN HISTORICAL COVERAGE ---")

# Preserve the original Year column and create a text version
asean_df = asean_df.copy()
asean_df["Year_label"] = asean_df["Year"].astype(str)

# Extract the starting year from each observation period
asean_df["Year_start"] = pd.to_numeric(
    asean_df["Year_label"].str[:4]
)

# Summarise coverage for each country
coverage = (
    asean_df.groupby("Country")
    .agg(
        first_period=("Year_start", "min"),
        last_period=("Year_start", "max"),
        periods_available=("Year_label", "nunique")
    )
)

print(coverage)

# Show the actual observation periods for each country
print("\n--- AVAILABLE PERIODS BY COUNTRY ---")

periods_by_country = (
    asean_df.sort_values("Year_start")
    .groupby("Country")["Year_label"]
    .agg(lambda periods: ", ".join(periods))
)

print(periods_by_country)

# 8. Check duplicate country-year observations

print("\n--- DUPLICATE COUNTRY-YEAR PAIRS ---")

duplicates = df.duplicated(
    subset=["Country", "Year"]
).sum()

print("Duplicate observations:", duplicates)
